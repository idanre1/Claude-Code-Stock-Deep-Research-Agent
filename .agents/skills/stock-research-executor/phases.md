# Stock Research Executor - Phase-by-Phase Instructions

This document provides detailed instructions for each of the 8 phases of investment due diligence, including specific research objectives, agent deployment strategies, and output templates.

## Phase 1: Business Foundation (公司事实底座)

### Objective

Establish a factual understanding of what the company does, how it makes money, and its position in the industry value chain.

### Research Goals

1. Understand the core business model and product/service offerings
2. Identify revenue and profit sources by segment
3. Analyze customer base and use cases
4. Determine position in industry value chain
5. Track recent strategic changes (3-5 years)

### Multi-Agent Deployment Strategy

Deploy **4 agents in parallel**:

#### Agent 1A: Core Business and Products

**Objective**: Map the company's business model and product/service portfolio

**Key Questions**:
- What products/services does the company offer?
- What are the main business segments?
- How does each segment make money?
- What's the revenue mix by segment?

**Data to Find**:
- Product/service descriptions
- Business segment breakdown (with revenue percentages)
- Main revenue drivers for each segment
- Product/service生命周期 (growth, mature, declining)

**Sources to Prioritize**:
- Annual reports (business overview section)
- Company website and investor presentations
- Segment reporting in financial statements

**Output Structure**:
```markdown
## Core Business and Products

**Business Model**: [1-2 sentence description]

**Product/Service Portfolio**:
| Segment | Description | Revenue | % of Total | Growth Trend |
|---------|-------------|---------|------------|--------------|
| [Segment 1] | [description] | [amount] | [%] | [trend] |
| [Segment 2] | [description] | [amount] | [%] | [trend] |

**Key Insights**:
- [Insight 1]
- [Insight 2]
```

---

#### Agent 1B: Revenue and Profit Composition

**Objective**: Understand how the company generates revenue and profit

**Key Questions**:
- What are the main revenue streams?
- Which segments/products are most profitable?
- How has revenue mix changed over time?
- Are there any high-revenue but low-profit segments?

**Data to Find**:
- Revenue breakdown by segment/product/geography
- Gross margin by segment
- Operating profit by segment
- 3-5 year trend analysis

**Sources to Prioritize**:
- Annual reports (segment reporting)
- Financial statement notes
- Management commentary (earnings calls)

**Output Structure**:
```markdown
## Revenue and Profit Composition

**Revenue Mix** (Most Recent Year):
| Source | Revenue | % of Total | YoY Growth |
|--------|---------|------------|------------|
| [Source 1] | [amount] | [%] | [%] |
| [Source 2] | [amount] | [%] | [%] |

**Profit Contribution**:
| Segment | Gross Margin | Operating Margin | Profit % |
|---------|--------------|------------------|----------|
| [Segment 1] | [%] | [%] | [%] |
| [Segment 2] | [%] | [%] | [%] |

**Key Insights**:
- Most profitable segment: [name] with [margin]%
- [Any mismatches: high revenue but low profit, or vice versa]
```

---

#### Agent 1C: Customers and Value Chain Position

**Objective**: Identify who the company sells to and where it sits in the value chain

**Key Questions**:
- Who are the main customers (industries, demographics, geographies)?
- Is the customer base concentrated or diversified?
- What's the company's position in the value chain (upstream, midstream, downstream)?
- Does it have pricing power or is it a price taker?

**Data to Find**:
- Customer segments (B2B vs B2C, industries, geographies)
- Top customers (if disclosed)
- Distribution channels (direct, indirect, online, offline)
- Value chain position and bargaining power

**Sources to Prioritize**:
- Annual reports (customer and market sections)
- Industry reports
- Company investor presentations

**Output Structure**:
```markdown
## Customers and Value Chain Position

**Customer Segments**:
| Segment | Description | Revenue % | Growth |
|---------|-------------|-----------|--------|
| [Segment 1] | [description] | [%] | [trend] |
| [Segment 2] | [description] | [%] | [trend] |

**Customer Concentration**:
- Top 5/10 customers: [X]% of revenue (if disclosed)
- Concentration risk: [High/Medium/Low]

**Value Chain Position**:
- Position: [upstream/midstream/downstream/integrated]
- Bargaining power: [strong/moderate/weak]
- Reason: [explanation]

**Distribution Channels**:
- Direct: [%] - [description]
- Indirect/distributors: [%] - [description]
- Online/digital: [%] - [description]
```

---

#### Agent 1D: Recent Strategic Changes (3-5 Years)

**Objective**: Track significant strategic shifts, pivots, or transformations

**Key Questions**:
- What major strategic initiatives has the company undertaken?
- Have there been business model changes?
- Any M&A, divestitures, or restructurings?
- Technology investments or digital transformation?
- Market expansion or contraction?

**Data to Find**:
- Major acquisitions or divestitures
- New product launches or discontinuations
- Market entry/exit decisions
- Strategic partnerships or JVs
- Organizational restructuring

**Sources to Prioritize**:
- Annual reports (MD&A section, past 3-5 years)
- Press releases and announcements
- News archives for major events

**Output Structure**:
```markdown
## Recent Strategic Changes (Past 3-5 Years)

**Timeline of Major Events**:
| Year | Event | Impact | Status |
|------|-------|--------|--------|
| [Year] | [event] | [impact] | [ongoing/completed/failed] |
| [Year] | [event] | [impact] | [status] |

**Strategic Initiatives**:
1. **[Initiative 1]**: [description]
   - Launched: [year]
   - Investment: [amount if known]
   - Results to date: [description]

2. **[Initiative 2]**: [description]
   - ...

**Overall Assessment**:
- Strategy is [consistent/evolving/unclear]
- Success rate: [high/mixed/low]
```

---

### Phase 1 Synthesis and Report Generation

After all 4 agents complete:

1. **Compile findings** into coherent narrative
2. **Create summary table** of key business facts
3. **Identify any contradictions** between sources
4. **Generate Phase 1 report**: `01_Business_Foundation.md`

**Report Template**:
```markdown
# Phase 1: Business Foundation

## Executive Summary
[2-3 paragraph overview]

## 1.1 Core Business and Products
[Content from Agent 1A]

## 1.2 Revenue and Profit Composition
[Content from Agent 1B]

## 1.3 Customers and Value Chain Position
[Content from Agent 1C]

## 1.4 Recent Strategic Changes
[Content from Agent 1D]

## Key Takeaways
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

## Red Flags Identified
- [Any concerning findings]
- [Areas requiring further investigation]

## Sources
[List all sources with A-E ratings]
```

