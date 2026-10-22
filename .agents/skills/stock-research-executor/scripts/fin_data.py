#!/usr/bin/env python3
"""Annual financials from SEC EDGAR XBRL (US filers) + quality metrics, as markdown.

Usage:  fin_data.py TICKER [--years 10] [--out notes/00_financials.md] [--json notes/00_financials.json]
Env:    SEC_USER_AGENT="Your Name you@domain.com"  (SEC asks for a contact)
Method slugs in [brackets] are defined in ../methods.md.
"""
import argparse, datetime as dt, gzip, json, os, sys, urllib.request

UA = os.environ.get("SEC_USER_AGENT", "stock-research-agent research@example.com")
ANNUAL_FORMS = ("10-K", "10-K/A", "20-F", "20-F/A", "40-F")

TAGS = {  # first tag found wins for each fiscal year
    "rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"],
    "cogs": ["CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfGoodsSold"],
    "gp": ["GrossProfit"],
    "opinc": ["OperatingIncomeLoss"],
    "ni": ["NetIncomeLoss", "ProfitLoss"],
    "eps": ["EarningsPerShareDiluted"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
    "buyback": ["PaymentsForRepurchaseOfCommonStock"],
    "div": ["PaymentsOfDividends", "PaymentsOfDividendsCommonStock"],
    "shares": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
    "assets": ["Assets"],
    "ca": ["AssetsCurrent"],
    "cl": ["LiabilitiesCurrent"],
    "equity": ["StockholdersEquity",
               "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
    "ltdebt": ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations", "LongTermNotesPayable",
               "LongTermDebt"],
    "debt": ["DebtLongtermAndShorttermCombinedAmount", "DebtAndCapitalLeaseObligations"],
    "stdebt": ["DebtCurrent", "LongTermDebtCurrent"],
    "cp": ["CommercialPaper"],
    "cash": ["CashAndCashEquivalentsAtCarryingValue"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
    "tax": ["IncomeTaxExpenseBenefit"],
}
INSTANT = {"assets", "ca", "cl", "equity", "ltdebt", "debt", "stdebt", "cp", "cash"}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    return json.loads(data)


def day(s):
    return dt.date.fromisoformat(s)


def annual(gaap, tags, instant):
    """{fiscal_year_end: value}; the latest filing wins, so restatements are picked up."""
    merged = {}
    for t in tags:
        best = {}
        for rows in gaap.get(t, {}).get("units", {}).values():
            for x in rows:
                if x.get("form") not in ANNUAL_FORMS:
                    continue
                if not instant and ("start" not in x or
                                    not 350 <= (day(x["end"]) - day(x["start"])).days <= 380):
                    continue
                if x["end"] not in best or x["filed"] > best[x["end"]][0]:
                    best[x["end"]] = (x["filed"], x["val"])
        for end, (_, v) in best.items():
            merged.setdefault(end, v)
    return merged


def latest_filing(gaap, forms):
    rows = [x for t in TAGS["rev"] + TAGS["ni"] for u in gaap.get(t, {}).get("units", {}).values()
            for x in u if x.get("form") in forms]
    return max(rows, key=lambda x: (x["filed"], x["end"])) if rows else None


def div(a, b):
    return a / b if a is not None and b not in (None, 0) else None


def avg(a, b):
    return (a + b) / 2 if a is not None and b is not None else None


def gt(a, b):
    return a > b if a is not None and b is not None else None


def cagr(start, end, n):
    if start is None or end is None or start <= 0 or end <= 0:
        return None
    return (end / start) ** (1 / n) - 1


def fmt(v, kind):
    if v is None:
        return "n/a"
    if kind == "m":
        return f"{v / 1e6:,.0f}"
    if kind == "pct2":
        return f"{v * 100:.2f}%"
    if kind == "pct":
        return f"{v * 100:.1f}%"
    if kind in ("x", "eps"):
        return f"{v:.2f}"
    return str(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker")
    ap.add_argument("--years", type=int, default=10)
    ap.add_argument("--out")
    ap.add_argument("--json", help="also save the raw values as JSON (portable model inputs)")
    a = ap.parse_args()

    tick = a.ticker.upper().replace(".", "-")
    match = [v for v in get("https://www.sec.gov/files/company_tickers.json").values() if v["ticker"] == tick]
    if not match:
        sys.exit(f"{tick}: not an SEC registrant (non-US listing?). Use filings/web research and cite each figure.")
    cik = f"{match[0]['cik_str']:010d}"
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    facts = get(url)
    gaap = facts["facts"].get("us-gaap", {})
    if not gaap:
        sys.exit(f"{tick}: no us-gaap XBRL facts (likely an IFRS 20-F filer). Use filings/web research.")

    d = {k: annual(gaap, tags, k in INSTANT) for k, tags in TAGS.items()}
    years = sorted(set(d["rev"]) | set(d["ni"]))[-(a.years + 2):]  # 2 extra years for averages and deltas
    show = years[-a.years:]
    prev = {y: (years[i - 1] if i else None) for i, y in enumerate(years)}

    def g(k, y):
        return d[k].get(y) if y else None

    def gp(y):
        if g("gp", y) is not None:
            return g("gp", y)
        return g("rev", y) - g("cogs", y) if g("rev", y) is not None and g("cogs", y) is not None else None

    def fcf(y):
        return g("ocf", y) - g("capex", y) if g("ocf", y) is not None and g("capex", y) is not None else None

    def debt(y):  # total tag, else long-term + current portion + commercial paper
        if g("debt", y) is not None:
            return g("debt", y)
        return None if g("ltdebt", y) is None else g("ltdebt", y) + (g("stdebt", y) or 0) + (g("cp", y) or 0)

    def pa(k, y):
        return avg(g(k, y), g(k, prev.get(y)))

    def positive(v, base):  # ratio is not meaningful when its base is <= 0
        return v if base is not None and base > 0 else None

    def ic(y):  # invested capital = total debt + equity − cash
        return None if None in (debt(y), g("equity", y), g("cash", y)) else debt(y) + g("equity", y) - g("cash", y)

    def roic(y):  # NOPAT at the reported effective tax rate / avg invested capital
        pretax = g("pretax", y)
        if pretax is None and None not in (g("ni", y), g("tax", y)):
            pretax = g("ni", y) + g("tax", y)
        etr = positive(div(g("tax", y), pretax), pretax)
        base = avg(ic(y), ic(prev.get(y)))
        if etr is None or g("opinc", y) is None:
            return None
        return positive(div(g("opinc", y) * (1 - etr), base), base)

    def roa(y):  # Piotroski scales by beginning-of-year assets
        return div(g("ni", y), g("assets", prev.get(y)))

    def piotroski(y):
        p = prev.get(y)
        if not p:
            return None
        pp = prev.get(p)
        signals = [
            gt(roa(y), 0),
            gt(g("ocf", y), 0),
            gt(roa(y), roa(p)),
            gt(div(g("ocf", y), g("assets", p)), roa(y)),
            gt(div(g("ltdebt", p), pa("assets", p)), div(g("ltdebt", y), pa("assets", y))),
            gt(div(g("ca", y), g("cl", y)), div(g("ca", p), g("cl", p))),
            None if None in (g("shares", y), g("shares", p)) else g("shares", y) <= g("shares", p),
            gt(div(gp(y), g("rev", y)), div(gp(p), g("rev", p))),
            gt(div(g("rev", y), g("assets", p)), div(g("rev", p), g("assets", pp))),
        ]
        known = [s for s in signals if s is not None]
        return f"{sum(known)}/{len(known)}" if known else None

    rows = [
        ("**Income & cash flow (USD m)**", None, None),
        ("Revenue", lambda y: g("rev", y), "m"),
        ("Gross profit", gp, "m"),
        ("Operating income", lambda y: g("opinc", y), "m"),
        ("Net income", lambda y: g("ni", y), "m"),
        ("Diluted EPS (USD)", lambda y: g("eps", y), "eps"),
        ("Operating cash flow (OCF)", lambda y: g("ocf", y), "m"),
        ("Capex", lambda y: g("capex", y), "m"),
        ("FCF = OCF − capex [damodaran-2007]", fcf, "m"),
        ("Buybacks", lambda y: g("buyback", y), "m"),
        ("Dividends", lambda y: g("div", y), "m"),
        ("Diluted shares (m)", lambda y: g("shares", y), "m"),
        ("**Balance sheet (USD m)**", None, None),
        ("Total assets", lambda y: g("assets", y), "m"),
        ("Shareholders' equity", lambda y: g("equity", y), "m"),
        ("Long-term debt", lambda y: g("ltdebt", y), "m"),
        ("Total debt (incl. current)", debt, "m"),
        ("Cash & equivalents", lambda y: g("cash", y), "m"),
        ("**Profitability [nissim-penman-2001]**", None, None),
        ("Gross margin", lambda y: div(gp(y), g("rev", y)), "pct"),
        ("Operating margin", lambda y: div(g("opinc", y), g("rev", y)), "pct"),
        ("Net margin", lambda y: div(g("ni", y), g("rev", y)), "pct"),
        ("**DuPont ROE [soliman-2008]**", None, None),
        ("ROE = NI / avg equity", lambda y: positive(div(g("ni", y), pa("equity", y)), pa("equity", y)), "pct"),
        ("Asset turnover = Rev / avg assets", lambda y: div(g("rev", y), pa("assets", y)), "x"),
        ("Equity multiplier = avg assets / avg equity",
         lambda y: positive(div(pa("assets", y), pa("equity", y)), pa("equity", y)), "x"),
        ("ROIC = OpInc × (1 − ETR) / avg (debt + equity − cash)", roic, "pct2"),
        ("**Earnings quality**", None, None),
        ("OCF / NI [sloan-1996]", lambda y: positive(div(g("ocf", y), g("ni", y)), g("ni", y)), "x"),
        ("FCF / NI [sloan-1996]", lambda y: positive(div(fcf(y), g("ni", y)), g("ni", y)), "x"),
        ("Accruals = (NI − OCF) / avg assets [hribar-collins-2002]",
         lambda y: None if None in (g("ni", y), g("ocf", y)) else div(g("ni", y) - g("ocf", y), pa("assets", y)),
         "pct"),
        ("Piotroski F-score, passed/available [piotroski-2000]", piotroski, "raw"),
    ]

    k10 = latest_filing(gaap, ANNUAL_FORMS)
    q = latest_filing(gaap, ("10-Q",))
    link = lambda x: f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{x['accn'].replace('-', '')}/"
    out = [f"# {tick} ({facts.get('entityName', '')}): Financial Data from SEC EDGAR XBRL", "",
           f"- **Source** (Grade A, regulatory filings): SEC EDGAR companyfacts API, CIK {cik}, {url}",
           f"- **Retrieved**: {dt.date.today()}"]
    if k10:
        out.append(f"- **Latest annual filing**: {k10['form']}, period ending {k10['end']}, "
                   f"filed {k10['filed']}, {link(k10)}")
    if q and (not k10 or q["filed"] > k10["filed"]):
        out.append(f"- **Latest interim filing**: 10-Q, period ending {q['end']}, filed {q['filed']}, {link(q)} "
                   "(not in the table below; take quarterly figures from that filing)")
    out += ["- Columns are fiscal-year end dates. Each value comes from the latest filing, so restatements are "
            "included. Method slugs in [brackets] are defined in the skill's `methods.md`. n/a means the item "
            "is not tagged in XBRL (use the filing text or report \"not found\"), or a ratio with a "
            "denominator ≤ 0 (not meaningful).",
            "", "## Annual Figures and Ratios", "",
            "| Metric | " + " | ".join(show) + " |", "|---|" + "---|" * len(show)]
    for label, f, kind in rows:
        cells = [""] * len(show) if f is None else [fmt(f(y), kind) for y in show]
        out.append(f"| {label} | " + " | ".join(cells) + " |")

    out += ["", "## Growth (CAGR) [def-cagr]", "", "| Metric | 3Y | 5Y | 10Y |", "|---|---|---|---|"]
    last = years[-1]
    for label, f in [("Revenue", lambda y: g("rev", y)), ("Net income", lambda y: g("ni", y)),
                     ("Diluted EPS", lambda y: g("eps", y)), ("Operating cash flow", lambda y: g("ocf", y)),
                     ("FCF", fcf)]:
        cells = [fmt(cagr(f(years[-1 - n]), f(last), n), "pct") if n < len(years) else "n/a" for n in (3, 5, 10)]
        out.append(f"| {label} | " + " | ".join(cells) + " |")

    missing = [k for k in TAGS if k not in ("gp", "cogs", "debt", "stdebt", "cp") and not any(y in d[k] for y in show)]
    if missing:
        out += ["", "## Not Found in XBRL", "",
                "Get these from the filing text or report \"not found\": "
                + ", ".join(f"`{k}` ({' / '.join(TAGS[k])})" for k in missing)]

    if a.json:
        bundle = {"ticker": tick, "cik": cik, "source": url, "retrieved": str(dt.date.today()),
                  "units": "USD; ratios as decimals", "fiscal_year_ends": show,
                  "metrics": {label.strip("*"): {y: f(y) for y in show} for label, f, _ in rows if f}}
        with open(a.json, "w") as fh:
            json.dump(bundle, fh, indent=1, default=str)
        print(f"wrote {a.json}")

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
