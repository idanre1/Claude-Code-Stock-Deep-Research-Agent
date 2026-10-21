#!/usr/bin/env python3
"""Deterministic valuation math. Agents choose the inputs (and cite them); this script does the arithmetic.

  valuation.py wacc    --rf 0.043 --beta 1.1 --erp 0.045 [--kd 0.05 --tax 0.21 --debt 90e9 --equity 500e9]
  valuation.py dcf     --fcf0 12e9 --growth 0.12,0.10,0.08,0.06,0.05 --tg 0.025 --rate 0.09 \
                       --net-debt 80e9 --shares 2.8e9 [--price 150 --rf 0.043]
  valuation.py reverse --price 150 --fcf0 12e9 --years 10 --tg 0.025 --rate 0.09 --net-debt 80e9 --shares 2.8e9

All rates are decimals. Use one unit for money (e.g. USD) and the share count in the same scale.
Method slugs in [brackets] are defined in ../methods.md.
"""
import argparse, sys


def pv_per_share(fcf0, growth, tg, rate, net_debt, shares):
    if fcf0 <= 0:
        sys.exit("FCF0 must be > 0. When current FCF is negative (e.g. a capex build-out), use a normalized base "
                 "(OCF − maintenance capex, or a multi-year average) and state the basis.")
    if rate <= tg:
        sys.exit(f"discount rate {rate:.2%} must exceed terminal growth {tg:.2%} [gordon-1959]")
    fcf, pv = fcf0, 0.0
    for t, g in enumerate(growth, 1):
        fcf *= 1 + g
        pv += fcf / (1 + rate) ** t
    tv = fcf * (1 + tg) / (rate - tg)
    pv_tv = tv / (1 + rate) ** len(growth)
    ev = pv + pv_tv
    return (ev - net_debt) / shares, ev, pv_tv / ev, fcf


def growth_path(s, years):
    g = [float(x) for x in s.split(",")]
    return g if len(g) > 1 else g * years


def wacc(a):
    ke = a.rf + a.beta * a.erp
    print(f"- Cost of equity ke = rf + β·ERP = {a.rf:.2%} + {a.beta:.2f} × {a.erp:.2%} = **{ke:.2%}** [sharpe-1964]")
    if a.debt is not None and a.equity is not None and a.kd is not None:
        v = a.debt + a.equity
        w = a.equity / v * ke + a.debt / v * a.kd * (1 - a.tax)
        print(f"- WACC = E/V·ke + D/V·kd·(1−t) = {a.equity / v:.1%} × {ke:.2%} + {a.debt / v:.1%} × "
              f"{a.kd:.2%} × (1 − {a.tax:.0%}) = **{w:.2%}** [damodaran-2007]")


def dcf(a):
    g = growth_path(a.growth, a.years)
    v, ev, tv_share, _ = pv_per_share(a.fcf0, g, a.tg, a.rate, a.net_debt, a.shares)
    print(f"- Inputs: FCF0 {a.fcf0:,.0f}; growth {', '.join(f'{x:.1%}' for x in g)}; terminal g {a.tg:.2%}; "
          f"discount rate {a.rate:.2%}; net debt {a.net_debt:,.0f}; shares {a.shares:,.0f}")
    print(f"- Enterprise value {ev:,.0f}; terminal value is {tv_share:.0%} of EV [damodaran-2007] [gordon-1959]")
    print(f"- **Intrinsic value per share: {v:,.2f}**" +
          (f" vs. price {a.price:,.2f} → {v / a.price - 1:+.1%}" if a.price else ""))
    if a.rf is not None and a.tg > a.rf:
        print(f"- WARNING: terminal growth {a.tg:.2%} exceeds the risk-free rate {a.rf:.2%}; "
              "long-run growth should not exceed it [damodaran-2007]")
    if tv_share > 0.8:
        print("- WARNING: terminal value exceeds 80% of EV; the result mostly reflects terminal assumptions")
    rates = [a.rate - 0.01, a.rate, a.rate + 0.01]
    tgs = [a.tg - 0.005, a.tg, a.tg + 0.005]
    print("\nSensitivity, value per share (rows: discount rate, columns: terminal g):\n")
    print("| rate \\ g | " + " | ".join(f"{t:.2%}" for t in tgs) + " |")
    print("|---|" + "---|" * len(tgs))
    for r in rates:
        cells = [f"{pv_per_share(a.fcf0, g, t, r, a.net_debt, a.shares)[0]:,.2f}" if r > t else "n/m" for t in tgs]
        print(f"| {r:.2%} | " + " | ".join(cells) + " |")


def reverse(a):
    f = lambda x: pv_per_share(a.fcf0, [x] * a.years, a.tg, a.rate, a.net_debt, a.shares)[0] - a.price
    lo, hi = -0.5, 1.0
    if f(lo) > 0 or f(hi) < 0:
        sys.exit("price is outside the range implied by growth of -50%..100%; check inputs")
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    g = (lo + hi) / 2
    fcf_n = a.fcf0 * (1 + g) ** a.years
    print(f"- Price {a.price:,.2f} implies **{g:.1%} annual FCF growth for {a.years} years** "
          f"(FCF {a.fcf0:,.0f} → {fcf_n:,.0f}), then {a.tg:.2%} forever, at a {a.rate:.2%} discount rate "
          "[rappaport-mauboussin-2001]")
    print("- Compare with historical FCF/revenue CAGR [def-cagr] and consensus; state whether the implied path is plausible.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    w = sub.add_parser("wacc")
    for k in ("rf", "beta", "erp"):
        w.add_argument(f"--{k}", type=float, required=True)
    for k in ("kd", "debt", "equity"):
        w.add_argument(f"--{k}", type=float)
    w.add_argument("--tax", type=float, default=0.21)
    for name in ("dcf", "reverse"):
        p = sub.add_parser(name)
        p.add_argument("--fcf0", type=float, required=True, help="base-year free cash flow")
        p.add_argument("--tg", type=float, required=True, help="terminal growth")
        p.add_argument("--rate", type=float, required=True, help="discount rate (WACC)")
        p.add_argument("--net-debt", type=float, required=True, help="debt minus cash")
        p.add_argument("--shares", type=float, required=True, help="diluted shares")
        p.add_argument("--years", type=int, default=5 if name == "dcf" else 10)
        p.add_argument("--price", type=float, required=name == "reverse")
        if name == "dcf":
            p.add_argument("--growth", required=True, help="one rate, or a comma-separated path per year")
            p.add_argument("--rf", type=float, help="risk-free rate, for the terminal-growth check")
    a = ap.parse_args()
    {"wacc": wacc, "dcf": dcf, "reverse": reverse}[a.cmd](a)


if __name__ == "__main__":
    main()
