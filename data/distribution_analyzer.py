import pandas as pd
import numpy as np
from scipy import stats
import sys

# Load the CSV, automatically handling NULLs as NaN
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'synth_seed2.csv'
df = pd.read_csv(filename)

# Select numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

results = {}

for col in numeric_cols:
    data = df[col].dropna()
    desc = data.describe()
    # Try fitting common distributions
    distributions = {
        'normal': stats.norm,
        'exponential': stats.expon,
        'uniform': stats.uniform,
        'lognormal': stats.lognorm,
        'poisson': stats.poisson if np.all(data == data.astype(int)) else None,
        'binomial': stats.binom if set(data.unique()) <= {0, 1} else None,
    }
    best_fit = None
    best_p = -1
    best_params = None
    for name, dist in distributions.items():
        if dist is None:
            continue
        try:
            # Fix for lognormal: only fit to strictly positive data
            if name == 'lognormal':
                data_to_fit = data[data > 0]
                if len(data_to_fit) == 0:
                    continue
            else:
                data_to_fit = data
            params = dist.fit(data_to_fit)
            # Kolmogorov-Smirnov test
            D, p = stats.kstest(data_to_fit, name, args=params)
            if p > best_p:
                best_fit = name
                best_p = p
                best_params = params
        except Exception:
            continue
    results[col] = {
        'best_fit': best_fit,
        'p_value': best_p,
        'params': best_params,
        'summary': desc.to_dict()
    }

# Output results to both console and file
output_file = f"distribution_results_{filename.replace('.csv','')}.txt"
with open(output_file, 'w') as f:
    for col, res in results.items():
        output = (
            f"Column: {col}\n"
            f"  Best fit: {res['best_fit']}\n"
            f"  Parameters: {res['params']}\n"
            f"  p-value: {res['p_value']:.4f}\n"
            f"  Summary: {res['summary']}\n\n"
        )
        print(output)
        f.write(output)