---

## Phase 2: Industry Analysis (行业周期分析)

### Objective

Assess industry dynamics, competitive landscape, and where the industry sits in the business cycle.

### Research Goals

1. Determine industry cycle stage (recovery/expansion/recession/contraction)
2. Analyze supply-demand dynamics
3. Assess competitive landscape and concentration
4. Identify key industry drivers and trends
5. Evaluate policy and external factors

### Multi-Agent Deployment Strategy

Deploy **4 agents in parallel**:

#### Agent 2A: Industry Cycle Stage

**Objective**: Determine where the industry is in the business cycle

**Key Questions**:
- Is the industry in recovery, expansion, recession, or contraction?
- What's the evidence (capacity utilization, inventory levels, pricing)?
- How long has the current cycle phase lasted?
- What typically triggers cycle inflection points?

**Data to Find**:
- Industry production/output trends
- Capacity utilization rates
- Inventory levels (raw materials, work-in-progress, finished goods)
- Pricing trends (inflation/deflation)
- CapEx trends (expansion or contraction)

**Sources to Prioritize**:
- Industry association reports
- Government statistics (bureau of statistics, industry ministry)
- Research reports (McKinsey, BCG, Bain - verify with primary sources)
- Company management commentary

**Output Structure**:
```markdown
## Industry Cycle Stage Assessment

**Current Stage**: [Recovery/Expansion/Recession/Contraction]

**Evidence**:
| Indicator | Current Level | Trend | Implication |
|-----------|--------------|-------|-------------|
| Capacity Utilization | [%] | [rising/stable/falling] | [implication] |
| Inventory Levels | [high/normal/low] | [trend] | [implication] |
| Pricing | [inflation/stable/deflation] | [trend] | [implication] |
| CapEx | [expansion/maintenance] | [trend] | [implication] |

**Cycle Duration**:
- Current phase started: [year/quarter]
- Typical cycle length: [X] years
- Time until next inflection: [estimate if possible]

**Leading Indicators** (1-2 year forward-looking):
1. [Indicator 1]: [what it signals]
2. [Indicator 2]: [what it signals]

**Lagging Indicators** (confirms what already happened):
1. [Indicator 1]: [what it confirms]
2. [Indicator 2]: [what it confirms]
```

---

#### Agent 2B: Supply-Demand Dynamics

**Objective**: Analyze supply and demand fundamentals

**Key Questions**:
- What's driving demand? (secular trends, cyclical factors, policy)
- What's the supply situation? (capacity, new entrants, constraints)
- Is the market in balance, oversupply, or shortage?
- What's the medium-term outlook (1-3 years)?

**Data to Find**:
- Demand drivers and trends
- Supply capacity and utilization
- Import/export dynamics
- New capacity announcements
- Order backlogs or delivery times

**Sources to Prioritize**:
- Industry reports
- Company disclosures (if industry participant)
- Trade publications
- Government trade data

**Output Structure**:
```markdown
## Supply-Demand Analysis

**Demand Drivers**:
| Driver | Type | Strength | Trend |
|--------|------|----------|-------|
| [Driver 1] | [secular/cyclical/policy] | [strong/moderate/weak] | [growing/stable/declining] |
| [Driver 2] | [type] | [strength] | [trend] |

**Supply Situation**:
- Current capacity: [amount]
- Capacity utilization: [%]
- New capacity coming online: [amount] by [year]
- Supply constraints: [any limitations]

**Market Balance**:
- Current: [surplus/balance/shortage]
- Gap: [amount if quantified]
- 12-24 month outlook: [improving/deteriorating/stable]

**Key Risks to Supply-Demand Balance**:
- Risk 1: [description]
- Risk 2: [description]
```

---

#### Agent 2C: Competitive Landscape and Concentration

**Objective**: Map the competitive environment

**Key Questions**:
- Who are the main competitors?
- What's the market structure (fragmented, oligopoly, monopoly)?
- What are the market shares (CR5, HHI if available)?
- How intense is competition? (price wars, innovation, differentiation)
- What are the barriers to entry/exit?
- **Value-chain profit capture**: map the chain (inputs → company → customers → end users). Where is the binding constraint (bottleneck)? Pricing power sits there. Does the company *capture* the industry's growth (margin and ROIC rising) or only *transit* it (revenue up, margins flat or falling, with value passed to suppliers or customers)?
- Classify the company as **value captor** (growth + margin expansion), **volume taker** (growth, flat margin), **optionality** (exposure not yet in earnings) or **cost bearer** (its input costs rise with the trend). Revenue growth alone is not benefit.

**Data to Find**:
- Major competitors and market shares
- Margin and ROIC trend of the company vs. its key suppliers and customers (who is gaining share of the profit pool?)
- Industry concentration (CR5, CR10)
- Competitive dynamics (price competition, innovation, consolidation)
- Recent M&A activity
- Barriers to entry (regulatory, capital, technology, brand)

**Sources to Prioritize**:
- Industry reports
- Company annual reports (competitive landscape sections)
- Antitrust/regulatory filings
- News archives for M&A

**Output Structure**:
```markdown
## Competitive Landscape

**Market Structure**: [Fragmented/Oligopoly/Dominant player/Monopoly]

**Major Competitors**:
| Rank | Company | Market Share | Key Strengths |
|------|---------|--------------|---------------|
| 1 | [Company] | [%] | [strengths] |
| 2 | [Company] | [%] | [strengths] |
| 3 | [Company] | [%] | [strengths] |

**Industry Concentration**:
- CR5 (top 5 share): [X]%
- Concentration level: [high/medium/low]
- Trend: [consolidating/stable/fragmenting]

**Competitive Dynamics**:
- Primary basis of competition: [price/quality/innovation/service/brand]
- Intensity: [fierce/moderate/limited]
- Recent M&A: [description of consolidation trends]

**Barriers to Entry**:
| Barrier Type | Level | Description |
|--------------|-------|-------------|
| Capital | [high/medium/low] | [description] |
| Regulatory | [high/medium/low] | [description] |
| Technology | [high/medium/low] | [description] |
| Brand/Network | [high/medium/low] | [description] |

**Barriers to Exit**:
- Sunk costs: [high/medium/low]
- Regulatory constraints: [yes/no]
- Union/employment issues: [yes/no]
```

---

#### Agent 2D: Policy and External Variables

