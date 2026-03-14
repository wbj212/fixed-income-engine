import numpy as np

def vasicek_model(r0, a, b, sigma, T, steps, paths=10000):
    """
    Simulates interest rate paths using the Vasicek Stochastic Differential Equation.
    dr_t = a(b - r_t)dt + sigma * dW_t
    """
    dt = T / steps
    rates = np.zeros((steps, paths))
    rates[0] = r0
    
    for t in range(1, steps):
        # Browninan Motion component
        dW = np.random.normal(0, np.sqrt(dt), paths)
        # SDE Step: Mean reversion + Volatility
        dr = a * (b - rates[t-1]) * dt + sigma * dW
        rates[t] = rates[t-1] + dr
        
    return rates

def calculate_portfolio_var(simulated_rates, confidence_level=0.99):
    """Calculates Value-at-Risk (VaR) from the simulated distribution."""
    final_rates = simulated_rates[-1]
    # Calculate losses relative to the mean or current value
    percentile = np.percentile(final_rates, (1 - confidence_level) * 100)
    return round(percentile, 6)

# Example usage for calibration:
# rates = vasicek_model(r0=0.045, a=0.1, b=0.05, sigma=0.01, T=1, steps=252)
