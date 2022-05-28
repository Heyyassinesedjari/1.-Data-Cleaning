##useful tips
# make everything lower case
# remove any white spaces at the beginning and end of cells.
#use the fuzzywuzzy package to help identify which strings are closest to each other
### "apple" and "snapple" are two changes away from each other
### usually end up saving you at least a little time
###Fuzzywuzzy returns a ratio given two strings. The closer the ratio is to 100, the smaller th

#imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import chardet
from fuzzywuzzy import process
import fuzzywuzzy

#set seed for reproducibility
np.random.seed(0)

#load data
professors = pd.read_csv("pakistan_intellectual_capital.csv")

#look if there is any data entry inconsistency in 'Country' column
strings = professors["Country"].unique()
strings.sort()
print(strings)

#doing some data pre-processing on "Country" column
professors["Country"] = professors["Country"].str.lower()
professors["Country"] = professors["Country"].str.strip()

#Here, we can see that we deleted unnecessary spaces and lowercased every string
strings = professors["Country"].unique()
strings.sort()
print(strings)

#Now lets replace usofa by usa and southkorea by south korea
def replace_matches_in_column(df, column, string_to_match, min_ratio = 47):
    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = process.extract(string_to_match, strings, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
    # let us know the function's done
    print("All done!")


replace_matches_in_column(professors, "Country", "usa", 74)
replace_matches_in_column(professors, "Country", "south korea",47)

#now it's all good
strings = professors["Country"].unique()
strings.sort()
print(strings)
