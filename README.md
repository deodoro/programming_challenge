# NSDP Delay Analysis Challenge

## Objective
Welcome to the NSDP Delay Analysis Challenge. This project involves analyzing delays in National Summary Data Page (NSDP) dissemination across various countries to identify patterns, trends, and outliers in the data. The end goal is to visually present these findings using Power BI, enhancing understanding of which countries and regions have shown improvement or regression in timeliness.

## Repository Contents
- **NSDP_DE_Challenge.py**: Python script for data processing and analysis.
- **Average_Delay_By_Country.csv**: Contains the average delay per year for each country, derived from the Python script.
- **Regional_Averages.csv**: Lists average delay by region for each year.
- **Outliers.csv**: Details outlier countries with their respective delay values.
- **NSDP_Analysis.pbix**: Power BI report for interactive data visualization.

## How to Use This Repository
1. **Data Analysis**:
   - Run the Python script `NSDP_DE_Challenge.py` to process the data and generate CSV files.
   - Ensure Python and necessary libraries (Pandas) are installed:
     ```bash
     pip install pandas
     ```

2. **Visualizing Data with Power BI**:
   - Open the Power BI report `NSDP_Analysis.pbix` with Power BI Desktop.
   - Explore the interactive visuals which can be filtered by year, country, and region.

## Power BI Report Features
- **Yearly Delay Trends**: Visualize how the average delay has changed over the years for each country.
- **Regional Performance**: Compare delays by region to see which regions have improved or worsened.
- **Top 5 Delayed Countries**: Identify the countries with the highest average delays.
- **Outliers Identification**: Highlight countries where delays are significantly higher or lower than the norm.

## Instructions for Running the Python Script
- Navigate to the directory containing `NSDP_DE_Challenge.py`.
- Execute the script:
  ```bash
  python NSDP_DE_Challenge.py
