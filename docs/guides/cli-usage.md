# Command Line Usage Guide

This guide covers all aspects of using Synth911Gen2 from the command line interface.

## 🚀 Quick Start

### Basic Command

```bash
# Generate 1,000 records with default settings
python main.py --cli -n 1000
```

### Common Patterns

```bash
# Generate data for a specific month
python main.py --cli -n 5000 -s 2024-06-01 -e 2024-06-30

# Generate French data
python main.py --cli -n 1000 -l fr_FR -o french_data.csv

# Generate only law enforcement data
python main.py --cli -n 2000 -a "LAW" -o law_enforcement.csv

# Generate data using uv run
uv run main.py --cli -n 2000 -a "LAW" -o law_enforcement.csv
```

## 📋 Command Line Options

### Required Options

| Option | Description | Example |
|--------|-------------|---------|
| `--cli` | Enable command-line mode | `python main.py --cli` |

### Data Generation Options

| Option | Short | Description | Default | Example |
|--------|-------|-------------|---------|---------|
| `--num-records` | `-n` | Number of records to generate | `10000` | `-n 5000` |
| `--start-date` | `-s` | Start date (YYYY-MM-DD) | `2024-01-01` | `-s 2024-06-01` |
| `--end-date` | `-e` | End date (YYYY-MM-DD) | `2024-12-31` | `-e 2024-06-30` |
| `--num-names` | | Names per shift | `8` | `--num-names 12` |
| `--locale` | `-l` | Faker locale | `en_US` | `-l fr_FR` |
| `--agencies` | `-a` | Comma-separated agencies | All | `-a "LAW,FIRE"` |
| `--output-file` | `-o` | Output file path | `computer_aided_dispatch.csv` | `-o my_data.csv` |
| `--agency-probabilities` | | Probabilities for selected agencies (comma-separated, must sum to 1) | | `--agency-probabilities 0.7,0.2,0.1` |

### Information Options

| Option | Description | Example |
|--------|-------------|---------|
| `--list-locales` | Show available locales | `python main.py --cli --list-locales` |
| `--help` | Show help message | `python main.py --cli --help` |

## 🎯 Usage Examples

### Example 1: Basic Data Generation

```bash
# Generate 10,000 records for 2024
python main.py --cli -n 10000 -s 2024-01-01 -e 2024-12-31
```

**Output:**
```
Starting data generation...
Number of records: 10000
Date range: 2024-01-01 to 2024-12-31
Locale: en_US
Output file: computer_aided_dispatch.csv

Data generation completed successfully!
Generated 10000 records
```

### Example 2: Multi-Language Data

```bash
# Generate French data
python main.py --cli -n 5000 -l fr_FR -o french_dispatch.csv

# Generate Spanish data
python main.py --cli -n 5000 -l es_ES -o spanish_dispatch.csv

# Generate German data
python main.py --cli -n 5000 -l de_DE -o german_dispatch.csv
```

### Example 3: Agency-Specific Data

```bash
# Generate only law enforcement data
python main.py --cli -n 2000 -a "LAW" -o law_enforcement.csv

# Generate fire and EMS data
python main.py --cli -n 3000 -a "FIRE,EMS" -o fire_ems.csv

# Generate all agency types
python main.py --cli -n 5000 -a "LAW,FIRE,EMS,RESCUE" -o all_agencies.csv
```

### Example 4: Time-Specific Data

```bash
# Generate data for a specific month
python main.py --cli -n 1000 -s 2024-06-01 -e 2024-06-30 -o june_2024.csv

# Generate data for multiple years
python main.py --cli -n 20000 -s 2023-01-01 -e 2024-12-31 -o two_year_data.csv

# Generate data for a specific week
python main.py --cli -n 500 -s 2024-03-18 -e 2024-03-24 -o week_12.csv
```

### Example 5: Custom Configuration

