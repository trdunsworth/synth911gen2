### Synth911Gen2 - Architecture Documentation (Arc42)

**Version:** 0.5.0
**Date:** June 2024
**Authors:** Tony Dunsworth, Contributors
**Status:** Draft

---

## 1. Introduction and Goals

Synth911Gen2 is a synthetic 911 dispatch data generator designed to create realistic emergency dispatch datasets for testing, analytics, and training. It supports multiple agencies, locales, and output formats, and provides both GUI and CLI interfaces.

### 1.1 Requirements Overview

- Generate synthetic 911 dispatch records with realistic patterns
- Support multiple agencies (LAW, FIRE, EMS, RESCUE)
- Allow configuration of date ranges, locales, and agency probabilities
- Provide GUI, CLI, and web interfaces
- Output to CSV, JSON, XLSX

#### Key Functional Requirements

- **Data Generation**: Create realistic incident records
- **Multi-Interface**: GUI, CLI, and web support
- **Configurable**: Agencies, locales, date ranges, output formats

### 1.2 Quality Goals

| Priority | Quality Goal | Motivation |
|----------|--------------|------------|
| 1 | Realism of Data | Enable realistic testing and analytics |
| 2 | Usability | Easy to use for both technical and non-technical users |
| 3 | Extensibility | Support new agencies, locales, and output formats |

### 1.3 Stakeholders

| Role/Name | Contact | Expectations |
|-----------|---------|--------------|
| Maintainer | tony.dunsworth@example.com | Reliable, well-documented tool |
| Data Scientists | - | Realistic, configurable datasets |
| Developers | - | Extensible, testable codebase |

## 2. Architecture Constraints

- Python 3.11+
- Polars, Faker, Flask dependencies
- Cross-platform (Windows, macOS, Linux)

### 2.1 Technical Constraints

| Constraint | Background/motivation |
|------------|----------------------|
| Python 3.11+ | Leverage latest language features |
| Polars/Faker | Efficient data generation |

### 2.2 Organizational Constraints

| Constraint | Background/motivation |
|------------|----------------------|
| Open Source | Community contributions |

### 2.3 Conventions

- PEP8 code style
- Docstrings for public APIs

## 3. System Scope and Context

Synth911Gen2 generates synthetic 911 dispatch data for use in analytics, testing, and training. It interacts with users via GUI, CLI, and web interfaces, and outputs data files for downstream use.

### 3.1 Business Context

| Partner | Input | Output |
|---------|-------|--------|
| User | Configuration | Synthetic data files |
| Downstream Tools | Data files | Analytics, ML, etc. |

### 3.2 Technical Context

- GUI: Tkinter
- CLI: argparse
- Web: Flask
- Data: Polars DataFrames, CSV/JSON/XLSX output

## 4. Solution Strategy

- Modular Python codebase
- Shared constants and validation logic
- Interface-specific modules (GUI, CLI, Web)
- Use of Faker for realistic data

## 5. Building Block View

- main.py: Entry point
- synth911gen.py: Core data generation logic
- synth911.py: Legacy/compatibility
- synthgui.py: GUI
- webgui.py: Web interface
- shared/constants.py: Shared config and validation

## 6. Runtime View

- User launches via GUI, CLI, or web
- Configuration is parsed
- Data is generated and written to file

## 7. Deployment View

- Local execution (Windows, macOS, Linux)
- Optional Docker deployment for web interface

## 8. Cross-cutting Concepts

- Logging, error handling, extensibility

## 9. Design Decisions

- Use of Polars and Faker for performance and realism
- Modular design for extensibility

## 10. Quality Requirements

- Unit tests for core logic
- Linting and code style enforcement

---

*This document is auto-generated and should be reviewed for accuracy and completeness.* 