# Synth911Gen2 - User Guide

**Last Updated:** June 2024

## Welcome to Synth911Gen2! 🌟

This guide will help you get started with using Synth911Gen2 quickly and effectively.

## What is Synth911Gen2?

Synth911Gen2 is a synthetic 911 dispatch data generator for testing, analytics, and training. It supports multiple agencies, locales, and output formats, and provides both GUI and CLI interfaces.

### Key Features

- Realistic synthetic 911 dispatch data
- Multiple agencies and locales
- GUI, CLI, and web interfaces

### Use Cases

- Data science and analytics
- Software testing
- Training and simulation

## Quick Start

### Installation

#### Option 1: pip install

```bash
pip install -r requirements.txt
```

#### Option 2: Development install

```bash
pip install -e .
```

### Verification

```bash
python main.py --help
```

### First Steps

```bash
python main.py --cli -n 1000 -s 2024-01-01 -e 2024-01-31
```

## Getting Started Tutorial

### Step 1: Install dependencies

Install Python 3.11+ and required packages.

```bash
pip install -r requirements.txt
```

### Step 2: Generate data

Run the CLI or GUI to generate your first dataset.

```bash
python main.py --cli -n 1000
```

### Step 3: Explore output

Open the generated CSV file in your favorite tool.

## Core Concepts

### Data Generation

Synth911Gen2 creates realistic incident records for LAW, FIRE, EMS, and RESCUE agencies.

**Example:**

```bash
python main.py --cli -a "LAW,FIRE" -n 1000
```

### Configuration

You can configure agencies, locales, date ranges, and output formats.

**Example:**

```bash
python main.py --cli -l fr_FR -n 1000
```

## Common Use Cases

### Use Case 1: Generate law enforcement data

**Steps:**
1. Set agency to LAW
2. Run CLI with -a LAW
3. Review output

**Example:**

```bash
python main.py --cli -a LAW -n 1000
```

### Use Case 2: Generate multi-agency data

**Steps:**
1. Set agencies to LAW,FIRE,EMS
2. Run CLI with -a LAW,FIRE,EMS
3. Review output

**Example:**

```bash
python main.py --cli -a LAW,FIRE,EMS -n 1000
```

## Configuration

### Basic Configuration

```yaml
agencies: [LAW, FIRE, EMS]
locale: en_US
num_records: 1000
```

### Advanced Configuration

```yaml
agencies: [LAW, FIRE, EMS, RESCUE]
locale: es_ES
num_records: 5000
output_file: spanish_data.csv
```

### Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| agencies | [LAW, FIRE, EMS] | Agencies to include |
| locale | en_US | Data locale |
| num_records | 10000 | Number of records |

## Features Overview

### Realistic Data

**Usage:**

```bash
python main.py --cli -n 1000
```

### Multi-Interface

**Usage:**

```bash
python main.py
```

## Best Practices

### Performance Tips

- Use smaller datasets for testing
- Use efficient output formats

### Security Considerations

- Do not use generated data in production

### Maintenance

- Keep dependencies up to date

## Troubleshooting

### Common Issues

#### Issue: Missing dependencies
**Symptoms:** ImportError
**Solution:** Install required packages

#### Issue: Permission denied
**Symptoms:** File write error
**Solution:** Check file permissions

### Debugging

```bash
python main.py --debug
``` 