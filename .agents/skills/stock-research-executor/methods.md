# Calculation Methods and Research Basis

Every computed number in a report carries a method slug, e.g. `OCF/NI 1.32 [sloan-1996]`. This file maps each slug to its formula and the research behind it. All DOIs were verified against Crossref. Phase 8 copies the slugs used into `sources/bibliography.md`.

Numbers come from [scripts/fin_data.py](scripts/fin_data.py) (SEC EDGAR XBRL, US filers), [scripts/valuation.py](scripts/valuation.py) and [scripts/market_data.py](scripts/market_data.py). Do not do this arithmetic by hand. [scripts/check_report.py](scripts/check_report.py) fails the run on any slug not defined here.

## Financial quality (`fin_data.py`)

| Slug | Metric | Formula | Why it matters |
|------|--------|---------|----------------|
| `def-cagr` | CAGR | (end / start)^(1/years) − 1; n/m if start ≤ 0 | Definition |
| `nissim-penman-2001` | Margins, asset turnover, leverage, ROIC | GM = GP/Rev; OM = OpInc/Rev; NM = NI/Rev; ROIC = OpInc × (1 − tax/pretax) / avg(total debt + equity − cash), pretax = NI + tax if untagged | Ratio analysis framework linking ratios to value |
| `soliman-2008` | DuPont ROE | ROE = NI/avg Equity = NM × (Rev/avg Assets) × (avg Assets/avg Equity); n/m if avg equity ≤ 0 | Turnover changes predict future profitability; margin vs. turnover drivers differ |
| `sloan-1996` | Earnings quality | OCF/NI, FCF/NI | High-accrual earnings are less persistent and are overpriced |
| `hribar-collins-2002` | Accruals ratio | (NI − OCF) / avg total assets | The cash-flow measure of accruals avoids balance-sheet estimation errors |
| `piotroski-2000` | F-score (0-9) | 9 binary signals: ROA>0, CFO>0, ΔROA>0, CFO/A>ROA, Δleverage<0, Δcurrent ratio>0, no share issuance, Δgross margin>0, Δasset turnover>0 | Separates financially strong from weak firms among value stocks |
| `damodaran-2007` | Free cash flow | FCF = OCF − capex | Cash-flow basis of DCF valuation |

## Valuation (`valuation.py`)

| Slug | Calculation | Formula | Constraint |
|------|-------------|---------|------------|
| `sharpe-1964` | Cost of equity (CAPM) | ke = rf + β × ERP | Use the current risk-free rate; cite β and ERP sources |
| `damodaran-2007` | WACC, explicit DCF | WACC = E/(D+E)·ke + D/(D+E)·kd·(1−t); EV = Σ FCF_t/(1+r)^t + TV/(1+r)^n | Terminal g ≤ long-run nominal growth / risk-free rate |
| `gordon-1959` | Terminal value | TV = FCF_n × (1+g) / (r − g) | Requires r > g |
| `rappaport-mauboussin-2001` | Reverse DCF | Solve for the FCF growth that makes DCF value per share = price | Compare implied growth with history and consensus |

## Market context (`market_data.py`; descriptive, never part of the signal rating)

| Slug | Indicator | Formula | Evidence |
|------|-----------|---------|----------|
| `brock-1992` | 50/200-day simple moving averages | mean of last n closes | Moving-average rules carried predictive content in 1897-1986 DJIA data |
| `wilder-1978` | RSI(14), ATR(14) | Wilder smoothing; RSI = 100 − 100/(1 + avg gain/avg loss); ATR = smoothed true range | Original definitions |
| `appel-2005` | MACD (12,26,9) | EMA12 − EMA26; signal = EMA9 of MACD | Original author's definition |
| `jegadeesh-titman-1993` | 12-1 month momentum | price 21 sessions ago / price 252 sessions ago − 1 | Past 3-12 month winners keep outperforming over 3-12 months |
| `def-volatility` | Realized volatility | stdev of 30 daily log returns × √252 | Definition |

