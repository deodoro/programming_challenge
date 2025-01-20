import pandas as pd

#Accessing the file located in Download folder

file_path = "Downloads/nsdp_delays_random.xlsx"
delays_df = pd.read_excel(file_path)

#1. include rows where Type is Timeliness and exclude any records where Delay (days) is negative or missing.

# Filter for rows where Type is 'Timeliness'
timeliness_df = delays_df[delays_df['Type'] == 'Timeliness']

# Exclude records where 'Delay (days)' is negative or missing
filtered_delays_df = timeliness_df[(timeliness_df['Delay (days)'] >= 0) & (timeliness_df['Delay (days)'].notna())]

print(filtered_delays_df.head())

#2. Calculate the average delay per year for each country. Identify the top 5 countries with the highest average delay across all years.

# Calculating the average delay per year for each country
avg_delay_df = filtered_delays_df.groupby(['Year', 'ISO3 Code'])['Delay (days)'].mean().reset_index()
avg_delay_df.rename(columns={'Delay (days)': 'Average Delay'}, inplace=True)

# Identifying the top 5 countries with the highest average delay across all years
top5_avg_delay_df = avg_delay_df.sort_values(by='Average Delay', ascending=False).head(5)

print(avg_delay_df)
print(top5_avg_delay_df)

#3. Compute the average delay by region for each year. Identify which region has shown the most improvement in timeliness over the years.

# Display unique ISO3 codes
unique_iso_codes = filtered_delays_df['ISO3 Code'].unique()
print(unique_iso_codes)

# Mapping countries to regions
country_region_map = {
    'DNK': 'Europe', 'DEU': 'Europe', 'BRA': 'South America',
    'IND': 'Asia', 'EGY': 'Africa', 'JPN': 'Asia',
    'FRA': 'Europe', 'CAN': 'North America', 'ARG': 'South America',
    'MEX': 'North America'
}

# Applying the country to region mapping using .loc for safe assignment
filtered_delays_df.loc[:, 'Region'] = filtered_delays_df['ISO3 Code'].map(country_region_map)
print(filtered_delays_df)

# Compute the average delay by region for each year
regional_avg_df = filtered_delays_df.groupby(['Year', 'Region'])['Delay (days)'].mean().reset_index()
regional_avg_df.rename(columns={'Delay (days)': 'Average Delays'}, inplace=True)

print(regional_avg_df)

# Identify the region with the most improvement in timeliness over the years
most_improved_region = regional_avg_df.loc[regional_avg_df.groupby('Year')['Average Delays'].idxmin()]

print("Region with the Most Improvement in Timeliness by Year:", most_improved_region)

#4. Identify any countries with delays that are statistical outliers (using a method of your choice, such as z-score or interquartile range).

# Calculate the first and third quartiles (Q1 and Q3)
first_quartile = filtered_delays_df["Delay (days)"].quantile(0.25)
third_quartile = filtered_delays_df["Delay (days)"].quantile(0.75)
interquartile_range = third_quartile - first_quartile  # Calculate the IQR

# Define lower and upper bounds for detecting outliers
lower_bound = first_quartile - 1.5 * interquartile_range
upper_bound = third_quartile + 1.5 * interquartile_range

print(f"Lower Bound for Outliers: {lower_bound}")
print(f"Upper Bound for Outliers: {upper_bound}")

# Filter rows where 'Delay (days)' falls outside the calculated bounds to identify outliers
outliers_df = filtered_delays_df[(filtered_delays_df['Delay (days)'] < lower_bound) | 
                                 (filtered_delays_df['Delay (days)'] > upper_bound)]


print("Detected Outliers: ", outliers_df[['ISO3 Code', 'Delay (days)']])

#5. Export the following outputs to CSV

# Exporting Average Delay by Country to a CSV file
avg_delay_df.to_csv('Downloads/Average_Delay_By_Country.csv', index=False)

# Exporting Regional Averages to a CSV file
regional_avg_df.to_csv('Downloads/Regional_Averages.csv', index=False)

# Exporting Outliers to a CSV file
outliers_df.to_csv('Downloads/Outliers.csv', index=False)

# Final print message to indicate completion of the process
print("CSV export process has been successfully completed.")
