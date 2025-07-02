# Development Setup Guide

This guide helps developers set up a development environment for contributing to Synth911Gen2.

## 🛠️ Prerequisites

### Required Software

- **Python**: 3.11 or higher
- **Git**: Latest version
- **Code Editor**: VS Code, PyCharm, or similar
- **Terminal**: Command line access

### Recommended Tools

- **uv**: Modern Python package manager
- **pre-commit**: Git hooks for code quality
- **Docker**: For containerized development
- **Make**: For build automation

## 🚀 Development Environment Setup

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/yourusername/synth911gen2.git
cd synth911gen2

# Add upstream remote (if forking)
git remote add upstream https://github.com/original-owner/synth911gen2.git
```

### Step 2: Create Virtual Environment

```bash
# Using venv (built-in)
python -m venv synth911_dev
source synth911_dev/bin/activate  # On Windows: synth911_dev\Scripts\activate

# Using uv (recommended)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # if available

# Or using uv
uv sync --dev
```

### Step 4: Install Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Install git hooks
pre-commit install
```

## 🔧 Development Tools Configuration

### VS Code Configuration

Create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "./synth911_dev/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [
        "tests"
    ],
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

### PyCharm Configuration

1. Open project in PyCharm
2. Set project interpreter to virtual environment
3. Configure code style (PEP 8)
4. Enable auto-imports and formatting

### Pre-commit Configuration

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.270
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

## 🧪 Testing Setup

### Install Testing Dependencies

```bash
pip install pytest pytest-cov pytest-mock pytest-asyncio
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=synth911gen2 --cov-report=html

# Run specific test file
pytest tests/test_synth911gen.py

# Run with verbose output
pytest -v

# Run tests in parallel
pytest -n auto
```

### Test Structure

```
tests/
├── __init__.py
├── conftest.py              # Pytest configuration
├── test_synth911gen.py      # Core functionality tests
├── test_gui.py              # GUI tests
├── test_cli.py              # CLI tests
├── test_web.py              # Web interface tests
└── fixtures/                # Test data fixtures
    ├── sample_data.csv
    └── config.json
```

### Example Test

```python
# tests/test_synth911gen.py
import pytest
import pandas as pd
from synth911gen import generate_synthetic_data

def test_generate_synthetic_data_basic():
    """Test basic data generation."""
    data = generate_synthetic_data(num_records=10)
    
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 10
    assert 'incident_id' in data.columns
    assert 'timestamp' in data.columns

def test_generate_synthetic_data_validation():
    """Test parameter validation."""
    with pytest.raises(ValueError):
        generate_synthetic_data(num_records=-1)
    
    with pytest.raises(ValueError):
        generate_synthetic_data(start_date="invalid-date")

@pytest.mark.parametrize("locale", ["en_US", "fr_FR", "es_ES"])
def test_generate_synthetic_data_locales(locale):
    """Test data generation with different locales."""
    data = generate_synthetic_data(num_records=5, locale=locale)
    assert len(data) == 5
```

## 🔍 Code Quality Tools

### Ruff (Linting and Formatting)

```bash
# Install ruff
pip install ruff

# Check code
ruff check .

# Format code
ruff format .

# Fix issues automatically
ruff check --fix .
```

### Type Checking

```bash
# Install mypy
pip install mypy

# Run type checking
mypy synth911gen2/

# Run with strict mode
mypy --strict synth911gen2/
```

### Security Scanning

```bash
# Install bandit
pip install bandit

# Run security scan
bandit -r synth911gen2/
```

## 📦 Building and Packaging

### Update Version

```bash
# Update version in pyproject.toml
# Update version in __init__.py
# Update CHANGELOG.md
```

### Build Package

```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Check package
twine check dist/*
```

### Local Installation

```bash
# Install in development mode
pip install -e .

# Test installation
python -c "import synth911gen2; print(synth911gen2.__version__)"
```

## 🐳 Docker Development

### Development Dockerfile

```dockerfile
# Dockerfile.dev
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt requirements-dev.txt ./

# Install Python dependencies
RUN pip install -r requirements.txt -r requirements-dev.txt

# Copy source code
COPY . .

# Install in development mode
RUN pip install -e .

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "main.py"]
```

