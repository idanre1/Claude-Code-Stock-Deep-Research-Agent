# Stock Question Refiner - Examples

This document provides detailed examples of how the Stock Question Refiner skill works in practice.

## Table of Contents

1. [Example 1: Value Investing - A-share Blue Chip](#example-1-value-investing)
2. [Example 2: Incomplete Information - How to Follow Up](#example-2-incomplete-information---how-to-follow-up)

---

## Example 1: Value Investing - A-share Blue Chip

### User's Initial Request

```
User: 我想知道贵州茅台 600519 值不值得投资
```

### Question Refiner's Response

```
我可以帮您对贵州茅台进行投资研究，但我不能直接告诉您"值不值得买"或给
出投资建议。不过，我可以帮您系统性地研究这家公司，帮您做出自己的判断。

为了给您提供最合适的研究，我需要了解一些信息：

**1. 您的投资风格是什么？**
   A. 价值投资 - 寻找被低估的优质资产，关注安全边际
   B. 成长投资 - 关注高成长性，愿意为成长付出溢价
   C. 红利投资 - 关注稳定分红和现金流
   D. 其他

**2. 您的持有周期？**
   A. 短期（6个月以内）
   B. 中期（6-18个月）
   C. 长期（1-3年以上）

**3. 您最关心哪些方面？（选2-3个）**
   - 生意质量：护城河、定价权、商业模式
   - 财务质量：现金流、盈利质量
   - 行业态势：行业周期、竞争格局
   - 公司治理：管理层、资本配置
   - 估值：是否便宜、安全边际
   - 催化剂：近期催化因素

**4. 您的风险偏好？**
   - 保守：避免高负债、风险资产
   - 平衡：可接受适度风险
   - 激进：可承受高波动

请告诉我您的选择，我会据此生成针对性的研究计划。
```

### User's Response

```
User:
1. 价值投资，关注安全边际
2. 长期持有，3年以上
3. 最关心：生意质量、公司治理、估值
4. 风险偏好：保守
```

### Generated Structured Research Prompt

```markdown
### Investment Research Target

**Stock Ticker**: 600519.SH
**Company Name**: 贵州茅台股份有限公司 (Kweichow Moutai Co., Ltd.)
**Market**: A-share (Shanghai Stock Exchange)
**Industry/Sector**: Consumer Staples - Baijiu (White Spirits)

### Investment Parameters

**Investment Style**: Value Investing (深度价值)
- Philosophy: Buy high-quality assets at discounts to intrinsic value
- Focus: Business quality, competitive moat, margin of safety
- Implications: Prioritize durable competitive advantages, normalized earnings power,
  asset quality, conservative valuation

**Holding Period**: Long-term (3+ years)
- Time horizon: Multi-year ownership, compounding focus
- Research implications: Emphasize business sustainability, moat durability,
  long-term competitive position over short-term noise

**Risk Tolerance**: Conservative
- Risk constraints:
  - Avoid companies with high debt or financial leverage
  - Require proven business model with long operating history
  - Demand strong cash generation and balance sheet
  - No accounting or governance red flags

### Research Scope

**Must Cover** (All 8 Phases):
1. ✅ Business Foundation (facts, products, revenue structure)
2. ✅ Industry Analysis (baijiu industry cycle, competition, premiumization trends)
3. ✅ Business Breakdown (profit drivers, pricing power, moat)
4. ✅ Financial Quality (cash flow vs. earnings, capital efficiency)
5. ✅ Governance Analysis (state-owned enterprise, management track record)
6. ✅ Market Sentiment (bull/bear cases on luxury baijiu demand)
7. ✅ Valuation & Moat (brand moat assessment, historical and relative valuation)
8. ✅ Final Synthesis (signal rating, investment thesis, monitoring checklist)

**Deep Dive Priority** (User's Top Focus Areas):
- Priority 1: **Business Quality & Moat**
  - Brand strength and pricing power
  - Competitive advantages vs. Wuliangye, Yanghe, and other premium baijiu
  - Moat durability (threats from changing consumer preferences, counterfeit products)
  - Economic moat rating (0-5 scale) with evidence

- Priority 2: **Governance & Capital Allocation**
  - SOE governance structure and incentives
  - Capital allocation history (dividends, capex, M&A)
  - Management quality and track record
  - Shareholder return policies

- Priority 3: **Valuation & Margin of Safety**
  - Intrinsic value assessment using multiple methods (DCF, PE relative to history,
    peer comparison, sum-of-parts)
  - Historical valuation range analysis (5-10 years)
  - Current valuation vs. intrinsic value discount/premium
  - Margin of safety assessment

**Can Streamline** (Quick Pass):
- Phase 6: Market Sentiment (less critical for long-term value investor,
  focus on fundamentals over sentiment)

### Output Requirements

**Format**:
- [x] Executive Summary with signal light rating
  - 🟢🟢🟢 Strong Buy (significant margin of safety, strong moat)
  - 🟡🟡🟡 Hold (fairly valued or limited margin of safety)
  - 🔴🔴 Avoid (overvalued or deteriorating fundamentals)

- [x] 8-Phase detailed reports (one file per phase)
  - Language: Bilingual (Chinese primary, English key terms)
  - Structure: Executive summary + detailed analysis + key takeaways

- [x] Key financial data tables
  - 5-10 year history: Revenue, net income, operating cash flow, free cash flow
  - Margins: Gross margin, operating margin, net margin, FCF margin
  - Growth rates: Revenue CAGR, net income CAGR (3-year, 5-year, 10-year)
  - Efficiency: ROE, ROIC, asset turnover, cash conversion cycle
  - Balance sheet: Debt ratios, cash position, working capital trends

- [x] Valuation dashboard
  - Historical multiples: PE (TTM, forward), PB, PS, EV/EBITDA, FCF yield
  - Historical percentiles (5-year, 10-year)
  - Peer comparison: Wuliangye, Yanghe, Fenjiu, international luxury peers (LVMH,
    Kering)
  - DCF valuation with conservative assumptions
  - Reverse DCF: What growth is implied by current price?

- [x] Monitoring checklist
  - Conditions to strengthen thesis (e.g., maintains premium pricing, growth
    stabilizes, dividend increases)
  - Exit triggers (e.g., moat erosion, volume declines, margin compression,
    governance issues)

- [x] Bibliography with source quality ratings
  - A: Annual reports, regulatory filings, peer-reviewed research
  - B: Industry reports, reputable analyst research
  - C: Company presentations, management commentary
  - D: News articles, secondary sources
  - E: Social media, forums (verify with primary sources)

**Valuation Methods Required**:
- [x] Relative valuation (PE, PB, PS, EV/EBITDA)
  - Historical percentile analysis (5-year, 10-year)
  - Peer comparison (Wuliangye 000858.SZ, Yanghe 002304.SZ, Fenjiu 600809.SH)
  - International luxury goods comparison (LVMH, Kering, Hermes)

- [x] DCF valuation (essential for long-term value investor)
  - Base case, bull case, bear case scenarios
  - Conservative assumptions: WACC, terminal growth rate (2-3%)
  - Sensitivity analysis (WACC × growth rate)

- [x] Sum-of-the-parts (if applicable)
  - Moutai core business vs. series (飞天茅台 vs. 系列酒)
  - Wholesale vs. direct-to-consumer channels

- [x] Reverse DCF
  - What long-term growth rate is implied by current stock price?
  - Is this growth rate achievable or overly optimistic?

**Special Requirements**:
- **Data timeframe**: 5-10 years historical data for valuation context
- **Geography focus**: China domestic market, but benchmark against global luxury peers
- **Language**: Chinese primary, with English financial terms and ratios
- **Include charts/visualizations descriptions**: Yes (describe key charts that would
  help understanding)
- **Emphasis on**:
  - Cash flow quality over reported earnings
  - Sustainable competitive advantages (moat)
  - Conservative intrinsic value estimation
  - Margin of safety assessment

### Research Constraints

**Data Sources** (Priority Order):
1. Most authoritative:
   - Annual reports (年报)
   - IPO prospectus and offering documents
   - Regulatory filings (CSRC, Shanghai Stock Exchange)
   - Company announcements (定期报告、临时公告)

2. High quality:
   - Earnings call transcripts (业绩说明会纪要)
   - Investor relations presentations
   - Industry association reports (China Alcoholic Drinks Association)

3. Supplementary:
   - Brokerage research (use with skepticism, check conflicts of interest)
   - Industry reports (Jiémian, Wall Street CN, Bloomberg)
   - Academic research on baijiu industry

4. Market sentiment (for Phase 6 only):
   - News coverage (Caixin, FT, Bloomberg)
   - Social media (雪球, East Money - verify claims)

**Mandatory Verification**:
- ✅ Profit vs. cash flow cross-validation
  - Operating cash flow / Net income (historical 5-year trend)
  - Free cash flow / Net income
  - Accruals analysis (change in working capital)

- ✅ Company vs. peer comparison
  - Valuation multiples vs. Wuliangye, Yanghe, Fenjiu
  - Margin comparison (gross, operating, net)
  - Growth rates comparison
  - ROE and ROIC comparison

- ✅ Bear case analysis (identify risks and failure scenarios)
  - Premiumization trend reversal
  - Regulatory risks (anti-corruption, pricing restrictions)
  - Competition from premium foreign spirits
  - Counterfeit products and brand dilution
  - Volume growth slowdown (demographic headwinds)

- ✅ Source quality rating
  - All factual claims must cite sources with A-E rating
  - Distinguish between company disclosures and third-party analysis

**What NOT to Do**:
- ❌ Do NOT predict stock price or target price
- ❌ Do NOT give buy/sell/hold recommendations (only provide signal light rating
  based on fundamentals)
- ❌ Do NOT time market entry/exit points
- ❌ Do NOT guarantee investment outcomes or returns
- ❌ Do NOT provide trading strategies or technical analysis
- ❌ Do NOT make assumptions about Chinese government policy changes

### Final Instructions

**Output Directory**: `/datadrive/scratch/stock_research/STOCK_600519_Kweichow_Moutai/`

**File Structure**:
```
/datadrive/scratch/stock_research/STOCK_600519_Kweichow_Moutai/
├── 00_Executive_Summary.md
│   - Signal light rating with rationale
│   - One-paragraph investment thesis
│   - Key metrics summary table
│   - Margin of safety assessment
│   - Top 3 reasons to buy/avoid
├── 01_Business_Foundation.md
│   - Company overview
│   - Product portfolio (飞天茅台, 系列酒)
│   - Revenue and profit structure
│   - Channel structure (直销 vs. 经销)
│   - Strategic initiatives (i茅台APP, direct-to-consumer)
├── 02_Industry_Analysis.md
│   - Baijiu industry overview
│   - Premiumization trend
│   - Competitive landscape (tier 1 vs. tier 2 baijiu)
│   - Industry cycle position
│   - Key risks (regulation, demographics, competition)
├── 03_Business_Breakdown.md
│   - One-sentence business essence (品牌护城河 + 定价权 + 稀缺性)
│   - Business segment analysis
│   - Profit engine analysis
│   - Pricing power and volume dynamics
│   - Customer analysis (gift-giving, business entertainment, personal consumption)
├── 04_Financial_Quality.md
│   - 5-10 year financial trends
│   - Profitability trends (margins, ROE, ROIC)
│   - Cash flow quality analysis (OCF/NI, FCF/NI)
│   - Balance sheet strength (debt, cash, working capital)
│   - Red flag check (accruals, related party transactions, accounting quality)
├── 05_Governance_Analysis.md
│   - Ownership structure (SOE, state ownership)
│   - Management team and track record
│   - Capital allocation history (dividends, capex)
│   - Executive compensation and incentives
│   - Related party transactions and governance risks
├── 06_Market_Sentiment.md
│   - Bull case (premiumization, pricing power, scarcity value)
│   - Bear case (volume saturation, regulation, competition)
│   - Key debates and what data will resolve them
├── 07_Valuation_Moat.md
│   - Moat assessment (brand, network effects, cost advantage, regulatory)
│   - Moat rating (0-5) with evidence table
│   - Historical valuation analysis (multiples, percentiles)
│   - Peer comparison table
│   - DCF valuation with scenarios
│   - Reverse DCF implied growth
│   - Margin of safety assessment
├── notes/
└── sources/bibliography.md
```

**Quality Standards**:
- Every factual claim includes: Author/Org, Date, Title, URL/DOI, Page (if applicable)
- Clear distinction between [公司披露] [行业数据] [分析师观点] [市场传闻]
- All judgments supported by evidence or logical reasoning
- Use Chain-of-Verification for controversial claims
- Identify contradictions between sources explicitly
- Flag areas of uncertainty or insufficient data

**Reminders for Value Investing Approach**:
- Be conservative in assumptions (better to miss an opportunity than overpay)
- Focus on what can be known (facts), not what must be assumed (speculation)
- Demand margin of safety (price should be significantly below intrinsic value)
- Assess business quality first, then valuation (don't buy a bad business just because it's cheap)
- Think like an owner (would you buy this entire company?)
- Ignore short-term price volatility and focus on business fundamentals
- Assess moat durability (can this business maintain advantages for 10+ years?)

**Important Disclaimer**:
> 本研究报告仅供教育和信息用途，不构成投资建议或推荐。所有投资均有风险，包括本金损失。过往表现不代表未来结果。请自行进行尽职调查，并在做出投资决策前咨询合格的财务顾问。
>
> This research is for educational and informational purposes only and does not constitute investment advice. All investments involve risk. Past performance does not guarantee future results. Always conduct your own due diligence and consult with qualified financial advisors.

---

Begin the investment research on Kweichow Moutai (600519.SH) following the 8-phase due diligence framework tailored for conservative value investing.
```

---

## Example 2: Incomplete Information - How to Follow Up

### User's Initial Request

```
User: Research Tesla TSLA
```

### Question Refiner's Response

```
I'd be happy to help you research Tesla (TSLA). To create a tailored investment
research plan, I need to understand your context:

**1. What's your investment approach for Tesla?**
   Are you viewing Tesla as:
   A. A growth stock (EV revolution, autonomous driving potential)
   B. A mature auto manufacturer (focus on profitability and margins)
   C. A technology company (software, FSD, robotics)
   D. Not sure yet

**2. How long do you plan to hold?**
   A. Short-term (<1 year)
   B. Medium-term (1-3 years)
   C. Long-term (3+ years)
   D. Not sure

**3. What aspects are most important to you?**
   - EV market share and competitive position
   - Autonomous driving (FSD) progress
   - Financials and profitability
   - Elon Musk and management
   - Valuation (is it overvalued?)
   - Energy storage and solar business
   - Other

**4. Risk tolerance?**
   A. Conservative (avoid high volatility)
   B. Balanced
   C. Aggressive (comfortable with high volatility and binary outcomes)

Please share your preferences so I can tailor the research accordingly. Even if
you're not sure about some questions, telling me what you DO know will help.
```

### If User Says "I don't know / I'm new to investing"

```
No problem! Let me help you figure this out.

**To determine your investment style, think about**:

1. **What's more important to you?**
   - Buying companies growing fast, even if expensive (Growth)
   - Buying undervalued companies (Value)
   - Receiving regular dividend income (Income)

2. **How would you react if Tesla stock dropped 30%?**
   - Panic and sell (suggests conservative approach, Tesla may not be suitable)
   - Hold if fundamentals are strong (balanced)
   - Buy more if the story is intact (aggressive)

3. **What are you hoping for?**
   - Quick gains (short-term trading - this research framework is not ideal)
   - Long-term wealth creation (buy and hold for 5+ years)

**Based on Tesla specifically**:
- Tesla is a **high-volatility, high-growth stock** best suited for:
  - Growth investors
  - Long-term holders (3-5+ years)
  - Aggressive risk tolerance

- If you're conservative or have low risk tolerance, Tesla may not be suitable.

Would you like me to generate a **balanced research prompt** that covers all bases,
or would you prefer to think about your investment approach first and then come back?
```

---

## Summary of Key Examples

| Investment Style | Key Emphasis | Valuation Methods | Risk Considerations |
|-----------------|--------------|-------------------|---------------------|
| **Value** | Intrinsic value, margin of safety, moat | P/B, EV/EBITDA, DCF (conservative) | Overpaying, value traps, moat erosion |
| **Growth** | TAM, competitive positioning, growth sustainability | PEG, DCF (aggressive), user value | Valuation compression, growth slowdown, competition |
| **Turnaround** | Liquidity, solvency, restructuring, catalysts | Liquidation value, option value, recovery scenarios | Total loss, binary outcome, timeline uncertainty |
| **Dividend** | Yield sustainability, payout ratio, FCF generation | DDM, yield vs. alternatives, FCF coverage | Dividend cuts, payout ratio too high, regulatory risks |

---

## Notes

- All examples maintain the principle of **NOT providing investment advice**
- Each example emphasizes **different aspects** based on investment style
- **Risk tolerance** is always incorporated into constraints and warnings
- **Time horizon** affects which phases are prioritized
- **User's stated concerns** are always addressed specifically in the research prompt
- **Disclaimers** are always included to remind users this is research assistance, not financial advice
