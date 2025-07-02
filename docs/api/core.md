# Core API Reference

This document provides detailed API reference for the core data generation functions in Synth911Gen2.

## 📋 Overview

The core API consists of the main data generation engine located in `synth911gen.py`. This module handles the creation of synthetic 911 dispatch records with realistic patterns and relationships.

## 🔧 Main Functions

### `generate_synthetic_data()`

The primary function for generating synthetic 911 dispatch data.

```python
def generate_synthetic_data(
    num_records: int = 10000,
    start_date: str = "2024-01-01",
    end_date: str = "2024-12-31",
    locale: str = "en_US",
    agencies: Optional[List[str]] = None,
    num_names: int = 8,
    output_file: str = "computer_aided_dispatch.csv",
    agency_probabilities: Optional[List[float]] = None
) -> pd.DataFrame:
    """
    Generate synthetic 911 dispatch data.
    
    Args:
        num_records (int): Number of records to generate
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        locale (str): Faker locale for localized data
        agencies (List[str], optional): List of agencies to include
        num_names (int): Number of dispatcher names to generate
        output_file (str): Output CSV file path
        agency_probabilities (List[float], optional): Probabilities for selected agencies (must sum to 1)
        
    Returns:
        pd.DataFrame: Generated synthetic data
        
    Raises:
        ValueError: If parameters are invalid
        IOError: If output file cannot be written
    """
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `num_records` | `int` | `10000` | Number of dispatch records to generate |
| `start_date` | `str` | `"2024-01-01"` | Start date in YYYY-MM-DD format |
| `end_date` | `str` | `"2024-12-31"` | End date in YYYY-MM-DD format |
| `locale` | `str` | `"en_US"` | Faker locale for generating localized data |
| `agencies` | `List[str]` | `None` | List of agencies (LAW, FIRE, EMS, etc.) |
| `num_names` | `int` | `8` | Number of dispatcher names to rotate |
| `output_file` | `str` | `"computer_aided_dispatch.csv"` | Output file path |
| `agency_probabilities` | `List[float]` | `None` | Probabilities for selected agencies (must sum to 1) |

#### Return Value

Returns a pandas DataFrame containing the generated synthetic data with the following columns:

- `call_id`: Unique call identifier
- `agency`: Responding agency
- `event_time`: Date and time of event
- `day_of_year`: Day of the year (1-366)
- `week_no`: ISO week number
- `hour`: Hour of day (0-23)
- `day_night`: Day or night indicator
- `dow`: Day of week (0=Mon, 6=Sun)
- `shift`: Shift name or number
- `shift_part`: Part of shift (e.g., start/end)
- `problem`: Reported problem/incident type
- `address`: Incident address
- `priority_number`: Priority level (numeric)
- `call_taker`: Name of call taker
- `call_reception`: Time call was received
- `dispatcher`: Dispatcher name
- `queue_time`: Time call was queued (seconds)
- `dispatch_time`: Time units dispatched (seconds)
- `phone_time`: Time on phone (seconds)
- `ack_time`: Time dispatch acknowledged (secs)
- `enroute_time`: Time units en route (seconds)
- `on_scene_time`: Time units on scene (seconds)
- `process_time`: Processing time (seconds)
- `total_time`: Total call time (seconds)
- `time_call_queued`: Timestamp call queued
- `time_call_dispatched`: Timestamp call dispatched
- `time_call_acknowledged`: Timestamp dispatch acknowledged
- `time_call_disconnected`: Timestamp call disconnected
- `time_unit_enroute`: Timestamp units en route
- `time_call_closed`: Timestamp call closed
- `disposition`: Final outcome

#### Example Usage

```python
from synth911gen import generate_synthetic_data

# Basic usage
data = generate_synthetic_data(num_records=1000)

# Advanced usage with custom parameters
data = generate_synthetic_data(
    num_records=5000,
    start_date="2024-06-01",
    end_date="2024-06-30",
    locale="fr_FR",
    agencies=["LAW", "FIRE"],
    num_names=12,
    output_file="french_law_fire.csv"
)

# Advanced usage with custom agency probabilities
data = generate_synthetic_data(
    num_records=1000,
    agencies=["LAW", "FIRE"],
    agency_probabilities=[0.8, 0.2],
    output_file="law_fire_weighted.csv"
)
```

### `validate_parameters()`

Validates input parameters before data generation.

```python
def validate_parameters(
    num_records: int,
    start_date: str,
    end_date: str,
    locale: str,
    num_names: int
) -> bool:
    """
    Validate input parameters for data generation.
    
    Args:
        num_records (int): Number of records to generate
        start_date (str): Start date string
        end_date (str): End date string
        locale (str): Locale string
        num_names (int): Number of names
        
    Returns:
        bool: True if all parameters are valid
        
    Raises:
        ValueError: If any parameter is invalid
    """
```

### `generate_incident_data()`

Generates individual incident records.

```python
def generate_incident_data(
    fake: Faker,
    start_date: datetime,
    end_date: datetime,
    agencies: List[str],
    dispatchers: List[str]
) -> Dict[str, Any]:
    """
    Generate a single incident record.
    
    Args:
        fake (Faker): Faker instance for data generation
        start_date (datetime): Start date for timestamp range
        end_date (datetime): End date for timestamp range
        agencies (List[str]): Available agencies
        dispatchers (List[str]): Available dispatcher names
        
    Returns:
        Dict[str, Any]: Single incident record
    """
