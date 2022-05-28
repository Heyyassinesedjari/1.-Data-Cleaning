#Import modules we will use
import pandas as pd
import numpy as np

#1/ Taking a first look at the data

#Read in all our data
sf_permits = pd.read_csv(r"C:\Users\programmeur\Desktop\VSCode\Prerequisites\Course 1\data cleaning\Building_Permits.csv")

#Set seed for reproducibility
np.random.seed(0)

#Looking at the data
print(sf_permits.head())
print("-"*50)

#2/ Checking How many missing data points do we have?

# number of missing values per column
num_missing_val_perCol = sf_permits.isnull().sum()
print(num_missing_val_perCol)

#number of missing values in all the dataframe
num_missing_val = num_missing_val_perCol.sum()

#total number of cells in the dataframe
total_num_cells = np.product(sf_permits.shape)

#percentile of missing values in the dataframe
percent_missing = (num_missing_val / total_num_cells) * 100
print("the percentile of missing data in our dataset is ",percent_missing,"%")
print("-"*50)

#3/ figuring out why data is missing

print("""If a value in the "Street Number Suffix" column is missing, it is likely because it does not exist. 
If a value in the "Zipcode" column is missing, it was not recorded.""")
print("-"*50)

#4/ Dropping missing values: rows
sf_permits_drop_all_rows_with_na = sf_permits.dropna()

#5/ Dropping missing values: columns
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)

# calculate number of dropped columns
num_cols_in_original_dataset = sf_permits.shape[1]
num_cols_in_na_dropped = sf_permits_with_na_dropped.shape[1]
num_dropped_columns = num_cols_in_original_dataset - num_cols_in_na_dropped
print("Number of columns dropped is ",num_dropped_columns)
print("-"*50)

#6/ Filling missing values: automatically

sf_permits_with_na_imputed = sf_permits.fillna(method='bfill').fillna(0)
print(sf_permits_with_na_imputed)
print("-"*50)