```bash
# Generate data with 20 dispatchers
python main.py --cli -n 10000 --num-names 20 -o multi_dispatcher.csv

# Generate data with custom output location
python main.py --cli -n 5000 -o /path/to/your/data/emergency_data.csv

# Generate data with all custom parameters
python main.py --cli \
  -n 15000 \
  -s 2024-01-01 \
  -e 2024-12-31 \
  --num-names 15 \
  -l es_ES \
  -a "LAW,FIRE,EMS" \
  -o spanish_emergency_2024.csv
```

### Example 6: Custom Agency Probabilities

```bash
# Generate data with custom probabilities for LAW and FIRE
python main.py --cli -n 1000 -a "LAW,FIRE" --agency-probabilities 0.8,0.2 -o law_fire_weighted.csv

# Generate data with custom probabilities for three agencies
python main.py --cli -n 1000 -a "LAW,FIRE,EMS" --agency-probabilities 0.5,0.3,0.2 -o weighted_agencies.csv
```

## 🔍 Information Commands

### List Available Locales

```bash
python main.py --cli --list-locales
```

**Output:**
```
Available locales:
  en_US    - American English
  en_GB    - British English
  fr_FR    - French
  de_DE    - German
  es_ES    - Spanish
  it_IT    - Italian
  pt_BR    - Brazilian Portuguese
  nl_NL    - Dutch
  pl_PL    - Polish
  ru_RU    - Russian
  ja_JP    - Japanese
  ko_KR    - Korean
  zh_CN    - Chinese (Simplified)
  ar_SA    - Arabic
```

### Show Help

```bash
python main.py --cli --help
```

**Output:**
```
usage: main.py --cli [-h] [-n NUM_RECORDS] [-s START_DATE] [-e END_DATE] 
                    [--num-names NUM_NAMES] [-l LOCALE] [-o OUTPUT_FILE] 
                    [-a AGENCIES] [--list-locales]

Generate synthetic 911 dispatch data

options:
  -h, --help            show this help message and exit
  -n NUM_RECORDS, --num-records NUM_RECORDS
                        Number of records to generate (default: 10000)
  -s START_DATE, --start-date START_DATE
                        Start date in YYYY-MM-DD format (default: 2024-01-01)
  -e END_DATE, --end-date END_DATE
                        End date in YYYY-MM-DD format (default: 2024-12-31)
  --num-names NUM_NAMES
                        Number of names to generate per shift (default: 8)
  -l LOCALE, --locale LOCALE
                        Faker locale for generating localized data (default: en_US)
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Output file path (default: computer_aided_dispatch.csv)
  -a AGENCIES, --agencies AGENCIES
                        Comma-separated list of agencies to include (e.g., LAW,FIRE)
  --list-locales        List available locales and exit
```

## ⚙️ Advanced Usage

### Batch Processing

Create a script to generate multiple datasets:

```bash
#!/bin/bash
# generate_multiple_datasets.sh

# Generate datasets for different languages
for locale in en_US fr_FR es_ES de_DE; do
    echo "Generating data for $locale..."
    python main.py --cli -n 1000 -l $locale -o ${locale}_data.csv
done

# Generate datasets for different time periods
for month in 01 02 03 04 05 06; do
    echo "Generating data for 2024-$month..."
    python main.py --cli -n 500 -s 2024-$month-01 -e 2024-$month-30 -o 2024_${month}_data.csv
done
```

### Using with Cron (Linux/macOS)

Schedule regular data generation:

```bash
# Edit crontab
crontab -e

# Add line to generate daily data at 2 AM
0 2 * * * cd /path/to/synth911gen2 && python main.py --cli -n 1000 -o daily_data_$(date +\%Y\%m\%d).csv
```

### Using with Task Scheduler (Windows)

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily at 2 AM)
4. Set action: `python main.py --cli -n 1000 -o daily_data.csv`

## 🔧 Configuration Files

### Environment Variables

Set default values using environment variables:

```bash
# Set default locale
export SYNTH911_LOCALE=fr_FR

# Set default output directory
export SYNTH911_OUTPUT_DIR=/path/to/data

# Set default number of records
export SYNTH911_NUM_RECORDS=5000
```

