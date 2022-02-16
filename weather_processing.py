"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries
import pandas as pd
import datetime
import numpy as np

# TODO Import the dataset 

path = './data/weather_dataset.data'
data = pd.read_table(path ,sep=',')
# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data['dy'] = data['dy'].apply(str)
data['mo'] = data['mo'].apply(str)
data['yr'] = data['yr'].apply(str)
data['date'] = data['mo'] +'/'+ data['dy']+'/'+'19'+data['yr']
data['date'] = pd.to_datetime(data['date'])
data['date'].dt.strftime('%d/%m/%Y')
data['dy'] = data['dy'].astype(int)
data['mo'] = data['mo'].astype(int)
data['yr'] = data['yr'].astype(int)

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
#data is clean, need to get rid of nan by replacing them with the mean of each column.

# TODO Write a function in order to fix date (this relate only to the year info) and apply it
#done above 

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
data = data.set_index(data['date'], drop=False, append=False, inplace=False, verify_integrity=False).drop('date', 1)

# TODO Compute how many values are missing for each location over the entire record
data.isna().sum() #for each location
data.isna().sum().sum() #for the entire dataset

# TODO Compute how many non-missing values there are in total
non_missing_values = data.shape[0]*data.shape[1] - data.isna().sum().sum()

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times
data.sum().sum()/data.count().sum()

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
loc_stats = data.describe().loc[['min', 'max', 'mean', 'std']]

# TODO Find the average windspeed in January for each location
data[data['mo'] == 1].groupby('mo').mean()

# TODO Downsample the record to a yearly frequency for each location
data.groupby(lambda x: x.year).mean()
# TODO Downsample the record to a monthly frequency for each location
data.groupby(lambda x: (x.year,x.month)).mean()
# TODO Downsample the record to a weekly frequency for each location
week = lambda x: (x-data.index[0]).days / 7
data.groupby(week).mean()

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks
first_half = data.iloc[:21*6,:]
weekly_first_half = first_half.groupby(week)
stats = weekly_first_half.apply(lambda x: x.describe().loc[['min', 'max', 'mean', 'std']])
print(stats)
