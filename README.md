# Synth911Gen2 - Synthetic 911 Dispatch Data Generator

A comprehensive Python application for generating realistic synthetic 911 dispatch data for testing, training, and development purposes. This tool creates anonymized emergency dispatch records that maintain statistical patterns and relationships found in real emergency data.

## 🚨 Features

- **Multi-Interface Support**: GUI (Tkinter) and command-line interfaces
- **Multi-Language Support**: Generate data in 14+ locales including English, French, German, Spanish, and more
- **Flexible Data Generation**: Customizable number of records, date ranges, and agency types
- **Realistic Data Patterns**: Maintains realistic relationships between emergency types, times, and locations
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Headless Mode**: Perfect for automated data generation and CI/CD pipelines
- **Web Interface**: Optional Flask-based web GUI for remote access

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [GUI Mode](#gui-mode)
  - [Command Line Mode](#command-line-mode)
  - [Interactive Mode](#interactive-mode)
  - [Web Interface](#web-interface)
- [Configuration](#configuration)
- [Data Format](#data-format)
- [API Reference](#api-reference)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Installation

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

## 🚀 Quick Start

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

# Genrate data using uv
uv run main.py --cli -n 12000 -s 2024-01-01 -e 2024-12-31 -l en_GB -a "FIRE,EMS" -0 uv_test.csv
```

### Interactive Mode

```bash
python main.py --interactive
```

## 📖 Usage

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

### Web Interface

For remote access or server deployment:

```bash
python webgui.py
```

Access the web interface at `http://localhost:5000`

## ⚙️ Configuration

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

## 📊 Data Format

Generated data is saved in CSV format with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `incident_id` | Unique incident identifier | INC-2024-001234 |
| `timestamp` | Date and time of incident | 2024-03-15 14:30:22 |
| `caller_name` | Name of person reporting | John Smith |
| `caller_phone` | Phone number | (555) 123-4567 |
| `location` | Incident address | 123 Main St, Anytown, ST |
| `incident_type` | Type of emergency | Medical Emergency |
| `priority` | Priority level (1-5) | 2 |
| `agency` | Responding agency | EMS |
| `dispatcher` | Dispatcher name | Sarah Johnson |
| `status` | Incident status | Dispatched |

## 🔧 API Reference

### Core Modules

- `main.py` - Application entry point
- `synth911gen.py` - Core data generation engine
- `synthgui.py` - Tkinter GUI interface
- `synthgui_headless.py` - Command-line and interactive interfaces
- `webgui.py` - Flask web interface
- `shared/constants.py` - Shared configuration and constants

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

## 🧪 Development

### Project Structure

```
synth911gen2/
├── main.py                 # Main entry point
├── synth911gen.py         # Core data generation
├── synthgui.py            # Tkinter GUI
├── synthgui_headless.py   # CLI interface
├── webgui.py              # Web interface
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

## 🤝 Contributing

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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Report bugs and feature requests on GitHub
- **Documentation**: See the `/docs` directory for detailed documentation
- **Examples**: Check the `/examples` directory for usage examples

## 🔗 Related Projects

- [Faker](https://github.com/joke2k/faker) - Python library for generating fake data
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [Flask](https://flask.palletsprojects.com/) - Web framework for the web interface

---

**Note**: This tool generates synthetic data for testing and development purposes only. Do not use generated data in production systems or for any real emergency response activities.
