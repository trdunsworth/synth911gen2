# Synth911Gen2 - Synthetic 911 Dispatch Data Generator

> **Full documentation is available in [`docs/README.md`](docs/README.md).**

A comprehensive Python application for generating realistic synthetic 911 dispatch data for testing, training, and development purposes. This tool creates anonymized emergency dispatch records that maintain statistical patterns and relationships found in real emergency data.

## Features

- **Multi-Interface Support**: GUI (Tkinter), command-line, and text-based (TUI) interfaces
- **Multi-Language Support**: Generate data in 14+ locales including English, French, German, Spanish, and more
- **Flexible Data Generation**: Customizable number of records, date ranges, and agency types
- **Realistic Data Patterns**: Maintains realistic relationships between emergency types, times, and locations
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Headless Mode**: Perfect for automated data generation and CI/CD pipelines
- **Web Interface**: Optional Flask-based web GUI for remote access

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [GUI Mode](#gui-mode)
  - [Command Line Mode](#command-line-mode)
  - [Interactive Mode](#interactive-mode)
  - [TUI (Text User Interface) Mode](#tui-text-user-interface-mode)
  - [Web Interface](#web-interface)
- [Configuration](#configuration)
- [Data Format](#data-format)
- [API Reference](#api-reference)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Documentation](#documentation)

## Installation

### Prerequisites

- Python 3.11 or higher
- pip or uv package manager

### Install Dependencies

```bash
# Using pip
pip install -r requirements.txt

# Using uv (recommended)
uv sync
```

### Verify Installation

```bash
python main.py --help
```

## Quick Start

### GUI Mode (Recommended for beginners)

```bash
python main.py
```

### Command Line Mode

```bash
# Generate 10,000 records for 2024
python main.py --cli -n 10000 -s 2024-01-01 -e 2024-12-31

# Generate French data
python main.py --cli -n 5000 -l fr_FR -o french_dispatch.csv

# Generate data using uv
uv run main.py --cli -n 12000 -s 2024-01-01 -e 2024-12-31 -l en_GB -a "FIRE,EMS" -0 uv_test.csv
```

### Interactive Mode

```bash
python main.py --interactive
```

### TUI (Text User Interface) Mode

The TUI provides a terminal-based interactive experience for generating data:

```bash
python tui.py

# Start the TUI using uv
uv run tui.py
```

This mode is ideal for users who prefer keyboard navigation and a fast, text-based workflow.

## Usage

### GUI Mode

The graphical interface provides an intuitive way to configure and generate data:

1. **Number of Records**: Set how many dispatch records to generate
2. **Date Range**: Specify start and end dates for the data
3. **Names per Shift**: Configure how many dispatcher names to rotate
4. **Locale**: Choose the language/region for generated data
5. **Agencies**: Specify which emergency agencies to include
6. **Output File**: Set the destination CSV file

### Command Line Mode

```bash
# Basic usage
python main.py --cli -n 10000 -s 2024-01-01 -e 2024-12-31

# Advanced options
python main.py --cli \
  -n 50000 \
  -s 2024-01-01 \
  -e 2024-12-31 \
  --num-names 12 \
  -l es_ES \
  -a "LAW,FIRE,EMS" \
  -o spanish_emergency_data.csv

# List available locales
python main.py --cli --list-locales
```

#### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `-n, --num-records` | Number of records to generate | 10000 |
| `-s, --start-date` | Start date (YYYY-MM-DD) | 2024-01-01 |
| `-e, --end-date` | End date (YYYY-MM-DD) | 2024-12-31 |
| `--num-names` | Names per shift | 8 |
| `-l, --locale` | Faker locale | en_US |
| `-a, --agencies` | Comma-separated agencies | All |
| `-o, --output-file` | Output file path | computer_aided_dispatch.csv |
| `--list-locales` | Show available locales | - |

### Interactive Mode

Interactive mode guides you through the configuration process:

```bash
python main.py --interactive
```

This mode prompts for each setting and validates input before generation.

### TUI (Text User Interface) Mode

The TUI provides a terminal-based interactive experience for generating data:

```bash
python tui.py
```

This mode is ideal for users who prefer keyboard navigation and a fast, text-based workflow.

### Web Interface

For remote access or server deployment:

```bash
python webgui.py
```

Access the web interface at `http://localhost:5000`

## Configuration

### Supported Locales

The application supports 14+ locales for generating localized data:

- `en_US` - American English
- `en_GB` - British English  
- `fr_FR` - French
- `de_DE` - German
- `es_ES` - Spanish
- `it_IT` - Italian
- `pt_BR` - Brazilian Portuguese
- `nl_NL` - Dutch
- `pl_PL` - Polish
- `ru_RU` - Russian
- `ja_JP` - Japanese
- `ko_KR` - Korean
- `zh_CN` - Chinese (Simplified)
- `ar_SA` - Arabic

### Agency Types

Common emergency agency types include:
- `LAW` - Law enforcement
- `FIRE` - Fire department
- `EMS` - Emergency medical services
- `RESCUE` - Search and rescue

## Data Format

Generated data is saved in CSV format with the following columns:

| Column                | Description                        | Example                  |
|-----------------------|------------------------------------|--------------------------|
| `call_id`             | Unique call identifier              | CALL-2024-000123         |
| `agency`              | Responding agency                   | EMS                      |
| `event_time`          | Date and time of event              | 2024-03-15 14:30:22      |
| `day_of_year`         | Day of the year (1-366)             | 74                       |
| `week_no`             | ISO week number                     | 11                       |
| `hour`                | Hour of day (0-23)                  | 14                       |
| `day_night`           | Day or night indicator              | Day                      |
| `dow`                 | Day of week (0=Mon, 6=Sun)          | 2                        |
| `shift`               | Shift name or number                | A                        |
| `shift_part`          | Part of shift (e.g., start/end)     | Start                    |
| `problem`             | Reported problem/incident type      | Medical Emergency        |
| `address`             | Incident address                    | 123 Main St, Anytown     |
| `priority_number`     | Priority level (numeric)            | 2                        |
| `call_taker`          | Name of call taker                  | John Smith               |
| `call_reception`      | Time call was received              | 2024-03-15 14:29:50      |
| `dispatcher`          | Dispatcher name                     | Sarah Johnson            |
| `queue_time`          | Time call was queued (seconds)      | 50                       |
| `dispatch_time`       | Time units dispatched (seconds)     | 100                      |
| `phone_time`          | Time on phone (seconds)             | 150                      |
| `ack_time`            | Time dispatch acknowledged (secs)   | 20                       |
| `enroute_time`        | Time units en route (seconds)       | 600                      |
| `on_scene_time`       | Time units on scene (seconds)       | 3600                     |
| `process_time`        | Processing time (seconds)           | 40                       |
| `total_time`          | Total call time (seconds)           | 70                       |
| `time_call_queued`    | Timestamp call queued               | 2024-03-15 14:30:00      |
| `time_call_dispatched`| Timestamp call dispatched           | 2024-03-15 14:30:10      |
| `time_call_acknowledged`| Timestamp dispatch acknowledged   | 2024-03-15 14:30:20      |
| `time_call_disconnected`| Timestamp call disconnected       | 2024-03-15 14:32:00      |
| `time_unit_enroute`   | Timestamp units en route            | 2024-03-15 14:30:30      |
| `time_call_closed`    | Timestamp call closed               | 2024-03-15 14:33:00      |
| `disposition`         | Final outcome                       | Resolved                 |

## API Reference

### Core Modules

- `main.py` - Application entry point
- `synth911gen.py` - Core data generation engine
- `synthgui.py` - Tkinter GUI interface
- `synthgui_headless.py` - Command-line and interactive interfaces
- `tui.py` - Text-based user interface (TUI)
- `webgui.py` - Flask web interface
- `shared/constants.py` - Shared configuration and constants
- `test_tui_and_gen.py` - Test script for TUI and generator

### Key Functions

```python
# Generate data programmatically
from synth911gen import generate_synthetic_data

data = generate_synthetic_data(
    num_records=1000,
    start_date="2024-01-01",
    end_date="2024-12-31",
    locale="en_US",
    agencies=["LAW", "FIRE", "EMS"]
)
```

## Development

### Project Structure

```python
synth911gen2/
├── main.py                 # Main entry point
├── synth911gen.py         # Core data generation
├── synthgui.py            # Tkinter GUI
├── synthgui_headless.py   # CLI interface
├── tui.py                 # Text-based user interface (TUI)
├── webgui.py              # Web interface
├── test_tui_and_gen.py    # TUI and generator test script
├── shared/
│   ├── __init__.py
│   └── constants.py       # Shared constants
├── data/                  # Sample data files
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project configuration
└── README.md             # This file
```

### Running Tests

```bash
# Run all tests
pytest

# Run TUI and generator tests
python test_tui_and_gen.py

# Run with coverage
pytest --cov=synth911gen2
```

### Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type checking
ty .
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add type hints to all functions
- Include docstrings for all public functions
- Write tests for new features
- Update documentation as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Issues**: Report bugs and feature requests on GitHub
- **Documentation**: See the `/docs` directory for detailed documentation
- **Examples**: Check the `/examples` directory for usage examples

## Related Projects

- [Faker](https://github.com/joke2k/faker) - Python library for generating fake data
- [Polars](https://pola.rs/) - Blazingly fast DataFrames library for Rust and Python
- [Flask](https://flask.palletsprojects.com/) - Web framework for the web interface
- [Fireduck](https://github.com/tonybaloney/fireduck) - Fast CSV/Parquet/Feather/Arrow file reader for Python
- [uv](https://github.com/astral-sh/uv) - Extremely fast Python package installer and resolver
- [ruff](https://github.com/astral-sh/ruff) - Extremely fast Python linter and code formatter
- [Textual](https://github.com/Textualize/textual) - Modern TUI (Text User Interface) framework for Python

## Documentation

The following documentation files are available for Synth911Gen2:

- [Architecture Overview](docs/architecture.md)
- [Architecture Decision Records (ADR)](docs/adr-0001-initial-architecture.md)
- [Onboarding Guide](docs/onboarding.md)
- [Deployment Guide](docs/deployment.md)
- [Data Security](docs/data-security.md)
- [Dependencies](docs/dependencies.md)
- [Entity Relationship Diagram](docs/er-diagram.md)

These documents are auto-generated and should be reviewed for accuracy and completeness. See the `/docs` directory for additional guides, API references, and examples.

---

**Note**: This tool generates synthetic data for testing and development purposes only. Do not use generated data in production systems or for any real emergency response activities.
