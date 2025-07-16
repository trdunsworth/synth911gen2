"""
Synthetic 911 Call Volume Generator

This module generates realistic synthetic inbound call volumes for 911 emergency centers
based on probability distributions from historical data. It supports generating data
at different frequencies (hourly, daily, weekly, monthly) and allows customization
of the time period and number of data points.

Usage:
    python synthvolgen.py <start_date> <num_rows> <frequency> [--output OUTPUT_FILE]

Example:
    python synthvolgen.py 2025-01-01 168 hour --output call_volumes.csv

Author: GitHub Copilot
Date: July 2025
"""

import os
import argparse
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def load_data(frequency):
    """
    Load call volume probability distribution data for the specified frequency.

    Args:
        frequency (str): One of 'hour', 'day', 'week', or 'month'.

    Returns:
        pd.DataFrame: DataFrame with volume data.

    Raises:
        ValueError: If frequency is not one of the accepted values.
    """
    if frequency == 'hour':
        return pd.read_csv('data/hour.csv')
    elif frequency == 'day':
        return pd.read_csv('data/day.csv')
    elif frequency == 'week':
        return pd.read_csv('data/week.csv')
    elif frequency == 'month':
        return pd.read_csv('data/month.csv')
    else:
        raise ValueError("Frequency must be one of: 'hour', 'day', 'week', 'month'")

def generate_call_volumes(start_date, num_rows, frequency):
    """
    Generate synthetic inbound call volumes for a 911 center.

    Args:
        start_date (datetime): The starting date and time for the generated data.
        num_rows (int): The number of rows (time intervals) to generate.
        frequency (str): The frequency of the data ('hour', 'day', 'week', or 'month').

    Returns:
        pd.DataFrame: DataFrame with columns 'DateTime' and 'CallVolume'.
    """
    data = load_data(frequency)
    call_volumes = []

    for i in range(num_rows):
        if frequency == 'hour':
            current_time = start_date + timedelta(hours=i)
            # Use hour of day to get base volume, add some randomness
            hour = current_time.hour
            base_volume = data.iloc[hour]['volume']
            # Add random variation (±20%)
            variation = np.random.normal(0, 0.2)
            volume = max(1, int(base_volume * (1 + variation)))
            
        elif frequency == 'day':
            current_time = start_date + timedelta(days=i)
            # Use random sampling from historical daily volumes with some variation
            base_volume = np.random.choice(data['call_volume'])
            variation = np.random.normal(0, 0.15)
            volume = max(1, int(base_volume * (1 + variation)))
            
        elif frequency == 'week':
            current_time = start_date + timedelta(weeks=i)
            # For weekly data, we'll use a different approach
            week_data = pd.read_csv('data/week.csv')
            base_volume = np.random.choice(week_data.iloc[:, 1])  # Second column
            variation = np.random.normal(0, 0.1)
            volume = max(1, int(base_volume * (1 + variation)))
            
        elif frequency == 'month':
            current_time = start_date + timedelta(days=i*30)  # Approximation for month
            month_data = pd.read_csv('data/month.csv')
            base_volume = np.random.choice(month_data.iloc[:, 1])  # Second column
            variation = np.random.normal(0, 0.1)
            volume = max(1, int(base_volume * (1 + variation)))
        else:
            raise ValueError("Frequency must be one of: 'hour', 'day', 'week', 'month'")

        call_volumes.append({'DateTime': current_time, 'CallVolume': volume})

    return pd.DataFrame(call_volumes)

def main():
    """
    Parse command-line arguments and generate synthetic call volume data.

    Command-line Arguments:
        start_date (str): Starting date in YYYY-MM-DD format.
        num_rows (int): Number of rows to generate.
        frequency (str): Frequency of call volume data ('hour', 'day', 'week', or 'month').
        --output (str, optional): Output CSV file path. If not provided, prints to console.

    Outputs:
        CSV file or console output with generated call volume data.
    """
    parser = argparse.ArgumentParser(description='Generate realistic inbound call volumes for a 911 center.')
    parser.add_argument('start_date', type=str, help='Starting date in YYYY-MM-DD format')
    parser.add_argument('num_rows', type=int, help='Number of rows to generate')
    parser.add_argument('frequency', type=str, choices=['hour', 'day', 'week', 'month'], help='Frequency of call volume data')
    parser.add_argument('--output', type=str, help='Output CSV file path')
    
    args = parser.parse_args()
    
    start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
    call_volume_data = generate_call_volumes(start_date, args.num_rows, args.frequency)
    
    if args.output:
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(args.output)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Save to CSV file
        call_volume_data.to_csv(args.output, index=False)
        print(f"Generated {len(call_volume_data)} rows of call volume data saved to {args.output}")
        print(f"Date range: {call_volume_data['DateTime'].min()} to {call_volume_data['DateTime'].max()}")
    else:
        print(call_volume_data)

if __name__ == '__main__':
    main()