```

## 🏗️ Data Generation Classes

### `DataGenerator`

Main class responsible for orchestrating data generation.

```python
class DataGenerator:
    """
    Main data generation class for creating synthetic 911 dispatch data.
    """
    
    def __init__(self, locale: str = "en_US"):
        """
        Initialize the data generator.
        
        Args:
            locale (str): Faker locale for data generation
        """
        
    def generate_records(self, num_records: int, **kwargs) -> pd.DataFrame:
        """
        Generate the specified number of records.
        
        Args:
            num_records (int): Number of records to generate
            **kwargs: Additional parameters
            
        Returns:
            pd.DataFrame: Generated records
        """
        
    def save_to_csv(self, data: pd.DataFrame, filename: str) -> None:
        """
        Save generated data to CSV file.
        
        Args:
            data (pd.DataFrame): Data to save
            filename (str): Output filename
        """
```

### `IncidentGenerator`

Handles the generation of individual incident records.

```python
class IncidentGenerator:
    """
    Generates individual incident records with realistic patterns.
    """
    
    def __init__(self, fake: Faker):
        """
        Initialize incident generator.
        
        Args:
            fake (Faker): Faker instance
        """
        
    def generate_incident(self, **kwargs) -> Dict[str, Any]:
        """
        Generate a single incident record.
        
        Args:
            **kwargs: Generation parameters
            
        Returns:
            Dict[str, Any]: Incident record
        """
```

## 📊 Data Patterns and Relationships

### Time Patterns

The generator creates realistic time patterns:

- **Hourly Distribution**: More calls during peak hours (8-10 AM, 5-7 PM)
- **Daily Patterns**: Weekday vs weekend variations
- **Seasonal Patterns**: Weather-related incident variations

### Geographic Patterns

- **Address Generation**: Realistic street addresses within the locale
- **Location Clustering**: Some areas have higher incident rates
- **Distance Relationships**: Response times correlate with location

### Incident Type Relationships

- **Agency Mapping**: Different agencies handle different incident types
- **Priority Correlation**: Incident types have associated priority levels
- **Time Correlation**: Certain incidents occur more at specific times

## 🔧 Configuration

### Supported Locales

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

### Agency Types

```python
DEFAULT_AGENCIES = [
    "LAW",    # Law enforcement
    "FIRE",   # Fire department
    "EMS",    # Emergency medical services
    "RESCUE", # Search and rescue
]
```

### Incident Types

```python
INCIDENT_TYPES = {
    "LAW": [
        "Traffic Accident",
        "Domestic Disturbance",
        "Burglary",
        "Assault",
        "Suspicious Activity"
    ],
    "FIRE": [
        "Structure Fire",
        "Vehicle Fire",
        "Brush Fire",
        "Medical Emergency",
        "Hazardous Materials"
    ],
    "EMS": [
        "Medical Emergency",
        "Trauma",
        "Cardiac Arrest",
        "Difficulty Breathing",
        "Unconscious Person"
    ]
}
```

## 🚨 Error Handling

### Common Exceptions

```python
class Synth911Error(Exception):
    """Base exception for Synth911Gen2 errors."""
    pass

class ValidationError(Synth911Error):
    """Raised when input validation fails."""
    pass

class GenerationError(Synth911Error):
    """Raised when data generation fails."""
    pass
```

### Error Handling Example

```python
try:
    data = generate_synthetic_data(
        num_records=1000,
        start_date="2024-01-01",
        end_date="2024-12-31",
        locale="en_US"
    )
except ValidationError as e:
    print(f"Validation error: {e}")
except GenerationError as e:
    print(f"Generation error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## 📈 Performance Considerations

### Memory Usage

- **Large Datasets**: For datasets > 100,000 records, consider chunking
- **DataFrame Operations**: Use efficient pandas operations
- **Garbage Collection**: Large objects are automatically cleaned up

### Processing Time

- **Small Datasets** (< 1,000 records): < 1 second
- **Medium Datasets** (1,000 - 10,000 records): 1-10 seconds
- **Large Datasets** (10,000 - 100,000 records): 10-60 seconds
- **Very Large Datasets** (> 100,000 records): 1+ minutes

### Optimization Tips

```python
# Use efficient data types
data = data.astype({
    'priority': 'int8',
    'incident_id': 'string'
})

# Process in chunks for very large datasets
chunk_size = 10000
for i in range(0, total_records, chunk_size):
    chunk = generate_synthetic_data(num_records=chunk_size)
    # Process chunk
```

## 🔍 Debugging

### Enable Debug Mode

```python
import logging

# Set up debug logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Debug output will show generation progress
data = generate_synthetic_data(num_records=100, debug=True)
```

### Data Validation

```python
def validate_generated_data(data: pd.DataFrame) -> bool:
    """
    Validate generated data for consistency.
    
    Args:
        data (pd.DataFrame): Generated data to validate
        
    Returns:
        bool: True if data is valid
    """
    # Check for required columns
    required_columns = ['incident_id', 'timestamp', 'caller_name', 'location']
    if not all(col in data.columns for col in required_columns):
        return False
    
    # Check for duplicate incident IDs
    if data['incident_id'].duplicated().any():
        return False
    
    # Check date range
    timestamps = pd.to_datetime(data['timestamp'])
    if timestamps.min() < start_date or timestamps.max() > end_date:
        return False
    
    return True
```

## 📚 Related Documentation

- [Architecture Overview](../architecture.md)
- [Architecture Decision Records (ADR)](../adr-0001-initial-architecture.md)
- [Entity Relationship Diagram](../er-diagram.md)
- [Deployment Guide](../deployment.md)

For more, see the [README](../../README.md) and the `/docs` directory.

---

**See Also**:

- [GUI API](gui.md) - Tkinter interface documentation
- [CLI API](cli.md) - Command-line interface documentation
- [Constants API](constants.md) - Configuration constants
