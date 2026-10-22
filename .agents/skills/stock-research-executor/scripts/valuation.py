#!/usr/bin/env python3
"""Deterministic valuation math. Agents choose the inputs (and cite them); this script does the arithmetic.

  valuation.py wacc    --rf 0.043 --beta 1.1 --erp 0.045 [--kd 0.05 --tax 0.21 --debt 90e9 --equity 500e9]
  valuation.py dcf     --fcf0 12e9 --growth 0.12,0.10,0.08,0.06,0.05 --tg 0.025 --rate 0.09 \
                       --net-debt 80e9 --shares 2.8e9 [--price 150 --rf 0.043]
  valuation.py dcf     --fcf-path=-20e9,-8e9,2e9,9e9,14e9 --tg 0.025 --rate 0.09 --net-debt 80e9 --shares 2.8e9
  valuation.py reverse --price 150 --fcf0 12e9 --years 10 --tg 0.025 --rate 0.09 --net-debt 80e9 --shares 2.8e9
  valuation.py reverse --price 150 --fcf-path=-20e9,-8e9,2e9 --years 7 ...   (solve growth after the explicit years)

--fcf-path gives explicit signed yearly FCF (e.g. a funded build-out with negative years); only the
final year must be positive. Add --save notes/valuation_runs.jsonl to log inputs and outputs.

  valuation.py replay notes/valuation_runs.jsonl   (re-run every logged run, compare results, write nothing)

All rates are decimals. Use one unit for money (e.g. USD) and the share count in the same scale.
Method slugs in [brackets] are defined in ../methods.md.
"""
import argparse, contextlib, datetime as dt, io, json, math, sys


def grow(fcf0, growth):
    out = []
    for g in growth:
        fcf0 *= 1 + g
        out.append(fcf0)
    return out


def value(fcfs, tg, rate, net_debt, shares):
    """Per-share value, EV and terminal share of EV for explicit yearly FCFs plus a Gordon terminal value."""
    if fcfs[-1] <= 0:
        sys.exit("final-year FCF must be > 0 to anchor a terminal value; extend the path to a steady state.")
    if rate <= tg:
        sys.exit(f"discount rate {rate:.2%} must exceed terminal growth {tg:.2%} [gordon-1959]")
    pv = sum(f / (1 + rate) ** t for t, f in enumerate(fcfs, 1))
    pv_tv = fcfs[-1] * (1 + tg) / (rate - tg) / (1 + rate) ** len(fcfs)
    ev = pv + pv_tv
    return (ev - net_debt) / shares, ev, (pv_tv / ev if ev > 0 else None)


def need_fcf0(a):
    if a.fcf0 is None or a.fcf0 <= 0:
        sys.exit("need --fcf0 > 0, or --fcf-path. When current FCF is negative (e.g. a capex build-out), give the "
                 "build-out years explicitly with --fcf-path, or use a normalized base and state the basis.")


def path(s):
    return [float(x) for x in s.split(",")]


def save(a, result):
    if a.save:
        rec = {"utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "cmd": a.cmd,
               "inputs": {k: v for k, v in vars(a).items() if k not in ("cmd", "save") and v is not None},
               "result": result}
        with open(a.save, "a") as fh:
            fh.write(json.dumps(rec) + "\n")
    return result


def growth_path(s, years):
    g = path(s)
    return g if len(g) > 1 else g * years


def wacc(a):
    ke = a.rf + a.beta * a.erp
    print(f"- Cost of equity ke = rf + β·ERP = {a.rf:.2%} + {a.beta:.2f} × {a.erp:.2%} = **{ke:.2%}** [sharpe-1964]")
    if a.debt is not None and a.equity is not None and a.kd is not None:
        v = a.debt + a.equity
        w = a.equity / v * ke + a.debt / v * a.kd * (1 - a.tax)
        print(f"- WACC = E/V·ke + D/V·kd·(1−t) = {a.equity / v:.1%} × {ke:.2%} + {a.debt / v:.1%} × "
              f"{a.kd:.2%} × (1 − {a.tax:.0%}) = **{w:.2%}** [damodaran-2007]")
        return save(a, {"ke": ke, "wacc": w})
    return save(a, {"ke": ke})


def dcf(a):
    if a.fcf_path:
        fcfs = path(a.fcf_path)
        desc = "explicit FCF " + ", ".join(f"{x:,.0f}" for x in fcfs)
    else:
        need_fcf0(a)
        if not a.growth:
            sys.exit("dcf needs --growth with --fcf0, or --fcf-path")
        g = growth_path(a.growth, a.years)
        fcfs = grow(a.fcf0, g)
        desc = f"FCF0 {a.fcf0:,.0f}; growth {', '.join(f'{x:.1%}' for x in g)}"
    v, ev, tv_share = value(fcfs, a.tg, a.rate, a.net_debt, a.shares)
    print(f"- Inputs: {desc}; terminal g {a.tg:.2%}; "
          f"discount rate {a.rate:.2%}; net debt {a.net_debt:,.0f}; shares {a.shares:,.0f}")
    tv_txt = f"{tv_share:.0%} of EV" if tv_share is not None else "n/m (EV ≤ 0)"
    print(f"- Enterprise value {ev:,.0f}; terminal value is {tv_txt} [damodaran-2007] [gordon-1959]")
    print(f"- **Intrinsic value per share: {v:,.2f}**" +
          (f" vs. price {a.price:,.2f} → {v / a.price - 1:+.1%}" if a.price else ""))
    if a.rf is not None and a.tg > a.rf:
        print(f"- WARNING: terminal growth {a.tg:.2%} exceeds the risk-free rate {a.rf:.2%}; "
              "long-run growth should not exceed it [damodaran-2007]")
    if tv_share is None or tv_share > 0.8:
        print("- WARNING: terminal value exceeds 80% of EV; the result mostly reflects terminal assumptions")
    if v < 0:
        print("- NOTE: negative equity value; equity cannot be worth less than 0, report the floor and the raw value")
    rates = [a.rate - 0.01, a.rate, a.rate + 0.01]
    tgs = [a.tg - 0.005, a.tg, a.tg + 0.005]
    print("\nSensitivity, value per share (rows: discount rate, columns: terminal g):\n")
    print("| rate \\ g | " + " | ".join(f"{t:.2%}" for t in tgs) + " |")
    print("|---|" + "---|" * len(tgs))
    for r in rates:
        cells = [f"{value(fcfs, t, r, a.net_debt, a.shares)[0]:,.2f}" if r > t else "n/m" for t in tgs]
        print(f"| {r:.2%} | " + " | ".join(cells) + " |")
    return save(a, {"value_per_share": v, "ev": ev, "tv_share_of_ev": tv_share, "fcfs": fcfs})


