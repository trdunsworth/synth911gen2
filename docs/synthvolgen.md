# Synthetic 911 Call Volume Generator

## Overview

The `synthvolgen_new.py` script is a command-line tool that generates realistic synthetic inbound call volumes for 911 emergency centers. It uses historical data patterns from CSV files to create statistically realistic call volume data at different time frequencies (hourly, daily, weekly, monthly).

## Features

- **Multiple Time Frequencies**: Generate data at hourly, daily, weekly, or monthly intervals
- **Historical Pattern-Based**: Uses real historical patterns from CSV data files
- **Realistic Variation**: Adds statistical variation to base patterns to simulate real-world conditions
- **Flexible Output**: Save to CSV file or print to console
- **Configurable Time Periods**: Specify any start date and number of data points

## Installation

### Prerequisites

- Python 3.7+
- Required packages:
  ```bash
  pip install pandas numpy
  ```

### File Structure

The script expects the following data files in a `data/` subdirectory:
```
data/
├── hour.csv     # Hourly call volume patterns (24 hours)
├── day.csv      # Daily call volume historical data
├── week.csv     # Weekly call volume patterns
└── month.csv    # Monthly call volume patterns
```

## Usage

### Command Line Syntax

```bash
python synthvolgen_new.py <start_date> <num_rows> <frequency> [--output OUTPUT_FILE]
```

### Parameters

- **`start_date`** (required): Starting date in YYYY-MM-DD format
- **`num_rows`** (required): Number of time intervals to generate
- **`frequency`** (required): Time frequency - one of:
  - `hour` - Generate hourly data
  - `day` - Generate daily data
  - `week` - Generate weekly data
  - `month` - Generate monthly data
- **`--output`** (optional): Output CSV file path. If not specified, prints to console

### Examples

#### Generate Hourly Data
```bash
# Generate 168 hours (1 week) of hourly call data starting Jan 1, 2025
python synthvolgen_new.py 2025-01-01 168 hour --output weekly_calls.csv

# Generate 13,140 hours (~1.5 years) of data
python synthvolgen_new.py 2023-08-01 13140 hour --output test_hour_freq1.csv
```

#### Generate Daily Data
```bash
# Generate 30 days of daily call data
python synthvolgen_new.py 2025-01-01 30 day --output monthly_calls.csv
```

#### Generate Weekly Data
```bash
# Generate 52 weeks (1 year) of weekly data
python synthvolgen_new.py 2025-01-01 52 week --output yearly_weekly_calls.csv
```

#### Print to Console (No File Output)
```bash
# Generate 10 hours of data and print to console
python synthvolgen_new.py 2025-01-01 10 hour
```

## Output Format

The generated CSV file contains two columns:

| Column | Description | Example |
|--------|-------------|---------|
| `DateTime` | Timestamp for the data point | `2025-01-01 00:00:00` |
| `CallVolume` | Number of calls for that time period | `15` |

### Sample Output
```csv
DateTime,CallVolume
2025-01-01 00:00:00,8
2025-01-01 01:00:00,6
2025-01-01 02:00:00,5
2025-01-01 03:00:00,2
2025-01-01 04:00:00,2
```

## Data Generation Logic

### Hourly Data
- Uses 24-hour pattern from `hour.csv`
- Maps current hour (0-23) to base volume from historical data
- Adds ±20% random variation using normal distribution
- Ensures minimum volume of 1 call

### Daily Data
- Randomly samples from historical daily volumes in `day.csv`
- Adds ±15% random variation
- Maintains realistic daily patterns

### Weekly Data
- Uses patterns from `week.csv`
- Adds ±10% variation for stability
- Generates weekly totals

### Monthly Data
- Uses patterns from `month.csv`
- Adds ±10% variation
- Approximates months as 30-day periods

## Data File Requirements

### hour.csv
Expected format:
```csv
hour,volume
00:00,10
01:00,8
02:00,5
...
23:00,15
```

### day.csv
Expected format:
```csv
date,call_volume
2023-01-01,150
2023-01-02,200
2023-01-03,180
...
```

### week.csv and month.csv
Should contain historical weekly/monthly volume data with volume in the second column.

## Error Handling

The script includes error handling for:
- Invalid frequency parameters
- Missing data files
- Invalid date formats
- File I/O errors

Common error messages:
- `"Frequency must be one of: 'hour', 'day', 'week', 'month'"` - Invalid frequency parameter
- `FileNotFoundError` - Missing required CSV data files
- `ValueError` - Invalid date format (use YYYY-MM-DD)

## Performance Considerations

- **Large Datasets**: Generating 13,000+ rows may take a few seconds
- **Memory Usage**: Script loads entire data files into memory
- **File Size**: Hourly data for 1 year ≈ 200KB output file

## Use Cases

### Emergency Services Planning
- **Capacity Planning**: Generate call volume forecasts for staffing decisions
- **Resource Allocation**: Model different scenarios for equipment and personnel needs
- **Training Data**: Create datasets for dispatcher training simulations

### Research and Analysis
- **Statistical Modeling**: Generate test datasets for call volume analysis algorithms
- **System Testing**: Create realistic load data for testing 911 system capacity
- **Academic Research**: Provide anonymized call volume data for emergency services research

### Business Intelligence
- **Trend Analysis**: Generate historical-like data for trend analysis tools
- **Dashboard Testing**: Create sample data for BI dashboard development
- **Simulation Studies**: Model "what-if" scenarios for different call volume patterns

## Troubleshooting

### Common Issues

1. **"KeyError: 'volume'"**
   - Check that `hour.csv` has columns named `hour,volume`
   - Verify data file format matches expected structure

2. **"FileNotFoundError"**
   - Ensure `data/` folder exists in the same directory as the script
   - Check that all required CSV files are present

3. **"No output generated"**
   - Verify the script completed (check for error messages)
   - For large datasets, wait for completion (may take time)

### Debug Mode
Run with smaller datasets first to verify functionality:
```bash
python synthvolgen_new.py 2025-01-01 5 hour
```

## Version History

- **July 2025**: Initial version with support for all frequency types
- **July 2025**: Added CSV output functionality and improved error handling

## Contributing

When modifying this script:
1. Maintain backward compatibility with existing data file formats
2. Add appropriate error handling for new features
3. Update this documentation for any new functionality
4. Test with sample data before deploying

## License

This script is part of the synth911gen2 project. See project README for license information.
