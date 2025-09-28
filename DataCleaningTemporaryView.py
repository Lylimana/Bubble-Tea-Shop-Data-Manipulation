import pandas as pd
import numpy as np
import string
import csv

# Temporary File to explore data from a diferent perspective (DataCleaning.py was getting too messy)

# Importing raw bubble tea shop data.
cleaned_data1 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset1.csv")
cleaned_data2 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset2.csv")
cleaned_data3 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset3.csv")
cleaned_data4 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset4.csv")
cleaned_data5 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset5.csv")
cleaned_data6 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset6.csv")
cleaned_data7 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset7.csv")
cleaned_data8 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset8.csv")
cleaned_data9 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset9.csv")

df= [cleaned_data1, cleaned_data2, cleaned_data3, cleaned_data3, cleaned_data4, cleaned_data5, cleaned_data6, cleaned_data7, cleaned_data8, cleaned_data9]

# Combining Datasets 
df = pd.concat(df)

# Checking df shape
df.shape

# Checking column names 
df.columns.tolist()
'''
Output: 
    ['OSrXXb',
    'rllt__details',
    'yi40Hd',
    'RDApEe',
    'rllt__details 2',
    'rllt__details 3',
    'rllt__details 4',
    'rllt__details 5',
    'uDyWh',
    'uDyWh 2',
    'yYlJEf href',
    'BSaJxc',
    'yYlJEf href 2',
    'UbRuwe',
    'rllt__details 6',
    'uDyWh 3']
'''

# Checking data
df.head(100)
'''
Upon some initial investigation, this is what I found: 
    'OSrXXb' - Shop Names   
    'rllt__details' - Type of store (mostly all bubble tea stores)
    'yi40Hd' - Rating 
    'RDApEe' - Number of Ratings
    'rllt__details 2' - Details (Location, Opening Times, Closing Times, Price, Phone Number)
    'rllt__details 3' - Details (Location, Opening Times, Closing Times, Price, Phone Number)
    'rllt__details 4' - Details (Location, Opening Times, Closing Times, Price, Phone Number)
    'rllt__details 5' - Details (Location, Opening Times, Closing Times, Price, Phone Number)
    'uDyWh' - Review
    'uDyWh 2' - Type of store (mostly all bubble tea stores) ?
    'yYlJEf href' - Website link 
    'BSaJxc' - Website (Not link)
    'yYlJEf href 2' - Google maps location 
    'UbRuwe' - Direction (Not link)
    'rllt__details 6' - Details (Location, Opening Times, Closing Times, Price, Phone Number)
    'uDyWh 3' - Details (Location, Opening Times, Closing Times, Price, Phone Number)?
'''

# Dropping unecessary columns 

# Creating function to drop columns in case more columns would need to be drop in the future
def drop_columns(df, columns): 
    df = df.drop(columns, axis = 1)
    return df

columns_to_drop = ['rllt__details', 'rllt__details 5', 'uDyWh 2', 'BSaJxc', 'UbRuwe']

df = drop_columns(df, columns_to_drop)

# Adding new columns 
df[['Address', 'Price', 'Phone number', 'Opening Times', 'Closing Times']] = np.nan

# Renaming existing columns
df = df.rename(columns = 
    {'OSrXXb': 'Shop Name',
    'yi40Hd': 'Rating',
    'RDApEe': 'Number of Ratings',
    'rllt__details 2': 'Details1',
    'rllt__details 3': 'Details2',
    'rllt__details 4': 'Details3',
    'rllt__details 6': 'Details4',
    'uDyWh 3': 'Details5',
    'uDyWh': 'Review',
    'yYlJEf href': 'Link',
    'yYlJEf href 2': 'Directions',
    }
    )

# Checking columns data types
df.dtypes

# Changing column datatypes to str
df[['Details1','Details2','Details3','Details4','Details5']] = df[['Details1','Details2','Details3','Details4','Details5']].astype(str)

df[['Closing Times','Opening Times','Price','Phone number','Address']] = df[['Closing Times','Opening Times','Price','Phone number','Address']].astype(str)

# Filtering values based on their contents: 'Address', 'Price', 'Phone number', 'Opening Times', 'Closing Times'
def column_filter(df, column):
    for value in df[column]:
        if value == "null": 
            continue
        elif "Closes" in value:
            df.loc[df[column] == value, 'Closing Times'] = value
        elif "Opens" in value: 
            df.loc[df[column] == value, 'Opening Times'] = value
        elif "£" in value: 
            df.loc[df[column] == value, 'Price'] = value
        elif "07" in value:
            df.loc[df[column] == value, 'Phone number'] = value
        elif "020" in value:
            df.loc[df[column] == value, 'Phone number'] = value
        else:
            df.loc[df[column] == value, 'Address'] = value
    return df

# Creating array for columns that need to be filtered
details = ['Details1','Details2','Details3','Details4', 'Details5']

# Calling column filter function on details array 
df = column_filter(df, details[0])

df = column_filter(df, details[1])

df = column_filter(df, details[2])

df = column_filter(df, details[3])

df = column_filter(df, details[4])

df.head()

# Dropping unecessary columns
columns_to_drop2 = ['Details1','Details2','Details3','Details4', 'Details5']

df = drop_columns(df, columns_to_drop2)

df.head()