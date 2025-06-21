# Constants API Reference

This document provides reference for all shared constants and configuration values used throughout Synth911Gen2.

## 📋 Overview

The constants module (`shared/constants.py`) contains configuration values, supported options, and validation functions used across multiple modules in the application.

## 🔧 Core Constants

### `DEFAULT_LOCALE`

The default locale used for data generation.

```python
DEFAULT_LOCALE = "en_US"
```

**Type**: `str`  
**Description**: Default Faker locale for generating localized data  
**Usage**: Used when no locale is specified by the user

### `SUPPORTED_LOCALES`

List of all supported locales for data generation.

```python
SUPPORTED_LOCALES = [
    "en_US",  # American English
    "en_GB",  # British English
    "fr_FR",  # French
    "de_DE",  # German
    "es_ES",  # Spanish
    "it_IT",  # Italian
    "pt_BR",  # Brazilian Portuguese
    "nl_NL",  # Dutch
    "pl_PL",  # Polish
    "ru_RU",  # Russian
    "ja_JP",  # Japanese
    "ko_KR",  # Korean
    "zh_CN",  # Chinese (Simplified)
    "ar_SA",  # Arabic
]
```

**Type**: `List[str]`  
**Description**: All locales supported by the application  
**Usage**: Used for validation and locale selection

## 🏢 Agency Configuration

### `DEFAULT_AGENCIES`

Default emergency agencies included in data generation.

```python
DEFAULT_AGENCIES = [
    "LAW",    # Law enforcement
    "FIRE",   # Fire department
    "EMS",    # Emergency medical services
    "RESCUE", # Search and rescue
]
```

**Type**: `List[str]`  
**Description**: Default agencies included when none are specified  
**Usage**: Used as fallback when user doesn't specify agencies

### `AGENCY_DESCRIPTIONS`

Human-readable descriptions for each agency type.

```python
AGENCY_DESCRIPTIONS = {
    "LAW": "Law Enforcement",
    "FIRE": "Fire Department", 
    "EMS": "Emergency Medical Services",
    "RESCUE": "Search and Rescue",
}
```

**Type**: `Dict[str, str]`  
**Description**: Mapping of agency codes to display names  
**Usage**: Used in GUI and documentation

## 🚨 Incident Type Configuration

### `INCIDENT_TYPES`

Mapping of agencies to their associated incident types.

```python
INCIDENT_TYPES = {
    "LAW": [
        "Traffic Accident",
        "Domestic Disturbance", 
        "Burglary",
        "Assault",
        "Suspicious Activity",
        "Traffic Violation",
        "Public Intoxication",
        "Vandalism"
    ],
    "FIRE": [
        "Structure Fire",
        "Vehicle Fire",
        "Brush Fire", 
        "Medical Emergency",
        "Hazardous Materials",
        "Gas Leak",
        "Electrical Fire",
        "Alarm Activation"
    ],
    "EMS": [
        "Medical Emergency",
        "Trauma",
        "Cardiac Arrest",
        "Difficulty Breathing",
        "Unconscious Person",
        "Chest Pain",
        "Stroke",
        "Seizure"
    ],
    "RESCUE": [
        "Water Rescue",
        "Mountain Rescue",
        "Vehicle Extrication",
        "Confined Space Rescue",
        "High Angle Rescue",
        "Search and Rescue",
        "Technical Rescue"
    ]
}
```

**Type**: `Dict[str, List[str]]`  
**Description**: Incident types associated with each agency  
**Usage**: Used to generate realistic incident data

### `PRIORITY_LEVELS`

Available priority levels for incidents.

```python
PRIORITY_LEVELS = [1, 2, 3, 4, 5]
```

**Type**: `List[int]`  
**Description**: Valid priority levels (1 = highest, 5 = lowest)  
**Usage**: Used for priority assignment and validation

### `PRIORITY_DESCRIPTIONS`

Human-readable descriptions for priority levels.

```python
PRIORITY_DESCRIPTIONS = {
    1: "Immediate - Life threatening",
    2: "High - Serious injury/illness", 
    3: "Medium - Non-life threatening",
    4: "Low - Minor injury/illness",
    5: "Non-emergency - Information/assistance"
}
```

**Type**: `Dict[int, str]`  
**Description**: Description of each priority level  
**Usage**: Used in GUI and documentation

## 📅 Date and Time Configuration

### `DEFAULT_DATE_RANGE`

Default date range for data generation.

