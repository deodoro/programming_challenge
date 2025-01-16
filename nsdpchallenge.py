# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CZGxgtw9LNwjLQRAwnNoGb6srVT_y5qE

**Country delays in NSDP dissemination**
"""

#Importing required libraries
import os
import pandas as pd
import numpy as np
import re

#Get current Directoy
cwd = os.getcwd()
print(cwd)

#Read the data from excel to pandas dataframe
#Excluding the current header ,as the 1st row is the actual header
data = pd.read_excel('nsdp_delays_random.xlsx',header=1)

#Understand the data/types
data.head()

"""**Data Cleansing**

1. The current data has few columns which are not required and hence can be removed/ignored.
2. There are errors/typos in data, which can be replaced with Zero's. 
3. Ignoring to query the data based on 'P/T' information, as the description for 'T' is missing and for some coutries the 'T' type also  has some value in the timelines.data['P/T'].unique()
"""

#Removing the columns which are not required 
data.drop(data.columns[[0,3, 5, 6, 23, 24, 25, 26]], axis=1, inplace=True)

#re-arranging the columns to have quaterly data together
data = data.iloc[:, [0,1,2,6,10,14,18,3,4,5,7,8,9,11,12,13,15,16,17]]

#Replace negetive values with 0
data = data.replace(-9999, 0)

#Replace the outliers with 0 (9999)
data = data.replace(9999, 0)

# Replacing np.nan with 0
data = data.replace(np.nan, 0)

#Replace spaces
data = data.replace(" ", "")

#Missing values can be treated with  'Zero's' . considering that there is no delay .
data.fillna(0)

#data = data.replace(['O','S','X','P','No','NYD','S -35'], 0)

#Replace anything/string which is not a numeric value with Zero (only in timelines column type)
data.iloc[:, 3:19] = data.iloc[:, 3:19].replace(r'\D+', 0, regex=True).astype('int')

# After preprocessing the data ,validate/test the data in the columns from [Q1,Dec] to check if they can be used for numeric conversion 
data.describe()

"""**Aggregating the Timelines**

1. some of the codes have monthly data and some have only quaterly data .
2. Assuming the quatery data is sum of the 3 months .And hence codes with montly data and quaterly data both are averaged by 12 months .
"""

# Averaging on quaterly data [Q1 : Q4]
data = data.assign(qtAverage=lambda x: (x['Q1'] + x['Q2'] + x['Q3'] + x['Q4'])/12)

# Averaging on monthly data [Jan : Dec]
data = data.assign(mtlyAverage=lambda x: data.iloc[:,7:18].mean(axis=1))

# Sum of Averages 
# Since the country has either quaterly data or montly data , they can be summed up
data = data.assign(Average=lambda x: x['qtAverage'] + x['mtlyAverage'])

# Export the data fram into an excel 
data.to_excel("output_new.xlsx",
...              sheet_name='Sheet_name_1')

#-------------------------------End-----------------------------------------------#