**Objective**: Identify key external factors affecting the industry

**Key Questions**:
- What government policies impact this industry? (subsidies, taxes, regulations)
- What macroeconomic factors matter? (interest rates, exchange rates, inflation)
- What technological disruptions are looming?
- What social or demographic trends are relevant?
- What geopolitical risks exist?

**Data to Find**:
- Relevant regulations and policy changes
- Government support or restrictions
- Macro sensitivity (interest rate, currency, commodity exposure)
- Technology disruptions
- ESG and social trends

**Sources to Prioritize**:
- Government websites and policy documents
- Regulatory filings
- Industry association policy comments
- News for recent policy changes

**Output Structure**:
```markdown
## Policy and External Variables

**Government Policies**:
| Policy | Impact | Direction | Timeline |
|--------|--------|----------|----------|
| [Policy 1] | [positive/negative/neutral] | [tightening/loosing/stable] | [immediate/gradual] |
| [Policy 2] | [impact] | [direction] | [timeline] |

**Macroeconomic Sensitivities**:
| Factor | Sensitivity | Current Trend | Impact |
|--------|-------------|---------------|--------|
| Interest Rates | [high/medium/low] | [rising/stable/falling] | [impact description] |
| Exchange Rates | [high/medium/low] | [trend] | [impact] |
| Inflation | [high/medium/low] | [trend] | [impact] |
| [Commodity] | [high/medium/low] | [trend] | [impact] |

**Technological Disruptions**:
- Disruption 1: [description] - [timing] - [impact level]
- Disruption 2: [description] - [timing] - [impact level]

**ESG/Social Trends**:
- Trend 1: [description] - [impact]
- Trend 2: [description] - [impact]

**Geopolitical Risks**:
- Risk 1: [description] - [probability] - [potential impact]
- Risk 2: [description] - [probability] - [potential impact]

**Structural vs. Cyclical Factors**:
- Structural (long-term): [factors]
- Cyclical (short-term): [factors]
```

---

### Phase 2 Synthesis

**Report Template**: `02_Industry_Analysis.md`

Include:
- Industry cycle stage with evidence
- Supply-demand outlook
- Competitive positioning map
- External risk assessment
- Investment implications based on industry cycle

---

## Phase 3: Business Breakdown (业务拆解)

### Objective

Understand the economics of how the company makes money at a granular level.

### Multi-Agent Deployment Strategy

Deploy **4 agents in parallel**:

#### Agent 3A: Business Segment Deep Dive

**Objective**: Detailed financial analysis of each business segment

**Key Questions**:
- What's the revenue and profit contribution of each segment?
- Which segments are growing vs. declining?
- Which segments have the best margins?
- Are there cross-subsidies (profitable segments funding unprofitable ones)?

**Data to Find**:
- Segment revenue, margins, growth (5-year history)
- Segment capital allocation (capex by segment)
- Intersegment transactions and transfer pricing
- Segment ROIC

**Output Structure**:
```markdown
## Business Segment Analysis

**Segment Financials** (Most Recent Year):
| Segment | Revenue | Growth | Gross Margin | Op Margin | ROIC |
|---------|---------|--------|--------------|-----------|------|
| [Seg 1] | [amount] | [%] | [%] | [%] | [%] |
| [Seg 2] | [amount] | [%] | [%] | [%] | [%] |

**5-Year Growth Trends**:
| Segment | CAGR | Trend | Driver |
|---------|------|-------|--------|
| [Seg 1] | [%] | [accelerating/stable/decelerating] | [driver] |
| [Seg 2] | [%] | [trend] | [driver] |

**Key Insights**:
- Core profit driver: [segment]
- Hidden gems: [segments with high potential but overlooked]
- Drag on performance: [segments losing money or growing slowly]
```

---

#### Agent 3B: Profit Engine and Economics

**Objective**: Understand the unit economics and profit drivers

**Key Questions**:
- How does the company make money on a per-unit basis?
- What are the key cost components?
- Are there economies of scale?
- What's the incremental margin on new business?
- Does the earnings evidence confirm the value-chain role assigned in Phase 2 (captor / volume taker / optionality / cost bearer)? Look for backlog, book-to-bill, price/mix vs. volume split, guidance raises and management Q&A admissions. If the evidence contradicts Phase 2, say so.

**Data to Find**:
- Unit economics (if disclosed)
- Revenue growth split into price, mix and volume
- Cost structure (fixed vs. variable)
- Operating leverage
- Gross margin trends and drivers

**Output Structure**:
```markdown
## Profit Engine Analysis

**One-Sentence Business Essence**:
[Company makes money by: [what it sells] → [to whom] → [why they can charge a premium / have cost advantage]]

**Cost Structure**:
| Cost Category | % of Revenue | Type | Trend |
|---------------|--------------|------|-------|
| [COGS component 1] | [%] | [fixed/variable] | [trend] |
| [COGS component 2] | [%] | [fixed/variable] | [trend] |
| SG&A | [%] | [mostly fixed/mixed] | [trend] |
| R&D | [%] | [mostly fixed/discretionary] | [trend] |

**Economies of Scale**:
- Scale advantages: [yes/no/partial]
- Evidence: [what shows scale benefits]
- Incremental margin on new revenue: [X]%

**Pricing Power**:
- Ability to raise prices: [strong/moderate/weak/none]
- Evidence: [historical price increases, margin stability]
- Customer price sensitivity: [high/medium/low]
```

---

#### Agent 3C: Customer and Pricing Analysis

**Objective**: Understand customer economics and pricing power

**Key Questions**:
- Who are the core customers and how valuable are they?
- How sticky are customers? (churn, switching costs)
- Does the company have pricing power?
- How are prices determined? (market-driven, cost-plus, value-based)

**Data to Find**:
- Customer retention/churn rates
- Customer acquisition vs. retention cost
- Historical pricing changes
- Customer concentration (top 5/10 customers)
- Contract structure (recurring vs. one-off)

**Output Structure**:
```markdown
## Customer and Pricing Analysis

**Customer Base**:
- Total customers: [number if disclosed]
- Customer segments: [B2B/B2C mix]
- Customer concentration: Top 5 = [X]%, Top 10 = [X]%
- Churn rate: [X]% (if disclosed)

**Customer Stickiness**:
| Factor | Level | Evidence |
|--------|-------|----------|
| Switching Costs | [high/medium/low] | [evidence] |
| Contract Length | [long/medium/short] | [evidence] |
| Renewal Rate | [%] | [source] |
| Customer Satisfaction | [high/medium/low] | [evidence] |

**Pricing Power Assessment**:
- Historical price changes: [list significant price increases/decreases]
- Price vs. competitors: [premium/parity/discount]
- Margin stability: [stable/volatile - indicates pricing power]
- Customer pushback: [high/medium/low resistance to price hikes]

**Pricing Strategy**:
- Approach: [market-driven/cost-plus/value-based/dynamic]
- Flexibility: [high/medium/low]
- Price competition intensity: [fierce/moderate/limited]
```

