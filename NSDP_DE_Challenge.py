import pandas as pd

# Accessing the file located in Download folder
file_path = "Downloads/nsdp_delays_random.xlsx"
delays_df = pd.read_excel(file_path)

# 1. Include rows where Type is Timeliness and exclude any records where Delay (days) is negative or missing
timeliness_df = delays_df[delays_df['Type'] == 'Timeliness']
filtered_delays_df = timeliness_df[(timeliness_df['Delay (days)'] >= 0) & (timeliness_df['Delay (days)'].notna())]
print("Filtered data preview:\n", filtered_delays_df.head())

# 2. Calculate the average delay per year for each country
avg_delay_df = filtered_delays_df.groupby(['Year', 'ISO3 Code'])['Delay (days)'].mean().reset_index()
avg_delay_df.rename(columns={'Delay (days)': 'Average Delay'}, inplace=True)

# Identify the top 5 countries with the highest average delay across all years
top5_avg_delay_df = avg_delay_df.sort_values(by='Average Delay', ascending=False).head(5)
print("Top 5 countries with highest average delay:\n", top5_avg_delay_df)

# 3. Compute the average delay by region for each year
# Mapping countries to regions
country_region_map = {
    'DNK': 'Europe', 'DEU': 'Europe', 'BRA': 'South America',
    'IND': 'Asia', 'EGY': 'Africa', 'JPN': 'Asia',
    'FRA': 'Europe', 'CAN': 'North America', 'ARG': 'South America',
    'MEX': 'North America'
}

# Applying the country to region mapping
filtered_delays_df['Region'] = filtered_delays_df['ISO3 Code'].map(country_region_map)
print("Filtered data with regions preview:\n", filtered_delays_df.head())

# Compute the average delay by region for each year
regional_avg_df = filtered_delays_df.groupby(['Year', 'Region'])['Delay (days)'].mean().reset_index()
regional_avg_df.rename(columns={'Delay (days)': 'Average Delays'}, inplace=True)
print("Regional averages:\n", regional_avg_df)

# Identify the region with the most improvement in timeliness over the years
most_improved_region = regional_avg_df.loc[regional_avg_df.groupby('Region')['Average Delays'].idxmin()]
print("Region with the most improvement in timeliness:\n", most_improved_region)

# 4. Identify any countries with delays that are statistical outliers
# Calculate the first and third quartiles (Q1 and Q3)
first_quartile = filtered_delays_df["Delay (days)"].quantile(0.25)
third_quartile = filtered_delays_df["Delay (days)"].quantile(0.75)
interquartile_range = third_quartile - first_quartile

# Define lower and upper bounds for detecting outliers
lower_bound = first_quartile - 1.5 * interquartile_range
upper_bound = third_quartile + 1.5 * interquartile_range
print(f"Lower Bound for Outliers: {lower_bound}, Upper Bound for Outliers: {upper_bound}")

# Filter rows where 'Delay (days)' falls outside the calculated bounds to identify outliers
outliers_df = filtered_delays_df[(filtered_delays_df['Delay (days)'] < lower_bound) | 
                                 (filtered_delays_df['Delay (days)'] > upper_bound)]
print("Detected outliers:\n", outliers_df[['ISO3 Code', 'Delay (days)']])

# 5. Export the results to CSV
# Exporting Average Delay by Country to a CSV file
if not avg_delay_df.empty:
    avg_delay_df.to_csv('Downloads/Average_Delay_By_Country.csv', index=False)
    print("Average Delay by Country exported successfully.")

# Exporting Regional Averages to a CSV file
if not regional_avg_df.empty:
    regional_avg_df.to_csv('Downloads/Regional_Averages.csv', index=False)
    print("Regional Averages exported successfully.")

# Exporting Outliers to a CSV file
if not outliers_df.empty:
    outliers_df.to_csv('Downloads/Outliers.csv', index=False)
    print("Outliers exported successfully.")
else:
    print("No outliers detected. Skipping export.")

# Final message
print("CSV export process has been successfully completed.")

