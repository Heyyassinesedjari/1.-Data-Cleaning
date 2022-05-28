#imports
import pandas as pd
import numpy as np
from dateutil.parser import parse
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#load_data
earthquakes = pd.read_csv("database.csv")
#set seed for reproducibility
np.random.seed(0)

#checking if there is any date column (Yes)
pd.set_option('max_columns',None)
print(earthquakes.head())

#checking its data type (dtype: object => python doesn't now that this is a date column)
print(earthquakes["Date"].head())
#or
print(earthquakes["Date"].dtype) 

#checking if all dates have the same formats
length_format = earthquakes["Date"].str.len()
print(length_format.value_counts()) #3 different formats

#observing does 3 different dates
indicies = earthquakes["Date"].str.len() == 24
different_dates = earthquakes["Date"].loc[indicies]
print(different_dates)

#changing manually the format of does dates since they are just 3
earthquakes.loc[3378,"Date"] = "02/23/1975"
earthquakes.loc[7512,"Date"] = "04/28/1985"
earthquakes.loc[20650,"Date"] = "03/13/2011"

#making a new datetime object column called "parsed_dates" => Now python does recognize this column as a datetime column
earthquakes["parsed_dates"] = pd.to_datetime(earthquakes["Date"], format = "%m/%d/%Y")
print(earthquakes["parsed_dates"])

#let's create a day column out of th "parsed_dates" column
earthquakes["Day of the month"] = earthquakes["parsed_dates"].dt.day
print(earthquakes["Day of the month"])

#plotting the day column to see if we didn't confuse day with months, the ditribution must be relatively even, let's see
sns.distplot(earthquakes["Day of the month"], kde=False, bins=31)
plt.show()  #the graph makes good sens ! :)
