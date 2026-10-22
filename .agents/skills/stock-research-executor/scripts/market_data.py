#!/usr/bin/env python3
"""Timestamped price snapshot + daily history + technical indicators, as markdown.

Usage:  market_data.py TICKER [--bench SPY] [--out notes/00_market.md] [--raw notes/raw/]
Source: Yahoo Finance chart API (Grade C market data). The raw response is saved with its SHA-256
so the price used by the report can be audited later. Method slugs in [brackets] are in ../methods.md.
Indicators describe price behaviour only; they never feed the fundamental signal rating.
"""
import argparse, datetime as dt, hashlib, json, math, os, sys, urllib.error, urllib.parse, urllib.request

URL = "https://query1.finance.yahoo.com/v8/finance/chart/{}?range=2y&interval=1d"


def fetch(ticker):
    url = URL.format(urllib.parse.quote(ticker))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:
        sys.exit(f"{ticker}: Yahoo chart API returned HTTP {e.code} (check the symbol, e.g. 0700.HK, 600519.SS)")
    res = json.loads(raw)["chart"]["result"]
    if not res:
        sys.exit(f"{ticker}: no data from Yahoo chart API")
    return url, raw, res[0]


def series(res):
    q = res["indicators"]["quote"][0]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose") or q["close"]
    rows = [(dt.datetime.fromtimestamp(t, dt.timezone.utc).date(), h, l, c, a)
            for t, h, l, c, a in zip(res["timestamp"], q["high"], q["low"], q["close"], adj)]
    return [r for r in rows if None not in r]


def sma(xs, n):
    return sum(xs[-n:]) / n if len(xs) >= n else None


def ema(xs, n):
    k, e = 2 / (n + 1), xs[0]
    out = [e]
    for x in xs[1:]:
        e = x * k + e * (1 - k)
        out.append(e)
    return out


def wilder(xs, n):  # Wilder smoothing: seed with the simple mean, then (prev*(n-1)+x)/n
    if len(xs) < n:
        return None
    s = sum(xs[:n]) / n
    for x in xs[n:]:
        s = (s * (n - 1) + x) / n
    return s


def rsi(closes, n=14):
    d = [b - a for a, b in zip(closes, closes[1:])]
    up, dn = wilder([max(x, 0) for x in d], n), wilder([max(-x, 0) for x in d], n)
    if up is None:
        return None
    return 100.0 if dn == 0 else 100 - 100 / (1 + up / dn)


def atr(rows, n=14):
    tr = [max(h - l, abs(h - pc), abs(l - pc)) for (_, h, l, _, _), (_, _, _, pc, _) in zip(rows[1:], rows)]
    return wilder(tr, n)


def macd(closes):
    line = [a - b for a, b in zip(ema(closes, 12), ema(closes, 26))]
    sig = ema(line, 9)
    return line[-1], sig[-1], line[-1] - sig[-1]


def ret(adj, days):
    return adj[-1] / adj[-1 - days] - 1 if len(adj) > days else None


def pct(v):
    return "n/a" if v is None else f"{v * 100:+.1f}%"