### Configuration Script

Create a configuration script:

```bash
#!/bin/bash
# config.sh

# Default settings
DEFAULT_LOCALE="en_US"
DEFAULT_RECORDS=10000
DEFAULT_OUTPUT="computer_aided_dispatch.csv"

# Function to generate data with defaults
generate_data() {
    local records=${1:-$DEFAULT_RECORDS}
    local locale=${2:-$DEFAULT_LOCALE}
    local output=${3:-$DEFAULT_OUTPUT}
    
    python main.py --cli -n $records -l $locale -o $output
}

# Usage: generate_data [records] [locale] [output_file]
```

## 🚨 Error Handling

### Common Errors and Solutions

#### Invalid Date Format

```bash
# Error
python main.py --cli -s 2024/01/01

# Solution: Use YYYY-MM-DD format
python main.py --cli -s 2024-01-01
```

#### Invalid Locale

```bash
# Error
python main.py --cli -l invalid_locale

# Solution: Check available locales
python main.py --cli --list-locales
```

#### Permission Denied

```bash
# Error: Permission denied when writing output file

# Solution: Check write permissions
ls -la /path/to/output/directory
chmod 755 /path/to/output/directory
```

#### Memory Issues

```bash
# Error: Out of memory for large datasets

# Solution: Reduce number of records or use chunking
python main.py --cli -n 1000  # Instead of 100000
```

### Debug Mode

Enable verbose output for troubleshooting:

```bash
# Set debug environment variable
export SYNTH911_DEBUG=1

# Run command with debug output
python main.py --cli -n 100
```

## 📊 Output Analysis

### Quick Data Validation

```bash
# Check generated file
ls -la computer_aided_dispatch.csv

# Count lines (records + header)
wc -l computer_aided_dispatch.csv

# Check file size
du -h computer_aided_dispatch.csv
```

### Data Preview

```bash
# View first few lines
head -5 computer_aided_dispatch.csv

# View last few lines
tail -5 computer_aided_dispatch.csv

# Check column headers
head -1 computer_aided_dispatch.csv
```

## 🔄 Automation Examples

### Continuous Integration

```yaml
# .github/workflows/generate-data.yml
name: Generate Test Data

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
  workflow_dispatch:  # Manual trigger

jobs:
  generate-data:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: python main.py --cli -n 1000 -o test_data.csv
      - uses: actions/upload-artifact@v3
        with:
          name: test-data
          path: test_data.csv
```

### Docker Integration

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Default command
CMD ["python", "main.py", "--cli", "-n", "1000"]
```

```bash
# Run in Docker
docker build -t synth911gen2 .
docker run -v $(pwd)/output:/app/output synth911gen2 --cli -n 1000 -o /app/output/data.csv
```

## 📈 Performance Tips

### Large Dataset Generation

```bash
# For very large datasets, use chunking
for i in {1..10}; do
    python main.py --cli -n 10000 -o chunk_${i}.csv
done

# Combine chunks
cat chunk_*.csv > large_dataset.csv
```

### Memory Optimization

```bash
# Use smaller chunks for memory-constrained systems
python main.py --cli -n 1000 -o small_chunk.csv

# Process in background
nohup python main.py --cli -n 50000 -o large_dataset.csv &
```

## 🆘 Troubleshooting

### Common Issues

1. **Command not found**: Ensure Python is in PATH
2. **Module not found**: Install dependencies with `pip install -r requirements.txt`
3. **Permission denied**: Check file permissions and directory access
4. **Out of memory**: Reduce number of records or use chunking
5. **Invalid locale**: Use `--list-locales` to see available options

### Getting Help

```bash
# Show help
python main.py --cli --help

# Check version
python main.py --version

# List locales
python main.py --cli --list-locales
```

---

**Next Steps**: 
- Explore [Interactive Mode](interactive-mode.md) for guided usage
- Check [GUI Usage](gui-usage.md) for graphical interface
- Review [Examples](../examples/) for advanced usage patterns