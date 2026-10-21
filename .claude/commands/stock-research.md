---
description: 对指定股票执行完整的投资尽调研究，从问题细化到最终报告生成。执行8阶段投资研究流程：公司事实底座、行业周期分析、业务拆解、财务质量、股权治理、市场分歧、估值护城河、综合报告。
argument-hint: [股票代码或公司名称，例如：600519, AAPL, 茅台]
allowed-tools: Task, WebSearch, WebFetch, mcp__web_reader__webReader, Read, Write, TodoWrite, Skill
---

# Stock Research

Target: $ARGUMENTS

Run the full 8-phase investment due diligence by chaining these skills, in order:

1. **stock-question-refiner** - ask the clarifying questions, wait for answers, produce the structured research prompt.
2. **stock-research-executor** - execute all 8 phases (follow its `phases.md`) and write every phase file. Do not stop until `00_Executive_Summary.md` and all `01`-`07` phase files exist.
3. **citation-validator** - validate the finished report and fix what it flags.

Output goes to `/datadrive/scratch/stock_research/STOCK_[ticker]_[company_name]/` (never inside this repo).

The signal rating is based on fundamentals only and is not investment advice.
