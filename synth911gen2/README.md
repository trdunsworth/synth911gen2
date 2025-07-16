# synth911gen2 Project

This project is designed to generate realistic inbound call volumes for a 911 center. It utilizes historical call volume data to simulate future call patterns based on various time frequencies.

## Project Structure

- **data/**: This directory contains CSV files with historical call volume data.
  - **hour.csv**: Hourly call volume data for the 911 center. Used to generate realistic inbound call volumes based on hourly patterns.
  - **week.csv**: Weekly call volume data for the 911 center. Provides insights into call volume trends over the course of a week.
  - **month.csv**: Monthly call volume data for the 911 center. Helps in understanding seasonal trends and variations in call volumes.
  - **day.csv**: Daily call volume data for the 911 center. Used to analyze daily fluctuations in call volumes.

- **synthvolgen.py**: This script is responsible for generating realistic inbound call volumes for the 911 center. It takes the following parameters:
  - **start_date**: The starting date for generating call volumes.
  - **num_rows**: The number of rows of call volume data to generate.
  - **frequency**: The frequency of the data (hourly, daily, weekly, or monthly).

## Usage Instructions

1. Ensure you have the required data files in the `data/` directory.
2. Run the `synthvolgen.py` script with the appropriate parameters to generate call volume data.
3. The generated data can be used for analysis, reporting, or further simulation of call handling scenarios.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.