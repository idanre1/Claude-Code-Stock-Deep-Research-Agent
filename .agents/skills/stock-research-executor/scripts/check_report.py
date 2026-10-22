#!/usr/bin/env python3
"""Deterministic checks on a finished stock research directory. Run before declaring the run complete.

Usage:  check_report.py /datadrive/scratch/stock_research/STOCK_[ticker]_[company]
Exit 1 on errors (missing files, unknown method slugs, valuation runs that do not replay with the bundled
notes/valuation.py, report scripts that depend on the skill directory); budget and price issues are warnings.
"""
import importlib.util, pathlib, re, sys

SKILL = pathlib.Path(__file__).resolve().parent.parent
REQUIRED = ["00_Executive_Summary.md", "01_Business_Foundation.md", "02_Industry_Analysis.md",
            "03_Business_Breakdown.md", "04_Financial_Quality.md", "05_Governance_Analysis.md",
            "06_Market_Sentiment.md", "07_Valuation_Moat.md", "sources/bibliography.md", "notes/00_baseline.md"]
BUDGET = {"00_Executive_Summary.md": 1200}
PHASE_BUDGET = 4000
SLUG = re.compile(r"^(?:def-[a-z-]+|(?!(?:mid|early|late|end|pre|post|fy|cy)-)[a-z]+(?:-[a-z]+)*-(?:19|20)\d\d|[a-z]+-rubric)$")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = pathlib.Path(sys.argv[1])
    errors, warnings = [], []

    errors += [f"missing {f}" for f in REQUIRED if not (root / f).exists()]

    known = set(re.findall(r"^\| `([a-z0-9-]+)`", (SKILL / "methods.md").read_text(), re.M))
    used = {}
    for p in sorted(root.glob("0*.md")):
        for n, line in enumerate(p.read_text().splitlines(), 1):
            for inside in re.findall(r"\[([^\]\n]{3,120})\]", line):
                for tok in re.split(r"[;,]\s*|\s+", inside):
                    if SLUG.match(tok) and tok not in known:
                        used.setdefault(tok, f"{p.name}:{n}")
    errors += [f"unknown method slug [{s}] first used at {loc}; define it in methods.md" for s, loc in used.items()]

    runs, engine = root / "notes/valuation_runs.jsonl", root / "notes/valuation.py"
    if runs.exists():
        if engine.exists():
            spec = importlib.util.spec_from_file_location("bundled_valuation", engine)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            errors += [f"valuation replay: {b}" for b in mod.replay(runs)]
        else:
            errors.append("notes/valuation.py missing: copy scripts/valuation.py into the report so its runs replay offline")
    for p in sorted(root.rglob("*.py")) + sorted(root.rglob("*.sh")):
        if str(SKILL) in p.read_text(errors="ignore"):
            errors.append(f"{p.relative_to(root)} references {SKILL}; use the bundled notes/valuation.py via a relative path")

    for p in sorted(root.glob("0*.md")):
        words = len(p.read_text().split())
        cap = BUDGET.get(p.name, PHASE_BUDGET)
        if words > cap:
            warnings.append(f"{p.name}: {words} words > budget {cap}; move detail to notes/ or appendices")

    market = root / "notes/00_market.md"
    if market.exists():
        m = re.search(r"\*\*Price\*\*: ([\d,]+\.\d\d)", market.read_text())
        summary = root / "00_Executive_Summary.md"
        if m and summary.exists() and m.group(1) not in summary.read_text():
            warnings.append(f"00_Executive_Summary.md does not quote the snapshot price {m.group(1)} "
                            "from notes/00_market.md")
    else:
        warnings.append("notes/00_market.md missing: price has no timestamped, auditable snapshot")

    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARN:  {w}")
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
