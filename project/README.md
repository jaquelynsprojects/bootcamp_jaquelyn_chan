# Cryptocurrency Tail Risk & Quantile Connectedness
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Cryptocurrency markets are known for extreme volatility and sudden price crashes. Standard risk models only measure average relationships during calm periods, failing to capture how risk rapidly spreads across tokens during market distress. 

Replicating Bouri et al. (2021), this project builds a Quantile Vector Autoregression (Q-VAR) pipeline across 7 major cryptocurrencies (BTC, ETH, XRP, LTC, XLM, XMR, DASH). By analyzing lower ($\tau=0.10$), median ($\tau=0.50$), and upper ($\tau=0.90$) quantiles, we quantify how inter-token risk contagion escalates during market crashes.

## Stakeholder & User
- **Decision Maker**: Crypto Fund Risk Manager (decides exposure limits and hedging strategies).
- **End User**: Quantitative Risk Analysts & Traders (monitor daily risk contagion metrics).
- **Timing & Context**: Daily risk surveillance and emergency stress hedging.

## Useful Answer & Decision
- **Answer Type**: Descriptive & Diagnostic (tail-risk network mapping).
- **Core Metrics**:
  - Total Spillover Index (TSI): System-wide risk connectedness across quantiles.
  - Net Directional Spillover (NSI = TO - FROM): Identifies net risk transmitters vs. receivers.
  - Relative Tail Dependence (RTD): Measures asymmetry between market crashes and booms.
- **Deliverables**: Python data/modeling pipeline and an interactive risk dashboard.

## Assumptions & Constraints
- **Data**: Daily price data (2015–2026) fetched via free public APIs (`yfinance`).
- **Trading Hours**: 24/7 continuous trading; verified stationary log returns.
- **Zero ML**: Pure statistical time-series models (Q-VAR) for full regulatory transparency.
- **Performance**: Pipeline executes within 60 seconds.

## Known Unknowns / Risks
- **Market Regime Shifts**: Crash events (e.g., FTX collapse) may alter spillover patterns.
  - *Mitigation*: Use 200-day rolling windows to track dynamic parameter changes.
- **High Correlation**: Extreme market stress can cause collinearity in lag variables.
  - *Mitigation*: Select optimal lag length using AIC.

## Lifecycle Mapping
Goal → Stage → Deliverable
- Project Definition → Stage 01 (Framing & Scoping) → Scoping README & Stakeholder Memo
- Data Pipeline → Stage 02 (Data Ingestion) → Cleaned Return Series Database & Loader
- Quantile-VAR Engine → Stage 03 (Modeling) → Q-VAR Variance Decomposition & Metrics
- Risk Visualization → Stage 04 (Productization) → Streamlit Dashboard & Spillover Plots

## Repo Plan
- `project/data/`: Raw and processed crypto price data.
- `project/src/`: Core Python modules (`data_loader.py`, `qvar.py`, `metrics.py`).
- `project/notebooks/`: EDA and replication experiments.
- `project/docs/`: Stakeholder memos and project specs.
- **Cadence**: Weekly milestones following course stages.