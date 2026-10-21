# Calculation Methods and Research Basis

Every computed number in a report carries a method slug, e.g. `OCF/NI 1.32 [sloan-1996]`. This file maps each slug to its formula and the research behind it. All DOIs were verified against Crossref. Phase 8 copies the slugs used into `sources/bibliography.md`.

Numbers come from [scripts/fin_data.py](scripts/fin_data.py) (SEC EDGAR XBRL, US filers) and [scripts/valuation.py](scripts/valuation.py). Do not do this arithmetic by hand.

## Financial quality (`fin_data.py`)

| Slug | Metric | Formula | Why it matters |
|------|--------|---------|----------------|
| `def-cagr` | CAGR | (end / start)^(1/years) − 1; n/m if start ≤ 0 | Definition |
| `nissim-penman-2001` | Margins, asset turnover, leverage | GM = GP/Rev; OM = OpInc/Rev; NM = NI/Rev | Ratio analysis framework linking ratios to value |
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
- **def-cagr**: Standard compound annual growth rate definition; no paper needed.