---

#### Agent 3D: Subsidiaries and Non-Core Items

**Objective**: Analyze non-core businesses, investments, and one-time items

**Key Questions**:
- What subsidiaries or investments does the company have?
- What's the contribution from non-operating items? (investment income, asset sales, government subsidies)
- Are there hidden assets or liabilities?
- What non-core activities could be divested?

**Data to Find**:
- List of major subsidiaries and associates
- Investment income and gains
- Asset sales and one-time gains
- Government subsidies and grants
- Non-operating items in P&L

**Output Structure**:
```markdown
## Subsidiaries and Non-Core Items

**Major Subsidiaries/Associates**:
| Entity | Business | Ownership | Contribution | Strategy |
|--------|----------|-----------|--------------|----------|
| [Sub 1] | [description] | [%] | [profit/loss] | [core/strategic/non-core] |
| [Sub 2] | [description] | [%] | [profit/loss] | [core/strategic/non-core] |

**Non-Operating Income** (Recent Year):
| Source | Amount | % of Net Income | Sustainability |
|--------|--------|-----------------|----------------|
| Investment Income | [amount] | [%] | [recurring/one-time] |
| Asset Sales | [amount] | [%] | [recurring/one-time] |
| Government Subsidies | [amount] | [%] | [recurring/declining/one-time] |
| [Other] | [amount] | [%] | [sustainability] |

**Hidden Assets**:
- Asset 1: [description] - [estimated value if available]
- Asset 2: [description] - [estimated value if available]

**Hidden Liabilities/Risks**:
- Risk 1: [description]
- Risk 2: [description]

**Core vs. Non-Core Assessment**:
- True core business profits: [amount] (excluding non-core)
- Non-core contribution to net income: [X]%
- Assessment: [core business strong/weak/non-core is critical/distraction]
```

---

### Phase 3 Synthesis

**Report Template**: `03_Business_Breakdown.md`

Include:
- One-sentence business essence
- Segment profitability matrix
- Customer economics summary
- Assessment of sustainable vs. non-sustainable profits

---

## Phase 4: Financial Quality (财务质量)

### Objective

Assess the quality of earnings, financial health, and sustainability of the business model.

### Multi-Agent Deployment Strategy

Deploy **4 agents in parallel**:

#### Agent 4A: Key Metrics and Trend Analysis

**Objective**: Calculate and analyze key financial metrics over 5-10 years

**Start from `notes/00_financials.md`** (SEC XBRL data produced by `scripts/fin_data.py`; US filers only). Use its numbers and method slugs as they are. Search the web only for items it marks n/a, for non-US companies, and for ROIC. Any additional arithmetic runs in code, never by hand.

**Key Questions**:
- What are the growth rates (revenue, net income, CAGR)?
- What's the profitability (margins, ROE, ROIC)?
- How have metrics trended over time?
- Are there any inflection points or concerning trends?

**Data to Find**:
- 5-10 year history of: revenue, net income, operating income, gross margin, net margin, ROE, ROIC
- Calculate CAGR (3-year, 5-year, 10-year if available)
- Volatility of metrics

**Output Structure**:
```markdown
## Key Financial Metrics (5-10 Year History)

**Growth Metrics**:
| Metric | 3Y CAGR | 5Y CAGR | 10Y CAGR | Trend |
|--------|---------|---------|----------|-------|
| Revenue | [%] | [%] | [%] | [accelerating/stable/decelerating] |
| Net Income | [%] | [%] | [%] | [trend] |
| Operating Income | [%] | [%] | [%] | [trend] |

**Profitability Metrics**:
| Metric | Latest | 5Y Avg | 10Y Avg | Trend |
|--------|--------|--------|---------|-------|
| Gross Margin | [%] | [%] | [%] | [improving/stable/declining] |
| Operating Margin | [%] | [%] | [%] | [trend] |
| Net Margin | [%] | [%] | [%] | [trend] |
| ROE | [%] | [%] | [%] | [trend] |
| ROIC | [%] | [%] | [%] | [trend] |

**DuPont Analysis (ROE Decomposition)**:
- ROE = Net Margin × Asset Turnover × Financial Leverage
- Net Margin: [%] - [trend]
- Asset Turnover: [X] - [trend]
- Financial Leverage: [X] - [trend]
- Driver of ROE changes: [which component]

**Key Inflection Points**:
- [Year]: [event/trend change] - [impact]
```

---

#### Agent 4B: Cash Flow Quality

**Objective**: Assess earnings quality through cash flow analysis

Use OCF/NI and FCF/NI `[sloan-1996]`, the accruals ratio `[hribar-collins-2002]` and the Piotroski F-score `[piotroski-2000]` from `notes/00_financials.md`. Explain *why* they moved (working capital, capex cycle, stock-based compensation, one-offs), with filing citations.

**Key Questions**:
- Do earnings convert to cash? (OCF/NI, FCF/NI)
- Are there red flags in cash flow? (consistent shortfall, working capital drag)
- What's the free cash flow generation?
- How is cash being used? (capex, dividends, buybacks, debt repayment)

**Data to Find**:
- Operating cash flow (OCF), free cash flow (FCF) for 5-10 years
- OCF/Net Income ratio
- FCF/Net Income ratio
- Cash flow from operations vs. net income reconciliation
- Use of cash (capex, dividends, buybacks, M&A, debt)

