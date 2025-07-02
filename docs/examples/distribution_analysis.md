# Distribution Analysis Example

This example demonstrates how to analyze the numeric columns of a CSV file and recommend NumPy random distributions using `distribution_analyzer.py`.

## Usage

```bash
python distribution_analyzer.py synth_seed2.csv
```

- The script will output the best-fit distributions and parameters for each numeric column.
- Results are also saved to a text file (e.g., `distribution_results_synth_seed2.txt`).

## Requirements

- Python 3.11+
- pandas
- numpy
- scipy

Install dependencies with:

```bash
uv pip install -r ../../requirements.txt
```

## 📚 Related Documentation

- [Entity Relationship Diagram](../er-diagram.md)
- [Core API Reference](../api/core.md)
- [Dependencies](../dependencies.md)

For more, see the [README](../../README.md) and the `/docs` directory.
