# Basic Examples

This guide provides simple, practical examples for getting started with Synth911Gen2.

## 🚀 Quick Examples

### Example 1: Generate Basic Dataset

Generate a simple dataset with default settings:

```python
from synth911gen import generate_synthetic_data

# Generate 1,000 records with default settings
data = generate_synthetic_data(num_records=1000)

print(f"Generated {len(data)} records")
print(f"Columns: {list(data.columns)}")
print(data.head())
```

**Output:**
```
Generated 1000 records
Columns: ['incident_id', 'timestamp', 'caller_name', 'caller_phone', 'location', 'incident_type', 'priority', 'agency', 'dispatcher', 'status']
   incident_id           timestamp caller_name    caller_phone                    location incident_type  priority agency    dispatcher    status
0  INC-2024-000001  2024-01-01 08:15:22   John Smith  (555) 123-4567        123 Main St, Anytown, ST  Medical Emergency        2    EMS  Sarah Johnson  Dispatched
1  INC-2024-000002  2024-01-01 09:30:45   Jane Doe    (555) 234-5678        456 Oak Ave, Anytown, ST  Traffic Accident        3   LAW  Mike Wilson   Dispatched
```

### Example 2: Generate Data for Specific Date Range

```python
# Generate data for a specific month
data = generate_synthetic_data(
    num_records=500,
    start_date="2024-06-01",
    end_date="2024-06-30",
    output_file="june_2024_data.csv"
)

print(f"Generated {len(data)} records for June 2024")
```

### Example 3: Generate Multi-Language Data

```python
# Generate French data
french_data = generate_synthetic_data(
    num_records=1000,
    locale="fr_FR",
    output_file="french_dispatch.csv"
)

# Generate Spanish data
spanish_data = generate_synthetic_data(
    num_records=1000,
    locale="es_ES",
    output_file="spanish_dispatch.csv"
)

print("Generated French and Spanish datasets")
```

## 📊 Data Analysis Examples

### Example 4: Basic Statistics

```python
import pandas as pd

# Generate data
data = generate_synthetic_data(num_records=5000)

# Basic statistics
print("=== Basic Statistics ===")
print(f"Total records: {len(data)}")
print(f"Date range: {data['timestamp'].min()} to {data['timestamp'].max()}")
print(f"Unique agencies: {data['agency'].nunique()}")
print(f"Unique incident types: {data['incident_type'].nunique()}")

# Agency distribution
print("\n=== Agency Distribution ===")
agency_counts = data['agency'].value_counts()
print(agency_counts)

# Priority distribution
print("\n=== Priority Distribution ===")
priority_counts = data['priority'].value_counts().sort_index()
print(priority_counts)
```

### Example 5: Time Analysis

```python
import pandas as pd

# Generate data
data = generate_synthetic_data(num_records=1000)

# Convert timestamp to datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Extract hour and analyze patterns
data['hour'] = data['timestamp'].dt.hour
data['day_of_week'] = data['timestamp'].dt.day_name()

# Hourly distribution
print("=== Calls by Hour ===")
hourly_counts = data['hour'].value_counts().sort_index()
for hour, count in hourly_counts.items():
    print(f"{hour:02d}:00 - {count} calls")

# Day of week distribution
print("\n=== Calls by Day of Week ===")
daily_counts = data['day_of_week'].value_counts()
print(daily_counts)
```

### Example 6: Incident Type Analysis

```python
# Generate data
data = generate_synthetic_data(num_records=2000)

# Incident type by agency
print("=== Incident Types by Agency ===")
incident_agency = data.groupby(['agency', 'incident_type']).size().unstack(fill_value=0)
print(incident_agency)

# Priority by incident type
print("\n=== Priority by Incident Type ===")
priority_incident = data.groupby(['incident_type', 'priority']).size().unstack(fill_value=0)
print(priority_incident)
```

## 🔧 Configuration Examples

### Example 7: Custom Agency Selection

```python
# Generate data with only law enforcement and fire department
data = generate_synthetic_data(
    num_records=1000,
    agencies=["LAW", "FIRE"],
    output_file="law_fire_only.csv"
)

print(f"Generated {len(data)} records for LAW and FIRE agencies")
print(f"Agencies in dataset: {data['agency'].unique()}")
```

### Example 8: Multiple Dispatchers

```python
# Generate data with 20 different dispatcher names
data = generate_synthetic_data(
    num_records=5000,
    num_names=20,
    output_file="multi_dispatcher.csv"
)

print(f"Generated {len(data)} records with {data['dispatcher'].nunique()} dispatchers")
print(f"Dispatcher names: {sorted(data['dispatcher'].unique())}")
```

### Example 9: Custom Date Ranges

```python
# Generate data for multiple years
data = generate_synthetic_data(
    num_records=10000,
    start_date="2023-01-01",
    end_date="2024-12-31",
    output_file="two_year_data.csv"
)

print(f"Generated {len(data)} records spanning 2023-2024")
```

## 📁 File Management Examples

