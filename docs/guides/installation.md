# Installation Guide

This guide covers all methods for installing Synth911Gen2 on different platforms and environments.

## 📋 Prerequisites

### System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+, CentOS 7+)
- **Python**: 3.11 or higher
- **Memory**: Minimum 4GB RAM (8GB recommended for large datasets)
- **Storage**: 1GB free space for installation, plus space for generated data

### Python Installation

If you don't have Python 3.11+ installed:

#### Windows
```bash
# Download from python.org or use winget
winget install Python.Python.3.11

# Or use Chocolatey
choco install python311
```

#### macOS
```bash
# Using Homebrew
brew install python@3.11

# Or download from python.org
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3.11-pip python3.11-venv
```

#### Linux (CentOS/RHEL/Fedora)
```bash
# Fedora
sudo dnf install python3.11 python3.11-pip

# CentOS/RHEL
sudo yum install python3.11 python3.11-pip
```

## 🚀 Installation Methods

### Method 1: Direct Installation (Recommended)

#### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/synth911gen2.git
cd synth911gen2
```

#### Step 2: Install Dependencies

**Using pip:**
```bash
pip install -r requirements.txt
```

**Using uv (recommended):**
```bash
# Install uv if not already installed
pip install uv

# Install dependencies
uv sync
```

**Using conda:**
```bash
conda create -n synth911 python=3.11
conda activate synth911
pip install -r requirements.txt
```

#### Step 3: Verify Installation
```bash
python main.py --help
```

### Method 2: Virtual Environment Installation

#### Step 1: Create Virtual Environment
```bash
# Create virtual environment
python -m venv synth911_env

# Activate virtual environment
# Windows
synth911_env\Scripts\activate

# macOS/Linux
source synth911_env/bin/activate
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 3: Verify Installation
```bash
python main.py --help
```

### Method 3: Development Installation

For developers who want to modify the code:

```bash
# Clone repository
git clone https://github.com/yourusername/synth911gen2.git
cd synth911gen2

# Create virtual environment
python -m venv synth911_dev
source synth911_dev/bin/activate  # or synth911_dev\Scripts\activate on Windows

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt  # if available
```

## 🔧 Platform-Specific Instructions

### Windows Installation

#### GUI Dependencies
The GUI requires Tkinter, which is usually included with Python on Windows. If you encounter issues:

```bash
# Reinstall Python with Tkinter
# Download from python.org and ensure "tcl/tk and IDLE" is selected
```

#### Common Issues
- **Path Issues**: Ensure Python is added to PATH during installation
- **Permission Issues**: Run as administrator if needed
- **Antivirus**: Add exceptions for the project directory

### macOS Installation

#### GUI Dependencies
```bash
# Install Xcode command line tools (if not already installed)
xcode-select --install

# For Tkinter issues, install Python via Homebrew
brew install python-tk@3.11
```

#### Common Issues
- **Permission Issues**: Use `sudo` if needed for system-wide installation
- **Python Version**: Ensure you're using the correct Python version

### Linux Installation

#### GUI Dependencies
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# CentOS/RHEL/Fedora
sudo dnf install python3-tkinter  # or yum for older versions
```

#### X11 Issues
If you encounter X11 display issues:

```bash
# Set display
export DISPLAY=:0

# Or run in headless mode
python main.py --cli
```

## 🐳 Docker Installation

### Using Docker

```bash
# Build the image
docker build -t synth911gen2 .

# Run the container
docker run -it --rm -v $(pwd)/output:/app/output synth911gen2

# Run with GUI (requires X11 forwarding on Linux)
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd)/output:/app/output synth911gen2
```

### Using Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  synth911:
    build: .
    volumes:
      - ./output:/app/output
    ports:
      - "5000:5000"  # For web interface
```

## 🔍 Verification

### Test Basic Functionality
```bash
# Test command-line interface
python main.py --cli -n 10 -s 2024-01-01 -e 2024-01-02

# Test interactive mode
python main.py --interactive

# Test web interface (if available)
python webgui.py
```

### Check Dependencies
```bash
# Verify all packages are installed
python -c "import polars, numpy, faker, flask; print('All dependencies installed successfully')"
```

## 🛠️ Troubleshooting

### Common Issues

#### Import Errors
```bash
# Error: No module named 'pandas'
pip install pandas

# Error: No module named 'tkinter'
# Windows: Reinstall Python with Tkinter
# Linux: sudo apt install python3-tk
# macOS: brew install python-tk@3.11
```

#### Permission Errors
```bash
# Windows: Run as administrator
# Linux/macOS: Use sudo or fix permissions
sudo chown -R $USER:$USER /path/to/project
```

#### GUI Not Working
```bash
# Try headless mode
python main.py --cli

# Check display settings
echo $DISPLAY  # Should show :0 or similar
```

#### Memory Issues
```bash
# Reduce number of records for testing
python main.py --cli -n 1000

# Check available memory
free -h  # Linux
top       # macOS
```

### Getting Help

1. **Check the logs**: Look for error messages in the terminal
2. **Verify Python version**: `python --version`
3. **Check dependencies**: `pip list`
4. **Search issues**: Check GitHub issues for similar problems
5. **Create issue**: Report new problems with system details

## 📦 Uninstallation

### Remove Virtual Environment
```bash
# Deactivate environment
deactivate

# Remove directory
rm -rf synth911_env
```

### Remove Dependencies
```bash
pip uninstall -r requirements.txt
```

### Remove Project
```bash
# Remove project directory
rm -rf synth911gen2
```

## 🔄 Updating

### Update from Git
```bash
git pull origin main
pip install -r requirements.txt
```

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

## 📚 Related Documentation

- [Deployment Guide](../deployment.md)
- [Data Security](../data-security.md)
- [Onboarding Guide](../onboarding.md)
- [Dependencies](../dependencies.md)

For more, see the [README](../../README.md) and the `/docs` directory.

---

**Next Steps**: After installation, proceed to the [Quick Start Guide](quickstart.md) to begin using Synth911Gen2. 