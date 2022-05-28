#useful info
##UTF-8 is the standard text encoding



#imports 
import pandas as pd
import numpy as np
import seaborn as sns
##helpful character encoding module
import chardet 

#set seed for reproducibility
np.random.seed(0)

#bytes datatype
sample_entry = b'\xa7A\xa6n'
print(sample_entry)       #b'\xa7A\xa6n'
print(type(sample_entry)) #<class 'bytes'>

#changing the encoding from "big5-tw" to "utf-8"

new_entry = (sample_entry.decode("big5-tw")).encode("utf-8", errors = "replace")
print(new_entry)         #b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(type(new_entry))   #<class 'bytes'>


#reading in files with encoding problems
try:
    police_killing = pd.read_csv("PoliceKillingsUS.csv") #Error
except UnicodeDecodeError:
    print("'utf-8' code can't decode byte 0x96 in position 2: invalid start byte")


#searching for the encoding datatype
with open("PoliceKillingsUS.csv", "rb") as rawdata:
    rawdata.seek(0)
    result1 = chardet.detect(rawdata.read(10000))
    rawdata.seek(0)
    result2 = chardet.detect(rawdata.read(100000))

#encoding datatypes while reading 10 000 vs 100 000 characters
print(result1)
print(result2)

#try to read again
police_killing = pd.read_csv("PoliceKillingsUS.csv", encoding=result2["encoding"]) #it work only if we read more characters: 10.000 it doesn't work X but 100.000 it work
print(police_killing.tail())

#save it in utf-8 csv file
police_killing.to_csv("police_killing_utf-8.csv")