```python
DEFAULT_START_DATE = "2024-01-01"
DEFAULT_END_DATE = "2024-12-31"
```

**Type**: `str`  
**Description**: Default start and end dates in YYYY-MM-DD format  
**Usage**: Used when no date range is specified

### `TIME_PATTERNS`

Time-based patterns for realistic data generation.

```python
TIME_PATTERNS = {
    "peak_hours": [8, 9, 17, 18, 19],  # Peak call hours
    "quiet_hours": [2, 3, 4, 5],       # Quiet hours
    "weekend_multiplier": 1.2,          # Weekend call volume multiplier
    "holiday_multiplier": 0.8           # Holiday call volume multiplier
}
```

**Type**: `Dict[str, Any]`  
**Description**: Time patterns for realistic call distribution  
**Usage**: Used in data generation algorithms

## 🔧 Application Configuration

### `DEFAULT_SETTINGS`

Default application settings.

```python
DEFAULT_SETTINGS = {
    "num_records": 10000,
    "num_names": 8,
    "output_file": "computer_aided_dispatch.csv",
    "debug": False,
    "verbose": False
}
```

**Type**: `Dict[str, Any]`  
**Description**: Default values for application settings  
**Usage**: Used as fallback when settings aren't specified

### `FILE_EXTENSIONS`

Supported file extensions for output.

```python
FILE_EXTENSIONS = [".csv", ".json", ".xlsx"]
```

**Type**: `List[str]`  
**Description**: Supported output file formats  
**Usage**: Used for file validation and GUI file dialogs

## 🔍 Validation Functions

### `validate_locale(locale: str) -> bool`

Validate if a locale is supported.

```python
def validate_locale(locale: str) -> bool:
    """
    Validate if a given locale is supported.
    
    Args:
        locale (str): The locale string to validate
        
    Returns:
        bool: True if the locale is supported, False otherwise
    """
    return locale in SUPPORTED_LOCALES
```

**Parameters**:
- `locale` (str): Locale string to validate

**Returns**: `bool` - True if supported, False otherwise

**Usage**: Used to validate user input and configuration

### `validate_agency(agency: str) -> bool`

Validate if an agency is supported.

```python
def validate_agency(agency: str) -> bool:
    """
    Validate if a given agency is supported.
    
    Args:
        agency (str): The agency string to validate
        
    Returns:
        bool: True if the agency is supported, False otherwise
    """
    return agency in DEFAULT_AGENCIES
```

**Parameters**:
- `agency` (str): Agency string to validate

**Returns**: `bool` - True if supported, False otherwise

**Usage**: Used to validate user input and configuration

### `validate_priority(priority: int) -> bool`

Validate if a priority level is valid.

```python
def validate_priority(priority: int) -> bool:
    """
    Validate if a given priority level is valid.
    
    Args:
        priority (int): The priority level to validate
        
    Returns:
        bool: True if the priority is valid, False otherwise
    """
    return priority in PRIORITY_LEVELS
```

**Parameters**:
- `priority` (int): Priority level to validate

**Returns**: `bool` - True if valid, False otherwise

**Usage**: Used to validate generated data and user input

## 📊 Data Generation Constants

### `INCIDENT_ID_FORMAT`

Format string for generating incident IDs.

```python
INCIDENT_ID_FORMAT = "INC-{year}-{number:06d}"
```

**Type**: `str`  
**Description**: Format string for incident ID generation  
**Usage**: Used in data generation to create unique incident IDs

### `PHONE_FORMAT`

Format string for phone number generation.

```python
PHONE_FORMAT = "({area_code}) {prefix}-{line_number}"
```

**Type**: `str`  
**Description**: Format string for phone number generation  
**Usage**: Used in data generation for consistent phone formatting

### `ADDRESS_FORMAT`

Format string for address generation.

```python
ADDRESS_FORMAT = "{street_number} {street_name}, {city}, {state}"
```

**Type**: `str`  
**Description**: Format string for address generation  
**Usage**: Used in data generation for consistent address formatting

## 🔧 Error Messages

### `ERROR_MESSAGES`

Standardized error messages used throughout the application.

```python
ERROR_MESSAGES = {
    "invalid_locale": "Invalid locale '{locale}'. Use --list-locales to see available options.",
    "invalid_agency": "Invalid agency '{agency}'. Valid agencies: {valid_agencies}",
    "invalid_priority": "Invalid priority '{priority}'. Must be between 1 and 5.",
    "invalid_date": "Invalid date '{date}'. Use YYYY-MM-DD format.",
    "invalid_records": "Number of records must be a positive integer.",
    "file_write_error": "Cannot write to file '{file}'. Check permissions.",
    "memory_error": "Insufficient memory for {records} records. Try a smaller number."
}
```

