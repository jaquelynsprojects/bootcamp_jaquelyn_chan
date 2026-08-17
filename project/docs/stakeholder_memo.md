# Stakeholder Context Memo: Cryptocurrency Tail Risk & Contagion Surveillance

**To:** Crypto Asset Investment Committee & Risk Management Group  
**From:** Quantitative Risk Analytics Team  
**Date:** Fall 2026  
**Subject:** System Framing for Quantile-Based Risk Spillover & Network Connectedness  

---

### 1. Executive Summary & Core Objective
Standard risk management tools relying on mean-based Vector Autoregression (VAR) fail to capture the severity of cross-token contagion during market crashes. In crypto markets, systemic connectedness surges from ~58% in normal conditions to over 75% during extreme tail events. Replicating the empirical methodology of Bouri, Saeed, Vo, & Roubaud (2021), this project develops an automated **Quantile-VAR (Q-VAR) Risk Surveillance System** to provide institutional decision-makers with early-warning metrics on tail-risk propagation.

---

### 2. Stakeholder Persona & Key Pain Points

* **Persona**: Senior Quantitative Risk Officer (Marcus)
  * **Role**: Manages multi-token digital asset risk exposure, tail-risk hedging, and margin requirements.
  * **Pain Points**: 
    - Standard portfolio diversification collapses during black-swan events due to non-linear spikes in cross-asset correlations.
    - Difficulty identifying whether a specific token is actively **transmitting** systemic risk or merely **absorbing** external market shocks.
  * **Workflow Decision**: Utilizes daily **Net Directional Spillover** metrics to dynamically reduce allocations to net risk transmitters (e.g., BTC, ETH) and execute targeted portfolio hedges during stress periods.

---

### 3. Quantitative Targets & Operational Deliverables

1. **Quantile Risk Decomposition**: Compute generalized forecast error variance decompositions across lower ($\tau = 0.10$), median ($\tau = 0.50$), and upper ($\tau = 0.90$) quantiles.
2. **Dynamic Fragility Tracking**: Output 200-day rolling Total Spillover Index (TSI) and Relative Tail Dependence (RTD) series to monitor market vulnerability over time.
3. **Productized Delivery**: Deliver modular Python scripts and an interactive dashboard visualizing directional risk networks and contagion heatmaps.