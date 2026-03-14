# Fixed Income Risk Engine: Stochastic Yield Modeling
**Quantitative Research | Risk & Analytics Portfolio**

A high-fidelity simulation engine designed to quantify interest rate sensitivity and portfolio tail risk using stochastic differential equations (SDEs). This project bridges the gap between theoretical fixed income math and production-grade risk monitoring.

## 🛠 Core Methodology
The engine utilizes a **Vasicek Model** to simulate the evolution of short-term interest rates. Unlike simpler models, the Vasicek framework accounts for **mean reversion**, a critical characteristic of interest rate regimes in fixed income markets.

### The Stochastic Differential Equation (SDE)
The short rate $r_t$ is modeled as:
$$dr_t = a(b - r_t)dt + \sigma dW_t$$

Where:
* **$a$ (0.15):** The speed of mean reversion, ensuring rates pull back toward the long-term target.
* **$b$ (0.05):** The long-term mean rate (5.0%).
* **$\sigma$ (0.012):** The instantaneous volatility (1.2%).
* **$dW_t$:** Standard Brownian Motion representing market shocks.

## 📈 Model Capabilities
* **Monte Carlo Simulation:** Generates 10,000 paths to visualize the probability distribution of future rate environments.
* **Sensitivity Analysis:** Calculates **Modified Duration** and **Convexity** for a multi-asset portfolio to estimate PnL impact from yield curve shifts.
* **Risk Metrics:** Computes **99% Value-at-Risk (VaR)** to quantify the maximum expected loss over a 1-year horizon.

## 📂 Repository Structure
* `data/`: Contains calibrated market yields and simulated output paths (`simulation_outputs_actual.csv`).
* `scripts/`: Core logic for the Vasicek SDE and bond pricing sensitivity.
* `index.html`: A high-fidelity "Data Ops" dashboard visualizing the engine's output.

## 🎓 The "Engine" Philosophy
As an **Applied Math & Chemical Engineering** major at the **University of Minnesota**, I view financial risk through the lens of logical systems and stochastic flow. This engine is built to be modular, allowing for "plug-and-play" calibration as market regimes shift.

---
*Developed by Benjamin Jeong | 2026*
