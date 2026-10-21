---
name: stock-research
description: "Entry point for full stock investment due diligence (股票投资尽调). Chains stock-question-refiner, stock-research-executor and citation-validator into the 8-phase process: 公司事实底座、行业周期分析、业务拆解、财务质量、股权治理、市场分歧、估值护城河、综合报告. Use when the user asks to research, analyze or do due diligence on a stock, ticker or listed company."
argument-hint: "Stock ticker or company name, e.g. 600519, AAPL, 茅台"
---

# Stock Research

Target: the stock ticker or company name the user gave.

Run the full 8-phase investment due diligence by chaining these skills, in order:

1. **stock-question-refiner** - ask the clarifying questions, wait for answers, produce the structured research prompt.
2. **stock-research-executor** - execute all 8 phases (follow its `phases.md`) and write every phase file. Do not stop until `00`-`07` and `sources/bibliography.md` exist. If the output folder already has partial results, resume from them.
3. **citation-validator** - validate the finished report and fix what it flags.

Output goes to `/datadrive/scratch/stock_research/STOCK_[ticker]_[company_name]/` (never inside this repo).

The signal rating is based on fundamentals only and is not investment advice.
