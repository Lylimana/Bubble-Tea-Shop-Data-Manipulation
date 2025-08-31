import pandas as pd
import numpy as np
import string
import csv


# Importing raw bubble tea shop data.
df1 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset1.csv")
df2 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset2.csv")
df3 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset3.csv")
df4 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset4.csv")
df5 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset5.csv")
df6 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset6.csv")
df7 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset7.csv")
df8 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset8.csv")
df9 = pd.read_csv("LondonBubbleTeaShopsDataset/BubbleTeaShopsDataset9.csv")

df_array = [df1, df2, df3, df3, df4, df5, df6, df7, df8, df9]

raw_df = pd.concat(df_array)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# PLAN OF ACTIONS 

    # Inital Data Exploration 
        # To understand the data im manipulating
    # Data Proprocessing 



# -----------------------------------------------------------------------------------------------------------------------------------------------

# INITIAL DATA EXPLORING 
raw_df.head(100)

raw_df.shape # Output suggest 201 shops and 16 features. 
    
raw_df.columns 
    # Output:
    # 'OSrXXb', 'rllt__details', 'yi40Hd', 'RDApEe', 'rllt__details 2',
    # 'rllt__details 3', 'rllt__details 4', 'rllt__details 5', 'uDyWh',
    # 'uDyWh 2', 'yYlJEf href', 'BSaJxc', 'yYlJEf href 2', 'UbRuwe',
    # 'rllt__details 6', 'uDyWh 3'

    # '' - Some sort of ID 
    # OSrXXb - Name of shop 
    # rllt__details - Type of store
    # yi40Hd - Rating
    # RDApEe - Number of ratings
    # rllt__details 2 - location/price/phone_number/closing_hours/opening_hours
    # rllt__details 3 - location/price/phone_number/closing_hours/opening_hours
    # rllt__details 4 - location/price/phone_number/closing_hours/opening_hours
    # rllt__details 5 - open/closed
    # uDyWh - Text Reviews ???
    # uDyWh 2 - Products sold ???
    # yYlJEf href - website link 
    # BSaJxc - link ???
    # yYlJEf href 2 - Google maps link 
    # UbRuwe - Directions ???
    # rllt__details 6 - Phone number
    # uDyWh 3 - ??? 

# Removing Columns 
drop_columns = [
    'uDyWh', 
    'uDyWh 2', 
    'yYlJEf href', 
    'BSaJxc', 
    'yYlJEf href 2', 
    'UbRuwe', 
    'rllt__details 6', 
    'uDyWh 3', 
    'rllt__details 5'
    ]

raw_df.drop(drop_columns, inplace = True, axis = 1)

raw_df.columns

# Renaming Columns 
raw_df = raw_df.rename(columns = {
                        'OSrXXb': 'shop_name', 
                        'rllt__details': 'type_of_store',
                        'yi40Hd': 'ratings', 
                        'RDApEe': 'number_of_ratings', 
                        })

# Checking data types
raw_df.dtypes
    # shop_name - object 
    # type_of_store - object
    # ratings - float64
    # number_of_ratings - object
    # rllt_details 2 - object
    # rllt_details 3 - object
    # rllt_details 4 - object

# Standardization 

# Standardizing "number_of_ratings columns"
# Removing "()"" from "number_of_ratings"
raw_df['number_of_ratings'] = raw_df['number_of_ratings'].str.slice(1,-1) 

# Changing floats to whole numbers.
for number_ratings in raw_df['number_of_ratings']: 
    if "K" in number_ratings:
        raw_df[number_ratings] = (raw_df[number_ratings].str.slice(0,-2)) 
    else: 
        continue

raw_df.head(100)