def num(v):
    return "n/a" if v is None else f"{v:,.2f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker", help="Yahoo symbol, e.g. ORCL, 0700.HK, 600519.SS")
    ap.add_argument("--bench", default="SPY", help="benchmark for relative return ('' to skip)")
    ap.add_argument("--out")
    ap.add_argument("--raw", help="directory to save the raw JSON response")
    a = ap.parse_args()

    retrieved = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    url, raw, res = fetch(a.ticker)
    m, rows = res["meta"], series(res)
    if len(rows) < 30:
        sys.exit(f"{a.ticker}: only {len(rows)} daily bars; not enough history")
    period = m.get("currentTradingPeriod", {}).get("regular", {})
    if period.get("start", 0) <= m["regularMarketTime"] < period.get("end", 0):  # market open: drop partial bar
        rows = rows[:-1]
    closes, adj = [r[3] for r in rows], [r[4] for r in rows]
    quote_utc = dt.datetime.fromtimestamp(m["regularMarketTime"], dt.timezone.utc)
    quote_local = quote_utc + dt.timedelta(seconds=m.get("gmtoffset", 0))
    digest = hashlib.sha256(raw).hexdigest()
    if a.raw:
        os.makedirs(a.raw, exist_ok=True)
        path = os.path.join(a.raw, f"{a.ticker}_chart_{quote_utc:%Y%m%dT%H%MZ}.json")
        with open(path, "wb") as fh:
            fh.write(raw)

    yr = rows[-252:]
    hi, lo = max(r[3] for r in yr), min(r[3] for r in yr)
    s50, s200 = sma(closes, 50), sma(closes, 200)
    ml, ms, mh = macd(closes)
    a14 = atr(rows)
    daily = [math.log(b / a_) for a_, b in zip(adj[-31:], adj[-30:])]
    vol = (sum((x - sum(daily) / len(daily)) ** 2 for x in daily) / (len(daily) - 1)) ** 0.5 * 252 ** 0.5
    mom = adj[-22] / adj[-253] - 1 if len(adj) > 252 else None
    bench = None
    if a.bench:
        try:
            badj = [r[4] for r in series(fetch(a.bench)[2])]
            bench = ret(badj, 252)
        except Exception as e:  # benchmark is optional context
            print(f"benchmark {a.bench} skipped: {e}", file=sys.stderr)
    r12 = ret(adj, 252)

    out = [f"# {a.ticker} ({m.get('longName', '')}): Market Data Snapshot", "",
           f"- **Price**: {m['regularMarketPrice']:,.2f} {m.get('currency', '')} on {m.get('fullExchangeName', '')}, "
           f"quote time {quote_utc:%Y-%m-%d %H:%M} UTC ({quote_local:%Y-%m-%d %H:%M} {m.get('timezone', '')}) "
           "[Grade C market data]",
           f"- **Last completed daily close**: {closes[-1]:,.2f} on {rows[-1][0]} (unadjusted; indicators use "
           "completed sessions only)",
           f"- **Source**: Yahoo Finance chart API, {url}",
           f"- **Retrieved**: {retrieved}; response SHA-256 `{digest[:16]}…`" +
           (f"; raw saved to `{path}`" if a.raw else ""),
           "- Use this price, with its quote time, for every price-dependent number in the report.",
           "", "## Technical Context (descriptive only; not part of the signal rating)", "",
           "| Indicator | Value | Method |", "|---|---|---|",
           f"| 52-week high / low (close) | {num(hi)} / {num(lo)} | definition |",
           f"| Price vs. 52-week high | {pct(closes[-1] / hi - 1)} | definition |",
           f"| 50-day / 200-day SMA | {num(s50)} / {num(s200)} | [brock-1992] |",
           f"| Price vs. 200-day SMA | {pct(closes[-1] / s200 - 1 if s200 else None)} | [brock-1992] |",
           f"| RSI (14, Wilder) | {num(rsi(closes))} | [wilder-1978] |",
           f"| ATR (14, Wilder) | {num(a14)} ({pct(a14 / closes[-1] if a14 else None).lstrip('+')} of price) | [wilder-1978] |",
           f"| MACD (12,26,9): line / signal / histogram | {num(ml)} / {num(ms)} / {num(mh)} | [appel-2005] |",
           f"| 30-day realized volatility (annualized) | {pct(vol).lstrip('+')} | [def-volatility] |",
           f"| 12-month total return | {pct(r12)} | definition |",
           f"| 12-1 month momentum | {pct(mom)} | [jegadeesh-titman-1993] |"]
    if bench is not None and r12 is not None:
        out.append(f"| 12-month return vs. {a.bench} | {pct(r12 - bench)} ({a.bench} {pct(bench)}) | definition |")
    text = "\n".join(out) + "\n"
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, "w") as fh:
            fh.write(text)
        print(f"wrote {a.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