**Output Structure**:
```markdown
## Cash Flow Quality Analysis

**Cash Flow vs. Earnings**:
| Year | Net Income | OCF | OCF/NI | FCF | FCF/NI |
|------|-----------|-----|--------|-----|--------|
| [Year] | [amount] | [amount] | [ratio] | [amount] | [ratio] |
| [Year] | [amount] | [amount] | [ratio] | [amount] | [ratio] |

**Assessment**:
- Average OCF/NI (5-year): [ratio]
  - [Excellent if > 1.0, Good if 0.8-1.0, Concerning if < 0.8, Red flag if < 0.5]
- Average FCF/NI (5-year): [ratio]
- Trend: [improving/stable/deteriorating]

**Red Flags**:
- [ ] Persistent OCF < Net Income (low quality earnings)
- [ ] Declining OCF/NI ratio (deteriorating quality)
- [ ] Large working capital swings (volatile cash conversion)
- [ ] High capex eating into cash flow (low FCF)

**Free Cash Flow Uses** (5-Year Total):
| Use | Amount | % of FCF |
|-----|--------|----------|
| Capex (maintenance) | [amount] | [%] |
| Capex (growth) | [amount] | [%] |
| Dividends | [amount] | [%] |
| Buybacks | [amount] | [%] |
| M&A | [amount] | [%] |
| Debt Repayment | [amount] | [%] |

**FCF Generation Capacity**:
- [Strong/Adequate/Weak]
- Sustainable dividend/buyback capacity: [yes/no/partially]
```

---

#### Agent 4C: Anomaly Screening (Red Flags)

**Objective**: Identify financial irregularities or accounting concerns

**Key Questions**:
- Are there any unusual items in the financials?
- Are receivables or inventory growing faster than sales?
- Are there frequent one-time items or accounting changes?
- Any related party transactions or off-balance sheet items?
- Any audit concerns or going doubt issues?

**Data to Find**:
- Receivables growth vs. revenue growth
- Inventory growth vs. revenue growth
- Non-recurring items (frequency, magnitude)
- Accounting changes or restatements
- Related party transactions
- Audit opinion (unqualified, qualified, going concern)
- Off-balance sheet items

**Output Structure**:
```markdown
## Financial Anomaly Screening

**Working Capital Trends**:
| Item | Growth (3Y) | Revenue Growth (3Y) | Delta | Assessment |
|------|------------|---------------------|-------|------------|
| Receivables | [%] | [%] | [%] | [OK/concerning] |
| Inventory | [%] | [%] | [%] | [OK/concerning] |
| Payables | [%] | [%] | [%] | [OK/concerning] |

**Red Flag Indicators**:
| Indicator | Status | Evidence | Concern Level |
|-----------|--------|----------|---------------|
| Receivables growing faster than sales | [yes/no] | [data] | [high/medium/low/n/a] |
| Inventory buildup | [yes/no] | [data] | [level] |
| Rising days sales outstanding (DSO) | [yes/no] | [data] | [level] |
| Frequent one-time items | [yes/no] | [list] | [level] |
| Accounting changes | [yes/no] | [description] | [level] |
| Related party transactions | [yes/no] | [description] | [level] |
| Audit concerns | [yes/no] | [description] | [level] |

**Accruals Analysis** (Balance Sheet Accruals):
- Accruals = (ΔCurrent Assets - ΔCash) - (ΔCurrent Liabilities - ΔShort-term Debt)
- High accruals may indicate low earnings quality

**Non-Recurring Items** (Past 3-5 Years):
| Year | Item | Amount | Impact on NI | Type |
|------|------|--------|--------------|------|
| [Year] | [item] | [amount] | [%] | [gain/charge/restructuring] |

**Overall Assessment**:
- Financial quality: [Excellent/Good/Fair/Poor]
- Red flags: [number] significant, [number] minor
- Key concern: [biggest red flag if any]
```

---

#### Agent 4D: Peer Comparison

**Objective**: Benchmark financial metrics against competitors

**Key Questions**:
- How does the company compare to peers on key metrics?
- Is it above or below average?
- Are there any significant outliers?
- What explains the differences?

**Data to Find**:
- Peer list (3-5 main competitors)
- Key metrics comparison: growth, margins, ROE, valuation multiples
- Differences in business models that explain metric differences

**Output Structure**:
```markdown
## Peer Comparison

**Peer Group**:
[Company] vs. [Peer 1], [Peer 2], [Peer 3]

**Metric Comparison** (Most Recent Year):
| Metric | [Company] | Peer Avg | Best Peer | Worst Peer | Rank |
|--------|-----------|----------|-----------|------------|------|
| Revenue Growth | [%] | [%] | [%] | [%] | [X/5] |
| Gross Margin | [%] | [%] | [%] | [%] | [X/5] |
| Operating Margin | [%] | [%] | [%] | [%] | [X/5] |
| Net Margin | [%] | [%] | [%] | [%] | [X/5] |
| ROE | [%] | [%] | [%] | [%] | [X/5] |
| ROIC | [%] | [%] | [%] | [%] | [X/5] |

**Outliers** (Significant deviations):
- [Metric]: [Company] is [better/worse] than peers by [X]pp
  - Explanation: [business model, strategy, or other factor]
- [Metric]: [Company] is [better/worse] than peers by [X]pp
  - Explanation: [reason]

**Competitive Positioning**:
- Overall financial quality: [above/at/below] peer average
- Strengths vs. peers: [list]
- Weaknesses vs. peers: [list]
```

---

### Phase 4 Synthesis

**Report Template**: `04_Financial_Quality.md`

Include:
- Financial health score (Excellent/Good/Fair/Poor)
- Cash flow quality assessment
- Red flag summary
- Peer ranking table

---

## Phase 5: Governance Analysis (股权与治理)

### Objective

Decide whether management and controlling shareholders are partners or extractors of minority shareholders. Good business + bad governance = high-volatility risk asset.

### Multi-Agent Deployment Strategy

Deploy **4 agents in parallel**:

#### Agent 5A: Ownership Structure and Related Parties

**Objective**: Map who controls the company and where minority shareholders can be hurt

**Key Questions**:
- Who is the controlling shareholder / actual controller? Dual-class or voting agreements?
- Board composition: independence, tenure, overlap with controller?
- Share pledges (ratio and trend), announced sell-down plans, control-change risk?
- Related-party transactions, competing businesses held by the controller, fund occupation?

**Data to Find**:
- Top 10 shareholders and insider ownership (latest filing), changes over 3 years
- Voting vs. economic ownership
- Pledge ratio (A-share/HK), insider sale plans (US: Form 4, 10b5-1)
- Related-party transaction amounts vs. revenue/profit

**Output Structure**:
```markdown
## Ownership Structure and Related Parties

**Control Map** (text diagram): [controller] → [holding entity] → [company], voting % vs. economic %

**Top Shareholders**:
| Holder | % Shares | % Votes | 3Y Change | Type |
|--------|----------|---------|-----------|------|

**Governance Risk Radar**:
| Risk | Level (H/M/L) | Evidence |
|------|---------------|----------|
| Control concentration | | |
| Share pledges / insider selling | | |
| Related-party transactions | | |
| Competing businesses / fund occupation | | |
| Board independence | | |

**Announcements to Track**: [list]
```