### Example 10: Save to Different Formats

```python
import pandas as pd

# Generate data
data = generate_synthetic_data(num_records=1000)

# Save as CSV
data.to_csv("dispatch_data.csv", index=False)

# Save as Excel (requires openpyxl)
data.to_excel("dispatch_data.xlsx", index=False)

# Save as JSON
data.to_json("dispatch_data.json", orient="records", indent=2)

print("Data saved in multiple formats")
```

### Example 11: Load and Process Existing Data

```python
import pandas as pd

# Load existing data
data = pd.read_csv("computer_aided_dispatch.csv")

# Process the data
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['date'] = data['timestamp'].dt.date
data['hour'] = data['timestamp'].dt.hour

# Filter for specific date
june_data = data[data['date'] >= pd.to_datetime('2024-06-01').date()]
june_data = june_data[june_data['date'] <= pd.to_datetime('2024-06-30').date()]

print(f"Found {len(june_data)} records in June 2024")
```

## 🎯 Real-World Scenarios

### Example 12: Testing Environment Setup

```python
# Generate small test dataset
test_data = generate_synthetic_data(
    num_records=100,
    start_date="2024-01-01",
    end_date="2024-01-02",
    output_file="test_data.csv"
)

print("Test dataset generated for development/testing")
```

### Example 13: Training Data for ML Models

```python
# Generate diverse dataset for machine learning
ml_data = generate_synthetic_data(
    num_records=50000,
    start_date="2023-01-01",
    end_date="2024-12-31",
    locale="en_US",
    agencies=["LAW", "FIRE", "EMS"],
    num_names=15,
    output_file="ml_training_data.csv"
)

print(f"Generated {len(ml_data)} records for ML training")
```

### Example 14: Multi-Language Testing

```python
import os

# Generate datasets in multiple languages
locales = ["en_US", "fr_FR", "es_ES", "de_DE"]

for locale in locales:
    data = generate_synthetic_data(
        num_records=1000,
        locale=locale,
        output_file=f"{locale}_data.csv"
    )
    print(f"Generated {len(data)} records for {locale}")

print("Multi-language datasets created")
```

## 🔍 Data Validation Examples

### Example 15: Validate Generated Data

```python
def validate_data(data):
    """Validate generated data for consistency."""
    
    # Check for required columns
    required_columns = ['incident_id', 'timestamp', 'caller_name', 'location']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"Missing columns: {missing_columns}")
        return False
    
    # Check for duplicate incident IDs
    if data['incident_id'].duplicated().any():
        print("Duplicate incident IDs found")
        return False
    
    # Check for valid priorities
    if not all(data['priority'].between(1, 5)):
        print("Invalid priority values found")
        return False
    
    # Check for valid agencies
    valid_agencies = ["LAW", "FIRE", "EMS", "RESCUE"]
    invalid_agencies = data[~data['agency'].isin(valid_agencies)]['agency'].unique()
    if len(invalid_agencies) > 0:
        print(f"Invalid agencies: {invalid_agencies}")
        return False
    
    print("Data validation passed!")
    return True

# Generate and validate data
data = generate_synthetic_data(num_records=1000)
validate_data(data)
```

### Example 16: Data Quality Checks

```python
def check_data_quality(data):
    """Perform data quality checks."""
    
    print("=== Data Quality Report ===")
    
    # Check for missing values
    missing_values = data.isnull().sum()
    if missing_values.sum() > 0:
        print("Missing values found:")
        print(missing_values[missing_values > 0])
    else:
        print("No missing values found")
    
    # Check data types
    print(f"\nData types:")
    print(data.dtypes)
    
    # Check value ranges
    print(f"\nValue ranges:")
    print(f"Priority: {data['priority'].min()} - {data['priority'].max()}")
    print(f"Unique agencies: {data['agency'].nunique()}")
    print(f"Unique incident types: {data['incident_type'].nunique()}")
    
    # Check timestamp range
    timestamps = pd.to_datetime(data['timestamp'])
    print(f"Date range: {timestamps.min()} to {timestamps.max()}")

# Generate and check data quality
data = generate_synthetic_data(num_records=1000)
check_data_quality(data)
```

## 🚨 Error Handling Examples

### Example 17: Handle Generation Errors

```python
try:
    # Try to generate data with invalid parameters
    data = generate_synthetic_data(
        num_records=-100,  # Invalid: negative number
        start_date="invalid-date",  # Invalid: wrong format
        end_date="2024-12-31"
    )
except ValueError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

# Correct usage
try:
    data = generate_synthetic_data(
        num_records=1000,
        start_date="2024-01-01",
        end_date="2024-12-31"
    )
    print(f"Successfully generated {len(data)} records")
except Exception as e:
    print(f"Error: {e}")
```

---

**Next Steps**: 
- Explore [Advanced Examples](advanced.md) for complex scenarios
- Check [Integration Examples](integration.md) for third-party integrations
- Review [Customization Examples](customization.md) for extending functionality 