import pandas as pd

#Reading in the file and printing the first 5 rows

file_path = "nsdp_delays_random.xlsx"
nsdp_df = pd.read_excel(file_path)
print(nsdp_df.head())

#1. Filter the Data

# Filtering the Data "Timeliness" Only Rows

type_df = nsdp_df[nsdp_df['Type'] == 'Timeliness']

#Excluding negative or missing values in Delay column

nsdp_filtered =  type_df[(type_df['Delay (days)'] >= 0) & (type_df['Delay (days)'].notna())]

print(nsdp_filtered.head())

nsdp_filtered.to_csv('nsdp_filtered.csv', index=False)

#2. Compute Aggregates

#Calculating mean of delay per year for each county

avg_delay = nsdp_filtered.groupby(['Year','ISO3 Code'])['Delay (days)'].mean().reset_index()
avg_delay.rename(columns={'Delay (days)': "Avg_Delays"}, inplace=True)

#Top 5 Countries with highest averages

Top5_avg_delay = avg_delay.sort_values(by='Avg_Delays', ascending=False).head(5)


print(Top5_avg_delay)


print(avg_delay)


#3. Regional Insights

#Compute the average delay by region for each year

unique_code = nsdp_filtered['ISO3 Code'].unique()
print(unique_code)

#Creating Region from each country
country_to_region = {'DNK': 'Europe',
                    'DEU': 'Europe' ,
                    'BRA': 'South America',
                    'IND': 'Asia',
                    'EGY' : 'Africa',
                    'JPN' : 'Asia',
                    'FRA' : 'Europe',
                    'CAN' : 'North America',
                    'ARG' : 'South America',
                    'MEX': 'North America'}

#Mapping the country to the region
nsdp_filtered.loc[:,'Region'] = nsdp_filtered['ISO3 Code'].map(country_to_region)
print(nsdp_filtered)

regional_avg = nsdp_filtered.groupby(['Year','Region'])['Delay (days)'].mean().reset_index()
regional_avg.rename(columns={'Delay (days)': "Avg_delays"}, inplace=True)

print(regional_avg)



#Region with the most improvement in timeliness

most_timely_region_per_year = regional_avg.loc[regional_avg.groupby('Year')['Avg_delays'].idxmin()]

print("Overall Most Timely Region by Year: ", most_timely_region_per_year)

#4. Detecting Outliers

print(nsdp_filtered["Delay (days)"].describe())

Q1 = nsdp_filtered["Delay (days)"].quantile(0.25)
Q3 = nsdp_filtered["Delay (days)"].quantile(0.75)
IQR = Q3 - Q1

#Uppper and Lower bounds

LowerBound = Q1 - 1.5 * IQR
UpperBound = Q3 + 1.5 * IQR

print(LowerBound)
print(UpperBound)

#Filtering Outliers

outliers_iqr = nsdp_filtered[(nsdp_filtered['Delay (days)'] < LowerBound) | (nsdp_filtered['Delay (days)'] > UpperBound)]


print("Detecting Outliers using IQR: ", outliers_iqr[['ISO3 Code','Delay (days)']])


#5. Exporting Results

#Exporting File

avg_delay.to_csv('Average_Delay_By_Country.csv', index=False)

regional_avg.to_csv('Regional_Averages.csv', index=False)

outliers_iqr.to_csv('Outliers.csv', index=False)