def reverse(a):
    fixed = path(a.fcf_path) if a.fcf_path else []
    if fixed:
        start = fixed[-1]
        if start <= 0:
            sys.exit("the last --fcf-path year must be > 0 to grow from it")
    else:
        need_fcf0(a)
        start = a.fcf0
    f = lambda x: value(fixed + grow(start, [x] * a.years), a.tg, a.rate, a.net_debt, a.shares)[0] - a.price
    lo, hi = -0.5, 1.0
    if f(lo) > 0 or f(hi) < 0:
        sys.exit("price is outside the range implied by growth of -50%..100%; check inputs")
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    g = (lo + hi) / 2
    fcf_n = start * (1 + g) ** a.years
    lead = f"after {len(fixed)} explicit years, " if fixed else ""
    print(f"- Price {a.price:,.2f} implies, {lead}**{g:.1%} annual FCF growth for {a.years} years** "
          f"(FCF {start:,.0f} → {fcf_n:,.0f}), then {a.tg:.2%} forever, at a {a.rate:.2%} discount rate "
          "[rappaport-mauboussin-2001]")
    print("- Compare with historical FCF/revenue CAGR [def-cagr] and consensus; state whether the implied path is plausible.")
    return save(a, {"implied_growth": g, "final_fcf": fcf_n})


def same(x, y):
    if isinstance(x, list):
        return isinstance(y, list) and len(x) == len(y) and all(map(same, x, y))
    if isinstance(x, float) or isinstance(y, float):
        return x is not None and y is not None and math.isclose(x, y, rel_tol=1e-9, abs_tol=1e-9)
    return x == y


def replay(log):
    """Re-run each logged run without saving; return the list of mismatch messages."""
    bad = []
    for n, line in enumerate(open(log), 1):
        rec = json.loads(line)
        argv = [rec["cmd"]] + [f"--{k.replace('_', '-')}={v}" for k, v in rec["inputs"].items()]
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                a = parser().parse_args(argv)
                got = CMDS[a.cmd](a)
        except SystemExit as e:
            bad.append(f"line {n} ({rec['cmd']}): fails on replay: {e}")
            continue
        diff = [k for k in rec["result"] if not same(rec["result"][k], got.get(k))]
        if diff:
            bad.append(f"line {n} ({rec['cmd']}): {', '.join(diff)} differ: logged {[rec['result'][k] for k in diff]}"
                       f" vs replay {[got.get(k) for k in diff]}")
    return bad


def parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    w = sub.add_parser("wacc")
    for k in ("rf", "beta", "erp"):
        w.add_argument(f"--{k}", type=float, required=True)
    for k in ("kd", "debt", "equity"):
        w.add_argument(f"--{k}", type=float)
    w.add_argument("--tax", type=float, default=0.21)
    for p in (w,):
        p.add_argument("--save", help="append inputs and result to this JSONL file")
    for name in ("dcf", "reverse"):
        p = sub.add_parser(name)
        p.add_argument("--fcf0", type=float, help="base-year free cash flow (> 0)")
        p.add_argument("--fcf-path", help="explicit signed FCF per year, comma-separated (use --fcf-path=-1e9,...)")
        p.add_argument("--tg", type=float, required=True, help="terminal growth")
        p.add_argument("--rate", type=float, required=True, help="discount rate (WACC)")
        p.add_argument("--net-debt", type=float, required=True, help="debt minus cash")
        p.add_argument("--shares", type=float, required=True, help="diluted shares")
        p.add_argument("--years", type=int, default=5 if name == "dcf" else 10)
        p.add_argument("--price", type=float, required=name == "reverse")
        p.add_argument("--save", help="append inputs and result to this JSONL file")
        if name == "dcf":
            p.add_argument("--growth", help="one rate, or a comma-separated path per year")
            p.add_argument("--rf", type=float, help="risk-free rate, for the terminal-growth check")
    sub.add_parser("replay").add_argument("log", help="valuation_runs.jsonl written by --save")
    return ap


CMDS = {"wacc": wacc, "dcf": dcf, "reverse": reverse}


def main():
    a = parser().parse_args()
    if a.cmd == "replay":
        bad = replay(a.log)
        print("\n".join(bad) or f"replay OK: every run in {a.log} reproduces")
        sys.exit(1 if bad else 0)
    CMDS[a.cmd](a)


if __name__ == "__main__":
    main()
