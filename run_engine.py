import pandas as pd
import numpy as np
from scripts.simulation import vasicek_model

# --- INPUT YOUR NUMBERS HERE ---
params = {
    'r0': 0.045,      # Current Short Rate (4.5%)
    'a': 0.15,        # Speed of Mean Reversion
    'b': 0.05,        # Long-term Mean Rate (5.0%)
    'sigma': 0.012,   # Volatility (1.2%)
    'T': 1.0,         # Time Horizon (1 Year)
    'steps': 252,     # Trading Days
    'paths': 10000    # Simulation Iterations
}

def execute_and_export():
    print(f"Starting simulation for {params['paths']} paths...")
    
    # Run the Vasicek SDE
    rates = vasicek_model(
        r0=params['r0'], a=params['a'], b=params['b'], 
        sigma=params['sigma'], T=params['T'], steps=params['steps'], 
        paths=params['paths']
    )
    
    # Convert to DataFrame (Final step rates for VaR analysis)
    # We export a manageable sample (first 100 paths) for the CSV to keep file size low
    df = pd.DataFrame(rates).iloc[:, :100] 
    df.index.name = 'Step_T'
    df_melted = df.reset_index().melt(id_vars='Step_T', var_name='Path_ID', value_name='Simulated_Rate')
    
    # Export to CSV
    df_melted.to_csv('data/simulation_outputs_actual.csv', index=False)
    print("Success: Actual simulation data exported to data/simulation_outputs_actual.csv")

if __name__ == "__main__":
    execute_and_export()
