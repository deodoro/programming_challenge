# NSDP Delay Analysis Challenge

## Objective
Welcome to the NSDP Delay Analysis Challenge Implementations. This project involves analyzing delays in National Summary Data Page (NSDP) dissemination across various countries to identify patterns, trends, and outliers in the data. The end goal is a visual presentation of these findings using Power BI, enhancing understanding of which countries and regions have shown improvement or regression in timeliness.

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

## Analyzing Data with Power BI Report
After running the Python script and generating the CSV files, results are loaded into the Power BI report to start analysis. The Power BI report, `NSDP_Analysis.pbix`, includes several interactive visualizations that allow for a dynamic exploration of the data.

### Features of the Power BI Report
1. **Yearly Delay Trends**: This line chart displays the average delay for each country across different years, helping to visualize trends and changes over time.
2. **Regional Performance Comparison**: A clustered bar chart shows the average delay by region, enabling comparisons across different regions and identification of regional trends.
3. **Top 5 Countries with Highest Delays**: A bar chart or table that lists the countries experiencing the highest average delays, drawing attention to areas that may need policy or process improvements.
4. **Outlier Analysis**: A scatter plot or highlighted table indicates outlier countries with delays significantly different from the norm, providing insights into extreme cases.

### Using the Power BI Report
- **Interactive Slicers**: Utilize the slicers provided for `Year`, `Country`, and `Region` to filter the data across different visualizations. These slicers help refine your view to specific subsets of data, enhancing your ability to conduct targeted analysis.
- **Dynamic Exploration**: Select different years to see how delay trends have shifted over time. Choose specific countries or regions to focus your analysis and view detailed performance. This dynamic interactivity allows stakeholders to pinpoint issues and track improvements or declines in timeliness across the dataset.

### Navigating the Visuals
- **Click and Explore**: Each visualization is interactive. Clicking on a country in any chart will filter other visuals to show relevant data for that country. Similarly, selecting a region or a year adjusts all charts to reflect data corresponding to your selection.
- **Drill Down/Up**: Some charts support drilling down for more detailed data exploration or drilling up for a broader overview. This feature is especially useful in understanding the granular details of delay data or in gaining a high-level perspective.

## Conclusion
This repository and the Power BI report provide comprehensive features for analyzing NSDP dissemination delays. Through detailed data processing and interactive visualizations, users can gain meaningful insights into the factors influencing reporting timeliness.
