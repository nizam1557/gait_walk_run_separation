# gait_walk_run_separation
A Python-based analysis to classify and visualize walking and running gait patterns based on acceleration data
# Gait Analysis

This repository contains a Python script to analyze and classify walking and running gait patterns from acceleration data. Using thresholds and peak detection, strides are extracted, categorized, and visualized.

## Features

- Automatically categorizes each data row as 'Walk' or 'Run' based on acceleration thresholds.
- Aggregates data from multiple CSV files in the current directory.
- Extracts strides using peak detection on the Z-axis acceleration.
- Computes stride-wise averages for acceleration across X, Y, and Z axes.
- Visualizes the walking vs. running strides on a scatter plot.

## Usage

1. Place all your `.csv` acceleration data files in the same directory as the script.
2. Run the script using Python:

   ```bash
   python gait_analysis.py
