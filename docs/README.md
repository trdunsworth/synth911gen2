# Synth911Gen2 Documentation

Welcome to the comprehensive documentation for Synth911Gen2, a synthetic 911 dispatch data generator.

> **For a project overview, installation, and usage instructions, see the main [`README.md`](../README.md) in the project root.**

## Project Overview

Synth911Gen2 is a Python application for generating realistic synthetic 911 dispatch data for testing, training, and development. It supports GUI, CLI, TUI, and web interfaces, and produces anonymized data with realistic statistical patterns.

## Quick Start

- See [Installation Guide](guides/installation.md) for setup
- See [Quick Start Guide](guides/quickstart.md) for first steps
- For interface usage, see [GUI Usage](guides/gui-usage.md) or [Command Line Usage](guides/cli-usage.md)

## 📚 Documentation Structure

### 🚀 Getting Started

- **[Installation Guide](guides/installation.md)** - Complete setup instructions
- **[Quick Start Guide](guides/quickstart.md)** - Get up and running in minutes
- **[Configuration Guide](guides/configuration.md)** - Configure the application

### 📖 User Guides

- **[GUI Usage](guides/gui-usage.md)** - Using the graphical interface
- **[Command Line Usage](guides/cli-usage.md)** - Command-line interface guide
- **[Interactive Mode](guides/interactive-mode.md)** - Step-by-step interactive mode
- **[Web Interface](guides/web-interface.md)** - Using the Flask web GUI

### 🧪 Examples

- **[Distribution Analysis Example](examples/distribution_analysis.md)** - Analyze numeric columns and fit distributions

### 🔧 API Reference

- **[Core API](api/core.md)** - Main data generation functions
- **[GUI API](api/gui.md)** - Tkinter interface components
- **[CLI API](api/cli.md)** - Command-line interface functions
- **[Web API](api/web.md)** - Flask web interface endpoints
- **[Constants](api/constants.md)** - Shared configuration constants

### 💡 Examples

- **[Basic Examples](examples/basic.md)** - Simple usage examples
- **[Advanced Examples](examples/advanced.md)** - Complex scenarios
- **[Integration Examples](examples/integration.md)** - Third-party integrations
- **[Customization Examples](examples/customization.md)** - Extending functionality

### 🧪 Development

- **[Development Setup](guides/development.md)** - Setting up for development
- **[Testing Guide](guides/testing.md)** - Running tests and quality checks
- **[Contributing Guide](guides/contributing.md)** - How to contribute

## 🎯 Quick Navigation

### For New Users

1. Start with [Installation Guide](guides/installation.md)
2. Follow the [Quick Start Guide](guides/quickstart.md)
3. Choose your interface: [GUI](guides/gui-usage.md) or [CLI](guides/cli-usage.md)

### For Developers

1. Review [Development Setup](guides/development.md)
2. Check [Core API](api/core.md) for integration
3. See [Examples](examples/) for usage patterns

### For System Administrators

1. [Installation Guide](guides/installation.md) for deployment
2. [Configuration Guide](guides/configuration.md) for customization
3. [Web Interface](guides/web-interface.md) for server deployment

## 🔍 Search Documentation

Use your browser's search function (Ctrl+F) to find specific topics within each document.

## 📝 Documentation Updates

This documentation is maintained alongside the codebase. If you find any issues or have suggestions for improvement, please:

1. Check if the issue is already reported
2. Create a new issue with the "documentation" label
3. Submit a pull request with your improvements

## 🆘 Getting Help

- **GitHub Issues**: Report bugs and request features
- **Discussions**: Ask questions and share ideas
- **Examples**: Check the examples directory for working code
- **API Reference**: Detailed function documentation

## ⚙️ Configuration Options

- **Custom Agency Probabilities**: You can specify the probability distribution for selected agencies in CLI, GUI, and Web interfaces. See [CLI Usage](guides/cli-usage.md) and [Quick Start](guides/quickstart.md) for details.
- **RESCUE Agency**: The RESCUE agency is now fully supported in all interfaces, with realistic problems and priorities.

---

**Last Updated**: July 2025
**Version**: 0.7.0