---

#### Agent 5B: Management Quality and Incentives

**Objective**: Test whether management's incentives and track record align with long-term shareholders

**Key Questions**:
- What are the compensation and equity-incentive KPIs (revenue / profit / cash flow / ROIC / TSR)?
- Are the KPIs easy to game (e.g., revenue or adjusted EPS instead of cash flow or ROIC)?
- How hard are the targets vs. history and peers?
- Do incentives reward short-term behavior (pushing revenue, cutting R&D)?
- Say-do consistency: did management hit its own guidance over the last 3-5 years?

**Data to Find**:
- Proxy statement / remuneration report: pay mix, KPIs, thresholds
- Stock-based compensation as % of revenue and of FCF; share-count trend
- Past guidance vs. actual results (each year)
- Insider buying vs. selling (24 months)

**Output Structure**:
```markdown
## Management Quality and Incentives

**Incentive KPIs**:
| KPI | Weight | Target | Gameable? | Assessment |
|-----|--------|--------|-----------|------------|

**Key Clause Excerpts**: [quoted, with citation]

**Guidance Track Record**:
| Year | Guided | Actual | Hit/Miss |
|------|--------|--------|----------|

**SBC and Dilution**: SBC [x]% of revenue, [x]% of FCF; diluted shares [trend] over 5Y

**Alignment Verdict**: [Aligned / Partly aligned / Misaligned] - [evidence]
```

---

#### Agent 5C: Capital Allocation Track Record

**Objective**: Judge where the money management earned actually went and what it returned

**Key Questions**:
- Over 5-10 years, how was cash deployed (capex, M&A, buybacks, dividends, debt paydown)?
- Did acquisitions create value or end in impairments/write-downs?
- Is ROIC above the cost of capital, and is it trending up or down?
- Were buybacks done at sensible prices, or did they only offset dilution?
- Did recent equity raises, buybacks or deals add to or dilute EPS?

**Data to Find**:
- Cumulative cash deployment by use (5-10Y)
- Major acquisitions: price, rationale, later impairments
- ROIC by year (state formula), WACC estimate
- Buyback volume and average price vs. share price range

**Output Structure**:
```markdown
## Capital Allocation Track Record

**Cash Deployment** (5-10Y cumulative):
| Use | Amount | % of Total |
|-----|--------|------------|

**ROIC vs. WACC**:
| Year | ROIC | WACC | Spread |
|------|------|------|--------|

**Major Deals**:
| Year | Deal | Price | Outcome (impairments, returns) |
|------|------|-------|--------------------------------|

**Capital Allocation Grade**: [A-F] - [rationale]
```

---

#### Agent 5D: Share Overhang and Event Calendar (筹码事件时间表)

**Objective**: Build a 12-month calendar of events that change share supply

**Key Questions**:
- Upcoming lock-up expiries, employee share unlocks, secondary offerings, rights issues, convertible conversions?
- Buyback program size, remaining authorization and execution pace?
- Planned insider or major-holder sales?
- For each event: potential selling pressure vs. absorption capacity, path to valuation impact, historical price reaction to similar events (if found)?

**Output Structure**:
```markdown
## Share Overhang and Event Calendar (next 12 months)

| Date | Event | Shares / Amount | % of Float | Selling Pressure vs. Absorption | Past Similar Reaction |
|------|-------|-----------------|-----------|----------------------------------|-----------------------|

**Net Assessment**: [overhang / neutral / supportive] - [reason]
```

---

### Phase 5 Synthesis

**Report Template**: `05_Governance_Analysis.md`

Include:
- Governance structure (text diagram) and risk radar
- Management alignment verdict with key clause excerpts
- Capital allocation grade with ROIC table
- 12-month share event calendar
- Announcements to track

---

## Phase 6: Market Sentiment (市场分歧)

### Objective

Lay out what bulls and bears are actually arguing about, and which future data will settle it. The value is not picking a side but knowing what to watch.

**Rules for all Phase 6 agents**: Do not take sides. No investment advice. No emotional or partisan language. Every judgment must be verifiable by future data or events.

### Multi-Agent Deployment Strategy

Deploy **5 agents in parallel** (6E is descriptive market context):

#### Agent 6A: Bull Case

**Objective**: Steelman the strongest bull thesis

**Key Questions**:
- What are the 3-5 core bull arguments, and who makes them (analysts, funds, management)?
- What is the strongest evidence for each?
- What must be true for the bull case to play out?

**Output Structure**:
```markdown
## Bull Case

| # | Argument | Key Evidence | Source | What Must Be True |
|---|----------|--------------|--------|-------------------|
```

---

#### Agent 6B: Bear Case

**Objective**: Steelman the strongest bear thesis, actively searching for disconfirming evidence

**Key Questions**:
- What are the 3-5 core bear arguments, and who makes them?
- Are there short-seller reports, regulatory probes, litigation, downgrades, accounting questions or negative press?
- What is the strongest evidence for each?
- What must be true for the bear case to play out?

**Output Structure**:
```markdown
## Bear Case

| # | Argument | Key Evidence | Source | What Must Be True |
|---|----------|--------------|--------|-------------------|

**Short Reports / Probes / Litigation**: [list with dates and status, or "none found"]
```

---

#### Agent 6C: Key Debates and Consensus

**Objective**: Identify where bulls and bears disagree and what the market consensus expects

**Key Questions**:
- What are the 3-5 points of disagreement?
- What does sell-side consensus expect (revenue/EPS next 2 years, rating distribution)?
- How have estimates been revised over the last 3-6 months?
- Which disagreements can be resolved by future data?

**Output Structure**:
```markdown
## Key Debates and Consensus

**Consensus**: Revenue FY+1 [x], FY+2 [x]; EPS FY+1 [x], FY+2 [x]; ratings [buy/hold/sell counts]; revisions [up/down/flat]

| Debate | Bull View | Bear View | Evidence Each Side | Resolvable by Data? |
|--------|-----------|-----------|--------------------|---------------------|
```

---

#### Agent 6D: Verification Nodes

**Objective**: Build a dated calendar of the events and data that will resolve the debates

**Key Questions**:
- What upcoming earnings, product launches, regulatory decisions, industry data releases or contract renewals matter?
- For each, what metric and threshold would confirm the bull view vs. the bear view?

