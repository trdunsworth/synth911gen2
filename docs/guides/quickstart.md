# Quick Start Guide

Get up and running with Synth911Gen2 in under 5 minutes! This guide will help you generate your first synthetic 911 dispatch dataset.

## 🚀 Prerequisites

Before starting, ensure you have:
- ✅ Python 3.11+ installed
- ✅ Synth911Gen2 installed (see [Installation Guide](installation.md))
- ✅ Basic familiarity with command line

## 📋 Step 1: Verify Installation

First, let's make sure everything is working:

```bash
# Check if the application runs
python main.py --help
```

You should see help text with available options. If you get an error, return to the [Installation Guide](installation.md).

## 🎯 Step 2: Generate Your First Dataset

### Option A: GUI Mode (Easiest for Beginners)

```bash
# Launch the graphical interface
python main.py
```

The GUI will open with default settings:
- **Number of Records**: 10,000
- **Date Range**: 2024-01-01 to 2024-12-31
- **Locale**: English (US)
- **Output File**: computer_aided_dispatch.csv

Simply click "Generate Data" to create your first dataset!

### Option B: Command Line Mode (Fastest)

```bash
# Generate 1,000 records for testing
python main.py --cli -n 1000 -s 2024-01-01 -e 2024-01-31
```

This will create a file called `computer_aided_dispatch.csv` with 1,000 records.

### Option C: Interactive Mode (Guided)

```bash
# Get step-by-step guidance
python main.py --interactive
```

Follow the prompts to configure your dataset.

## 📊 Step 3: Check Your Results

After generation, you'll find a CSV file with columns like:

| incident_id | timestamp | caller_name | location | incident_type | priority | agency |
|-------------|-----------|-------------|----------|---------------|----------|--------|
| INC-2024-000001 | 2024-01-01 08:15:22 | John Smith | 123 Main St | Medical Emergency | 2 | EMS |
| INC-2024-000002 | 2024-01-01 09:30:45 | Jane Doe | 456 Oak Ave | Traffic Accident | 3 | LAW |

## 📊 Distribution Analysis Utility

You can analyze the statistical distribution of numeric columns in any CSV file using:

```bash
python data/distribution_analyzer.py your_file.csv
```

See [Distribution Analysis Example](../examples/distribution_analysis.md) for details.

## 🎨 Step 4: Customize Your Data

### Change the Language/Locale

```bash
# Generate French data
python main.py --cli -n 1000 -l fr_FR -o french_dispatch.csv

# Generate Spanish data
python main.py --cli -n 1000 -l es_ES -o spanish_dispatch.csv
```

### Specify Agencies

```bash
# Only law enforcement and fire department
python main.py --cli -n 1000 -a "LAW,FIRE" -o law_fire_only.csv

# Only medical emergencies
python main.py --cli -n 1000 -a "EMS" -o medical_only.csv
```

### Custom Date Range

```bash
# Generate data for a specific month
python main.py --cli -n 5000 -s 2024-06-01 -e 2024-06-30 -o june_2024.csv

# Generate data for multiple years
python main.py --cli -n 10000 -s 2023-01-01 -e 2024-12-31 -o two_year_data.csv
```

### Custom Agency Probabilities

You can control the distribution of agencies in your dataset by specifying custom probabilities (must sum to 1.0):

```bash
# 80% LAW, 20% FIRE
python main.py --cli -n 1000 -a "LAW,FIRE" --agency-probabilities 0.8,0.2 -o law_fire_weighted.csv

# 50% LAW, 30% FIRE, 20% EMS
python main.py --cli -n 1000 -a "LAW,FIRE,EMS" --agency-probabilities 0.5,0.3,0.2 -o weighted_agencies.csv
```

This option is also available in the GUI and Web interfaces as a comma-separated field.

## 🔧 Step 5: Advanced Configuration

### Large Datasets

For generating large datasets (50,000+ records):

```bash
# Generate 100,000 records
python main.py --cli -n 100000 -s 2024-01-01 -e 2024-12-31 -o large_dataset.csv
```

**Note**: Large datasets may take several minutes to generate and require more memory.

### Multiple Dispatchers

```bash
# Use 20 different dispatcher names
python main.py --cli -n 10000 --num-names 20 -o multi_dispatcher.csv
```

### Custom Output Location

```bash
# Save to a specific directory
python main.py --cli -n 1000 -o /path/to/your/data/emergency_data.csv
```

## 📈 Step 6: Analyze Your Data

### Basic Statistics

```python
import pandas as pd

# Load your generated data
df = pd.read_csv('computer_aided_dispatch.csv')

# Basic statistics
print(f"Total records: {len(df)}")
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"Agencies: {df['agency'].unique()}")
print(f"Incident types: {df['incident_type'].value_counts()}")
```

### Time Analysis

```python
# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Hourly distribution
hourly_counts = df['timestamp'].dt.hour.value_counts().sort_index()
print("Calls by hour:")
print(hourly_counts)
```

## 🚨 Common Scenarios

### Testing Environment Setup

```bash
# Generate small test dataset
python main.py --cli -n 100 -s 2024-01-01 -e 2024-01-02 -o test_data.csv
```

### Training Data for ML Models

```bash
# Generate diverse dataset for machine learning
python main.py --cli -n 50000 -s 2023-01-01 -e 2024-12-31 -l en_US -a "LAW,FIRE,EMS" -o ml_training_data.csv
```

### Multi-Language Testing

```bash
# Generate datasets in multiple languages
for locale in en_US fr_FR es_ES de_DE; do
    python main.py --cli -n 1000 -l $locale -o ${locale}_data.csv
done
```

## 🛠️ Troubleshooting

### GUI Not Opening

```bash
# Try command line mode instead
python main.py --cli -n 1000
```

### Memory Issues

```bash
# Reduce number of records
python main.py --cli -n 100
```

### File Permission Errors

```bash
# Check write permissions
ls -la computer_aided_dispatch.csv

# Or specify a different output location
python main.py --cli -n 1000 -o ~/Desktop/my_data.csv
```

## 📚 Next Steps

Now that you've generated your first dataset, explore:

- **[GUI Usage Guide](gui-usage.md)** - Master the graphical interface
- **[Command Line Guide](cli-usage.md)** - Learn advanced CLI options
- **[Configuration Guide](configuration.md)** - Customize the application
- **[Examples](../examples/)** - See real-world usage patterns

## 🆘 Need Help?

- **Issues**: Check the terminal output for error messages
- **Documentation**: Browse the guides in this documentation
- **Examples**: Look at the examples directory for working code
- **GitHub**: Report bugs or request features

---

**Congratulations!** You've successfully generated your first synthetic 911 dispatch dataset. 🎉