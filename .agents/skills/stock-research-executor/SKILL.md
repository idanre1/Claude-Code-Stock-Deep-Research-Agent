---
name: stock-research-executor
description: 股票投资调研执行引擎，执行8阶段投资尽调流程。接收stock-question-refiner生成的结构化调研指令，部署多智能体并行研究，生成带引用的投资尽调报告。覆盖：公司事实底座、行业周期、业务拆解、财务质量、股权治理、市场分歧、估值护城河、综合报告。当用户需要进行股票投资研究、基本面分析、投资尽调时使用此技能。
---

# Stock Research Executor

Turn a structured research prompt from `stock-question-refiner` into a cited, 8-phase due diligence report. Per-agent briefs and report templates live in [phases.md](phases.md); a worked run is in [examples.md](examples.md).

## Output Layout

```
/datadrive/scratch/stock_research/STOCK_[ticker]_[company_name]/
├── 00_Executive_Summary.md    # Phase 8: signal rating, thesis, key metrics, monitoring checklist
├── 01_Business_Foundation.md  # Phase 1
├── 02_Industry_Analysis.md    # Phase 2
├── 03_Business_Breakdown.md   # Phase 3
├── 04_Financial_Quality.md    # Phase 4
├── 05_Governance_Analysis.md  # Phase 5
├── 06_Market_Sentiment.md     # Phase 6
├── 07_Valuation_Moat.md       # Phase 7
├── notes/                     # 00_baseline.md + one raw file per agent (1A.md ... 7D.md)
└── sources/bibliography.md    # All citations with A-E ratings
```

The run is complete only when `00`-`07` and `sources/bibliography.md` all exist.

## Procedure

Run end to end without stopping for plan approval. Only stop to ask the user if the ticker or company is ambiguous.

### Step 0: Resume check

List the output directory. Skip any agent whose `notes/<ID>.md` exists and any phase whose `0N_*.md` exists. Continue from the first missing piece.

### Step 1: As-of baseline (before Phase 1)

Establish and write `notes/00_baseline.md`:
- Today's date (from the environment, not from memory)
- Fiscal year end and reporting currency
- Latest annual filing (10-K / 20-F / annual report) and latest interim filing (10-Q / interim / quarterly report): period end, filing date, URL
- Next scheduled earnings date
- Current share price, shares outstanding and market cap, with the price date

Every agent uses this baseline. Data older than the latest filing must be labeled with its period.

### Step 2: Phases 1-7

For each phase, launch its 4 agents (briefs in [phases.md](phases.md)) **in parallel** as subagents, using the template below. Phases 1-6 are independent; if the host allows more parallel subagents, run two phases at once. Run Phase 7 after `04` and `06` exist; its agents read those files.

When a phase's agents finish, launch one synthesis subagent: read `notes/<N>*.md`, write `0N_*.md` using that phase's report template in [phases.md](phases.md), and return at most 5 lines. Do not read raw notes in the main session; this keeps its context small enough to finish all 8 phases.

**Agent template**:
```
You are research agent [ID] for [company] ([ticker]).

As-of baseline:
[contents of notes/00_baseline.md]

Your brief:
[the agent's section from phases.md]

User priorities: [style, horizon, risk tolerance, focus areas, specific concerns]

Rules:
- Base all figures on the latest filings in the baseline. Label anything older with its period.
- If data cannot be found, write "not found". Never estimate from memory or invent numbers.
- Cite every factual claim: [Organization, Title, Date, URL] plus an A-E grade.
- Label [FACT] vs [JUDGMENT]; give each key finding a confidence (High/Medium/Low).

Write your full findings to [output_dir]/notes/[ID].md using the brief's Output Structure,
ending with "Gaps & Contradictions" and "Sources".
Return ONLY: the file path, your 3 key findings, and the biggest gap (5 lines max).
```

### Step 3: Quality check (after Phase 7)

Confirm from the phase files, and send a fix-up agent for anything missing:
- Profit vs. cash flow cross-validation (OCF/NI, FCF/NI, 3-5 years) in `04`
- Company vs. peers comparison in `04` and `07`
- Bear case and risk scenarios in `06` and `07`
- User's priority phases covered in extra depth

### Step 4: Phase 8 synthesis

Read the Executive Summary and Key Takeaways of `01`-`07`, then write `00_Executive_Summary.md` using the Phase 8 template in [phases.md](phases.md). Merge every phase's Sources into `sources/bibliography.md` (dedupe, keep A-E grades).

### Step 5: Validate

Run the `citation-validator` skill on `00`-`07` and fix what it flags. Then list the directory to confirm the run is complete.

## Quality Standards

**Mandatory cross-validation**:
- Profit vs. cash flow: flag OCF/NI < 0.8 sustained; explain one-off items
- Company vs. peers: margins, growth, returns, multiples; explain outliers
- Bear case: 3-5 failure scenarios with likelihood, impact and trigger data

**Source quality (A-E)**:
- **A**: Regulatory filings (10-K/10-Q/20-F, annual/interim reports, prospectus), exchange announcements, audited statements, government statistics
- **B**: Earnings call transcripts, investor presentations, industry association data, reputable independent or sell-side research
- **C**: Reputable financial press (Reuters, Bloomberg, FT, WSJ, Caixin), expert commentary
- **D**: Blogs, opinion sites, data aggregators with unclear sourcing
- **E**: Social media, forums, rumors. Phase 6 sentiment only, never a factual basis

**Citation format**: `[Organization, Title, Date, URL]` plus page number for PDFs. Example:
`[Kweichow Moutai Co., Ltd., 2023 Annual Report, April 2024, https://www.cninfo.com.cn/...]`

## Rules

- No investment advice, price targets or market timing. The signal rating reflects fundamentals only.
- No hype or fear language. Present bull and bear cases with equal rigor.
- Never present opinions as facts. State uncertainty explicitly.

## Emphasis by Investment Style

| Style | Emphasize | Valuation | Red flags |
|-------|-----------|-----------|-----------|
| Value | Balance sheet, normalized earnings, margin of safety | P/B, EV/EBITDA, conservative DCF | Value traps, declining quality, accounting issues |
| Growth | TAM, competitive position, growth durability | PEG, DCF with growth scenarios, unit economics | Growth slowdown, competition, multiple compression |
| Turnaround | Liquidity, solvency, restructuring progress | Liquidation value, recovery scenarios | Insolvency, no path to viability |
| Dividend | Payout sustainability, FCF coverage | DDM, yield vs. alternatives | Payout > FCF, rising leverage |