**Output Structure**:
```markdown
## Verification Nodes

| Date / Window | Event | Metric to Watch | Bull Confirmed If | Bear Confirmed If |
|---------------|-------|-----------------|-------------------|-------------------|
```

---

#### Agent 6E: Market Context (descriptive, never part of the signal)

**Objective**: Describe how the market is positioned, without forecasting price

**Inputs**: `notes/00_market.md` (price snapshot and technicals from `scripts/market_data.py`; reuse its numbers and slugs, do not recompute)

**Key Questions**:
- Trend and momentum: price vs. SMA50/200, RSI, 12-1 momentum, 12-month return vs. benchmark?
- Ownership: largest institutional holders and recent changes (SEC 13F filings or the exchange equivalent), with filing dates?
- Short interest and days to cover (FINRA or exchange data), with settlement date?
- Macro and catalyst calendar for the next 6 months (central bank meetings, index events, sector data)?
- Options: implied volatility and skew only if an options chain was actually retrieved; otherwise write "not retrieved"

**Output Structure**:
```markdown
## Market Context (descriptive; excluded from the signal rating)

| Item | Value | As of | Source / Slug |
|------|-------|-------|---------------|

**Positioning read**: [2-3 sentences, no price forecast]
```

---

### Phase 6 Synthesis

**Report Template**: `06_Market_Sentiment.md`

Include:
- Bull vs. bear comparison table
- Consensus snapshot and revision trend
- Debates that future data can settle
- Verification node calendar
- Market Context appendix from 6E, labeled "descriptive; excluded from the signal rating"

---

## Phase 7: Valuation & Moat (估值与护城河)

### Objective

Rate the durability of competitive advantages with evidence, and determine what assumptions the current price is betting on. Agents 7B-7D read `04_Financial_Quality.md` and `06_Market_Sentiment.md` first and reuse their numbers.

### Multi-Agent Deployment Strategy

Deploy **4 agents in parallel**:

#### Agent 7A: Competitive Moat Assessment

**Objective**: Score the moat with verifiable evidence from company disclosures or authoritative sources

**Key Questions**:
1. **Pricing power**: 5-10 year gross margin, price-increase history, ability to pass on cost inflation?
2. **Switching costs**: What does a customer lose by switching (systems, processes, compliance, ecosystem)?
3. **Network / scale effects**: How does scale lower unit cost or improve the product?
4. **Intangibles**: Verifiable brand, patents, licenses, data or channel barriers?
5. **Competitive response**: How have rivals attacked, and how did the company defend (historical battles)?

**Scoring rubric** (each dimension 0-5, weighted):
| Dimension | Weight | Evidence Standard |
|-----------|--------|-------------------|
| Pricing power | 25% | Gross margin stability, price-increase history |
| Switching costs | 20% | Retention/churn, system dependence |
| Network effects | 20% | Value rising with user base |
| Scale advantages | 15% | Unit-cost advantage vs. peers |
| Intangible assets | 20% | Brand, patents, licenses, data |

Weighted total: 0-2 no moat, 2-4 narrow moat, 4-5 wide moat. Tag the score `[moat-rubric]`.

**Output Structure**:
```markdown
## Competitive Moat Assessment

| Dimension | Score (0-5) | Weight | Evidence | Source |
|-----------|-------------|--------|----------|--------|

**Weighted Moat Score**: [x.x]/5 - [No / Narrow / Wide]

**Historical Competitive Battles**: [attack → defense → outcome]

**Most Likely Erosion Point**: [what] - Monitoring metric: [metric, threshold]
```

---

#### Agent 7B: Relative Valuation

**Objective**: Place the current valuation in historical and peer context

**Key Questions**:
- Current P/E, P/B, P/S, EV/EBITDA, FCF yield (state price date from the baseline)?
- Where does each sit in its 5-10 year historical range (percentile)?
- Premium or discount to peers, and is it justified by growth, margins or returns?

**Output Structure**:
```markdown
## Relative Valuation (price as of [date])

| Multiple | Current | 5-10Y Low | Median | High | Percentile |
|----------|---------|-----------|--------|------|------------|

| Multiple | Company | Peer 1 | Peer 2 | Peer 3 | Peer Median | Premium/Discount |
|----------|---------|--------|--------|--------|-------------|------------------|

**Assessment**: [cheap / fair / expensive vs. history and peers] - [is the premium/discount justified?]
```

---

#### Agent 7C: Absolute Valuation (DCF and Reverse DCF)

**Objective**: Build a transparent DCF and reverse it to find what the price implies. Produce a valuation range, not a price target.

**All valuation arithmetic runs through `scripts/valuation.py`** (`wacc`, `dcf` for bear/base/bull, `reverse`). Cite a dated source for every input: risk-free rate from the U.S. Treasury yield curve (or the home-country government bond), cost of debt from the company's most recent bond issue or filing, beta, ERP, net debt and shares from `notes/00_financials.md`. Add `--save [output_dir]/notes/valuation_runs.jsonl` to every run so the model can be re-run, and paste the script output with its method slugs into the notes.

**Funding bridge (required when FCF is negative or capex is rising)**: before the DCF, build a yearly table from filings and guidance, then feed the resulting signed FCF straight into `dcf --fcf-path=...` (negative years allowed; the final year must be positive). Do not normalize a negative base into a positive one.

| Year | OCF | Gross capex | Customer advances / prepayments | New lease commitments | Interest paid | Debt raised (repaid) | Equity issued / dilution | FCF to firm |
|------|-----|-------------|---------------------------------|-----------------------|---------------|----------------------|--------------------------|-------------|

**Key Questions**:
- Discount rate: risk-free rate, equity risk premium, beta, cost of debt, with dated sources?
- How is the build-out funded year by year, and how much dilution or new debt does that imply per share?
- 5-10 year FCF projection: revenue growth, margin, reinvestment rate, each tied to Phase 3-4 evidence?
- Terminal growth and its justification?
- Sensitivity: discount rate × terminal growth (or × margin)?
- Reverse DCF: what revenue growth and margin path does the current market cap imply? Is that realistic vs. history and consensus?
- Which 2 assumptions are most likely wrong, and how can they be verified?