### Docker Compose for Development

```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  synth911-dev:
    build:
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - .:/app
      - /app/__pycache__
    ports:
      - "5000:5000"  # For web interface
    environment:
      - PYTHONPATH=/app
      - PYTHONUNBUFFERED=1
    command: ["python", "main.py", "--cli", "-n", "100"]
```

## 🔄 Development Workflow

### Feature Development

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make Changes**
   - Write code
   - Add tests
   - Update documentation

3. **Run Quality Checks**
   ```bash
   # Run tests
   pytest
   
   # Run linting
   ruff check .
   
   # Run type checking
   mypy synth911gen2/
   ```

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

5. **Push and Create PR**
   ```bash
   git push origin feature/new-feature
   # Create pull request on GitHub
   ```

### Bug Fix Workflow

1. **Create Bug Fix Branch**
   ```bash
   git checkout -b fix/bug-description
   ```

2. **Write Test**
   ```python
   def test_bug_fix():
       """Test that the bug is fixed."""
       # Write test that fails before fix
       pass
   ```

3. **Fix Bug**
   - Implement the fix
   - Ensure test passes

4. **Update Documentation**
   - Update relevant docs
   - Add to CHANGELOG.md

5. **Commit and Push**
   ```bash
   git commit -m "fix: description of bug fix"
   git push origin fix/bug-description
   ```

## 📚 Documentation Development

### Building Documentation

```bash
# Install documentation tools
pip install mkdocs mkdocs-material

# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

### Documentation Structure

```
docs/
├── index.md
├── guides/
│   ├── installation.md
│   ├── quickstart.md
│   └── development.md
├── api/
│   ├── core.md
│   ├── gui.md
│   └── cli.md
└── examples/
    ├── basic.md
    └── advanced.md
```

## 🚀 Performance Testing

### Benchmark Scripts

```python
# benchmarks/performance_test.py
import time
import psutil
from synth911gen import generate_synthetic_data

def benchmark_generation():
    """Benchmark data generation performance."""
    
    # Test different record counts
    record_counts = [100, 1000, 10000, 50000]
    
    for count in record_counts:
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
        
        data = generate_synthetic_data(num_records=count)
        
        end_time = time.time()
        end_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
        
        duration = end_time - start_time
        memory_used = end_memory - start_memory
        
        print(f"Records: {count:6d}, Time: {duration:6.2f}s, Memory: {memory_used:6.1f}MB")

if __name__ == "__main__":
    benchmark_generation()
```

## 🔧 Debugging

### Debug Configuration

Create `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        },
        {
            "name": "Python: Main Module",
            "type": "python",
            "request": "launch",
            "module": "main",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

### Logging Configuration

```python
# logging_config.py
import logging

def setup_logging(level=logging.INFO):
    """Setup logging configuration for development."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('synth911gen2.log'),
            logging.StreamHandler()
        ]
    )
```

## 📋 Development Checklist

Before submitting a pull request:

- [ ] Code follows PEP 8 style guidelines
- [ ] All tests pass
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Type hints are added
- [ ] No security issues (bandit check)
- [ ] Performance is acceptable
- [ ] CHANGELOG.md is updated
- [ ] Version is updated

## 🆘 Getting Help

### Development Resources

- **GitHub Issues**: Report bugs and request features
- **GitHub Discussions**: Ask questions and share ideas
- **Code Review**: Request code reviews from maintainers
- **Documentation**: Check existing documentation

### Common Issues

1. **Import Errors**: Ensure virtual environment is activated
2. **Test Failures**: Check test data and dependencies
3. **Performance Issues**: Use profiling tools
4. **Memory Issues**: Monitor memory usage with large datasets

## 📚 Related Documentation

- [Architecture Overview](../architecture.md)
- [Architecture Decision Records (ADR)](../adr-0001-initial-architecture.md)
- [Deployment Guide](../deployment.md)
- [Data Security](../data-security.md)
- [Dependencies](../dependencies.md)

For more, see the [README](../../README.md) and the `/docs` directory.

---

**Next Steps**: 
- Read the [Contributing Guide](contributing.md) for contribution guidelines
- Check the [Testing Guide](testing.md) for detailed testing information
- Review the [API Documentation](../api/) for integration details 