## Scoring rubrics (judgment, not statistics)

| Slug | Score | Formula | Basis |
|------|-------|---------|-------|
| `moat-rubric` | Moat score (0-5) | Σ weight × dimension score, weights from Phase 7A in [phases.md](phases.md) | Moat sources per Dorsey (2008); scores are analyst judgment backed by cited evidence |

## References

- **sloan-1996**: Sloan, R. G. (1996). Do Stock Prices Fully Reflect Information in Accruals and Cash Flows about Future Earnings? *The Accounting Review*, 71(3), 289-315. https://doi.org/10.2308/tar-9608042309 (JSTOR: https://www.jstor.org/stable/248290)
- **hribar-collins-2002**: Hribar, P., & Collins, D. W. (2002). Errors in Estimating Accruals: Implications for Empirical Research. *Journal of Accounting Research*, 40(1), 105-134. https://doi.org/10.1111/1475-679X.00041
- **piotroski-2000**: Piotroski, J. D. (2000). Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers. *Journal of Accounting Research*, 38 (Supplement), 1-41. https://doi.org/10.2307/2672906
- **nissim-penman-2001**: Nissim, D., & Penman, S. H. (2001). Ratio Analysis and Equity Valuation: From Research to Practice. *Review of Accounting Studies*, 6(1), 109-154. https://doi.org/10.1023/A:1011338221623
- **soliman-2008**: Soliman, M. T. (2008). The Use of DuPont Analysis by Market Participants. *The Accounting Review*, 83(3), 823-853. https://doi.org/10.2308/accr.2008.83.3.823
- **sharpe-1964**: Sharpe, W. F. (1964). Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk. *The Journal of Finance*, 19(3), 425-442. https://doi.org/10.1111/j.1540-6261.1964.tb02865.x
- **gordon-1959**: Gordon, M. J. (1959). Dividends, Earnings, and Stock Prices. *The Review of Economics and Statistics*, 41(2), 99-105. https://doi.org/10.2307/1927792
- **damodaran-2007**: Damodaran, A. (2007). Valuation Approaches and Metrics: A Survey of the Theory and Evidence. *Foundations and Trends in Finance*, 1(8), 693-784. https://doi.org/10.1561/0500000013
- **rappaport-mauboussin-2001**: Rappaport, A., & Mauboussin, M. J. (2001). *Expectations Investing: Reading Stock Prices for Better Returns*. Harvard Business School Press. Summary: Mauboussin, M. J. (2006), CFA Institute Conference Proceedings, https://doi.org/10.2469/cp.v23.n3.4260
- **brock-1992**: Brock, W., Lakonishok, J., & LeBaron, B. (1992). Simple Technical Trading Rules and the Stochastic Properties of Stock Returns. *The Journal of Finance*, 47(5), 1731-1764. https://doi.org/10.1111/j.1540-6261.1992.tb04681.x
- **jegadeesh-titman-1993**: Jegadeesh, N., & Titman, S. (1993). Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency. *The Journal of Finance*, 48(1), 65-91. https://doi.org/10.1111/j.1540-6261.1993.tb04702.x
- **wilder-1978**: Wilder, J. W. (1978). *New Concepts in Technical Trading Systems*. Trend Research. ISBN 978-0-89459-027-6.
- **appel-2005**: Appel, G. (2005). *Technical Analysis: Power Tools for Active Investors*. FT Press. ISBN 978-0-13-147902-9.
- **def-volatility**: Standard annualized realized volatility definition; no paper needed.
- **def-cagr**: Standard compound annual growth rate definition; no paper needed.
- **moat-rubric**: Dorsey, P. (2008). *The Little Book That Builds Wealth: The Knockout Formula for Finding Great Investments*. Wiley. ISBN 978-0-470-22651-3. Rubric weights are this skill's own convention.