**Type**: `Dict[str, str]`  
**Description**: Standardized error messages with placeholders  
**Usage**: Used for consistent error reporting

## 📈 Performance Constants

### `PERFORMANCE_LIMITS`

Performance-related limits and thresholds.

```python
PERFORMANCE_LIMITS = {
    "max_records_per_chunk": 50000,
    "memory_warning_threshold": 100000,
    "timeout_seconds": 300,
    "max_concurrent_processes": 4
}
```

**Type**: `Dict[str, Any]`  
**Description**: Performance limits and thresholds  
**Usage**: Used for performance optimization and warnings

## 🔒 Security Constants

### `SECURITY_SETTINGS`

Security-related configuration values.

```python
SECURITY_SETTINGS = {
    "max_file_size_mb": 100,
    "allowed_file_extensions": [".csv", ".json", ".xlsx"],
    "sanitize_input": True,
    "validate_output_path": True
}
```

**Type**: `Dict[str, Any]`  
**Description**: Security settings and restrictions  
**Usage**: Used for input validation and security checks

## 📝 Usage Examples

### Basic Usage

```python
from shared.constants import (
    DEFAULT_LOCALE, 
    SUPPORTED_LOCALES, 
    validate_locale,
    INCIDENT_TYPES
)

# Use default locale
print(f"Default locale: {DEFAULT_LOCALE}")

# Check if locale is supported
if validate_locale("fr_FR"):
    print("French locale is supported")

# Get incident types for law enforcement
law_incidents = INCIDENT_TYPES["LAW"]
print(f"Law enforcement incidents: {law_incidents}")
```

### Configuration Validation

```python
from shared.constants import (
    validate_locale,
    validate_agency,
    validate_priority,
    ERROR_MESSAGES
)

def validate_config(config):
    """Validate configuration dictionary."""
    errors = []
    
    # Validate locale
    if not validate_locale(config.get("locale", "en_US")):
        errors.append(ERROR_MESSAGES["invalid_locale"].format(
            locale=config.get("locale")
        ))
    
    # Validate agencies
    agencies = config.get("agencies", [])
    for agency in agencies:
        if not validate_agency(agency):
            errors.append(ERROR_MESSAGES["invalid_agency"].format(
                agency=agency,
                valid_agencies=", ".join(DEFAULT_AGENCIES)
            ))
    
    return errors
```

### Data Generation Configuration

```python
from shared.constants import (
    DEFAULT_SETTINGS,
    INCIDENT_TYPES,
    PRIORITY_LEVELS
)

def get_generation_config(user_config):
    """Merge user configuration with defaults."""
    config = DEFAULT_SETTINGS.copy()
    config.update(user_config)
    
    # Ensure agencies have incident types
    if "agencies" in config:
        for agency in config["agencies"]:
            if agency not in INCIDENT_TYPES:
                raise ValueError(f"No incident types defined for agency: {agency}")
    
    return config
```

## 🔄 Constants Updates

### Adding New Locales

To add a new locale:

1. Add to `SUPPORTED_LOCALES`:
   ```python
   SUPPORTED_LOCALES.append("pt_PT")  # Portuguese (Portugal)
   ```

2. Update locale descriptions if needed
3. Test with Faker to ensure compatibility

### Adding New Agencies

To add a new agency:

1. Add to `DEFAULT_AGENCIES`:
   ```python
   DEFAULT_AGENCIES.append("BOMB")  # Bomb squad
   ```

2. Add to `AGENCY_DESCRIPTIONS`:
   ```python
   AGENCY_DESCRIPTIONS["BOMB"] = "Bomb Squad"
   ```

3. Add incident types to `INCIDENT_TYPES`:
   ```python
   INCIDENT_TYPES["BOMB"] = [
       "Suspicious Package",
       "Explosive Device",
       "Bomb Threat"
   ]
   ```

### Modifying Default Settings

To change default settings:

```python
# Update default number of records
DEFAULT_SETTINGS["num_records"] = 5000

# Add new setting
DEFAULT_SETTINGS["enable_logging"] = True
```

---

**See Also**: 
- [Core API](core.md) - Main data generation functions
- [GUI API](gui.md) - Tkinter interface components  
- [CLI API](cli.md) - Command-line interface functions