**Output Structure**:
```markdown
## Absolute Valuation

**Key Assumptions**:
| Assumption | Bear | Base | Bull | Basis / Source |
|------------|------|------|------|----------------|

**Funding Bridge**: [table above, or "not needed: FCF positive and capex stable"]

**Intrinsic Value per Share**: Bear [x] / Base [x] / Bull [x] vs. current price [x] ([date])

**Sensitivity** (value per share):
| WACC \ g | [g1] | [g2] | [g3] |
|----------|------|------|------|

**Reverse DCF**: Current price implies [x]% revenue CAGR and [x]% FCF margin for [n] years - vs. 5Y history [x]% and consensus [x]%

**Most Fragile Assumptions**:
1. [assumption] - how to verify: [data / event]
2. [assumption] - how to verify: [data / event]
```

---

#### Agent 7D: Risk Scenarios and Black Swans

**Objective**: Quantify downside scenarios and define exit triggers

**Key Questions**:
- What does the bear scenario do to earnings and valuation (quantified)?
- Black swans: regulation, technology disruption, geopolitics, key-customer loss, accounting?
- Probability and impact of each?
- What observable thresholds would invalidate the thesis?

**Output Structure**:
```markdown
## Risk Scenarios

| Risk | Probability (H/M/L) | Impact (H/M/L) | Effect on Earnings / Value | Early Warning Signal |
|------|---------------------|----------------|----------------------------|----------------------|

**Black Swans**: [list with mechanism]

**Thesis-Breaking Triggers** (exit):
- [ ] [metric] falls below/above [threshold]
- [ ] [event] happens
```

---

### Phase 7 Synthesis

**Report Template**: `07_Valuation_Moat.md`

Include:
- Moat score table and erosion point
- Relative valuation dashboard (historical percentile + peers)
- DCF range, sensitivity, reverse DCF implied expectations
- Risk matrix and thesis-breaking triggers

---

## Phase 8: Final Synthesis

### Objective

Combine all findings into a comprehensive investment due diligence report.

### Tasks

1. Read the Executive Summary and Key Takeaways of `01`-`07`
2. Write `00_Executive_Summary.md` using the template below (key metrics table, monitoring checklist and risks live here)
3. Merge every phase's Sources section into `sources/bibliography.md`, deduplicated, with A-E grades. Add a "Methods" section listing the full reference from [methods.md](methods.md) for every method slug used in the report

### Executive Summary Structure

At most 1,200 words. Link to phase files for detail instead of repeating it. Quote the price and quote time from `notes/00_market.md`.

```markdown
# Executive Summary

## Signal Rating

🟢🟢🟢 **Strong Buy** / 🟡🟡🟡 **Hold** / 🔴🔴 **Avoid**   |   **Data confidence**: High / Medium / Low

**Rationale**: [2-3 sentences]. The signal scores the business and price; data confidence scores how well the evidence supports it. Keep them separate.

**Why this rating given the valuation**: [Reconcile the signal with the DCF range and reverse DCF. If the price sits outside the bear-base range, say explicitly why the rating is still Hold/Buy/Avoid.]

## Investment Thesis

**One-Liner**: [single sentence]

**Three drivers that decide the outcome**:
1. **[Driver]**: [evidence, metric now, what would change it]
2. **[Driver]**: ...
3. **[Driver]**: ...

## Key Metrics

| Metric | Value | Context |
|--------|-------|---------|
| Price / Market Cap | [x] at [quote time, exchange] | |
| TTM Revenue / growth | | |
| TTM Net Income / margin | | |
| OCF/NI, FCF | | [profit vs. cash] |
| ROIC | | [vs. WACC] |
| P/E, EV/EBITDA | | [percentile vs. history, vs. peers] |
| DCF bear / base / bull | | [implied growth from reverse DCF] |
| Moat | [0-5] | [width, erosion point] |

## Bull vs. Bear

| Top 3 reasons to consider | Top 3 reasons to avoid |
|---------------------------|------------------------|
| 1. [one sentence + evidence] | 1. [one sentence + evidence] |

## Decisive Dates

| Date / Window | Event | What it settles |
|---------------|-------|-----------------|

## Monitoring State

| Metric | Source | Next Date | Threshold (strengthen / exit) | Rationale | Current | Status |
|--------|--------|-----------|-------------------------------|-----------|---------|--------|

Status = pass / fail / not testable yet.

## Conclusion

[2-3 sentences]

---

**Data As Of**: [latest filing period] / price [x] at [quote time] | **Sources**: [n] | **Phases**: 8/8

**Disclaimer**: This research is for educational and informational purposes only and does not constitute investment advice. All investments involve risk. Past performance does not guarantee future results. Always conduct your own due diligence and consult with qualified financial advisors.
```

### Special Scenarios

#### Scenario 1: Distressed Company (e.g., bankruptcy risk)

**Adjustments**:
- Emphasize Phases 4 (solvency) and 7 (liquidation value)
- Add: "Going Concern vs. Liquidation" analysis
- Valuation: Focus on recovery scenarios, probability-weighted expected value
- Risk analysis: Emphasize binary outcomes and timing risks

#### Scenario 2: High-Growth Company (unprofitable)

**Adjustments**:
- Phase 4: Focus on cash burn rate, runway, path to profitability
- Valuation: Use user value models, TAM penetration, growth-over-earnings
- Skip: Traditional P/E, DCF (if no current cash flow)
- Add: Growth sustainability assessment, competitive moat durability

#### Scenario 3: Newly Public (IPO)

**Adjustments**:
- Phase 1: Emphasize IPO prospectus analysis
- Phase 4: Limited historical data (use prospectus financials)
- Phase 5: Check for lock-up expirations, insider selling plans
- Valuation: Difficult (no trading history), focus on prospectus guidance

#### Scenario 4: Foreign Company (e.g., Chinese A-share)

**Adjustments**:
- Data sources: Emphasize local language sources (Chinese for A-shares)
- Translation: Provide bilingual or clarify if using English sources
- Regulatory: Include country-specific regulatory risks
- Accounting: Note if using IFRS, GAAP, or local standards (CAS for China)

### Search Troubleshooting

#### Issue: Cannot Find Information

**Solution**:
1. Try alternative search queries
2. Search in different languages (if foreign company)
3. Look in regulatory filings instead of news
4. Acknowledge limitation explicitly in report
5. Flag for user to investigate further

#### Issue: Web Search Returns Poor Results

**Solution**:
1. Use more specific, targeted queries
2. Add site: filters (e.g., "site:sec.gov", "site:cninfo.com.cn")
3. Use file type filters (e.g., "filetype:pdf annual report")
4. Try alternative search terms
5. Check if company has changed names or tickers

---

For execution examples demonstrating these phases, see [examples.md](examples.md).
