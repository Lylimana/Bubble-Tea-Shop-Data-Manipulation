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
    # Data Preprocessing 

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

# Dropping null values
raw_df = raw_df.dropna(subset ={'number_of_ratings'})

# Standardization 

# Removing · from 'type_of_store' Columns 
raw_df['type_of_store'] = raw_df['type_of_store'].str.replace('·','')

# Standardizing 'number_of_ratings columns'
# Removing '()' from 'number_of_ratings'

raw_df['number_of_ratings'] = raw_df['number_of_ratings'].str.strip('()')
    # raw_df['number_of_ratings'] = raw_df['number_of_ratings'].str.slice(1,-1) 


# Changing values in 'number_of_ratings' from objects with K to int

    # my attempt to use regex to replace all the floats and convert to normal integers
        # mapping = {'K': '* 1e3'}
        # raw_df['number_of_ratings'] = pd.eval(raw_df['number_of_ratings'].replace(mapping, regex = True))


for number_ratings in raw_df['number_of_ratings']:
    if "K" in number_ratings:
    # This can also be used: if number_ratings[-1] == "K": 
        raw_df.loc[raw_df['number_of_ratings'] == number_ratings, 'number_of_ratings'] = number_ratings[0:-1:2]+"00"
        continue
   
raw_df['number_of_ratings'] = raw_df['number_of_ratings'].astype(int)
# If I find a better solution for this, I will replace it. 


# Splitting values in 'rllt__details' columns 

# Create new columns for values to be arranged into
raw_df['closing_times'] = np.nan
raw_df['opening_times'] = np.nan
raw_df['price'] = np.nan
raw_df['phone_number'] = np.nan
raw_df['location'] = np.nan

# Setting Columns data type to object
raw_df['closing_times'] = raw_df['closing_times'].astype(object)
raw_df['opening_times'] = raw_df['opening_times'].astype(object)
raw_df['price'] = raw_df['price'].astype(object)
raw_df['phone_number'] = raw_df['phone_number'].astype(object)
raw_df['location'] = raw_df['location'].astype(object)

# Setting Columns data type to str to allow for loops
raw_df['rllt__details 2'] = raw_df['rllt__details 2'].astype(str)
raw_df['rllt__details 3'] = raw_df['rllt__details 3'].astype(str)
raw_df['rllt__details 4'] = raw_df['rllt__details 4'].astype(str)

# Loop to funnel values into appropriate columns for each 'rllt__details' column
for details in raw_df['rllt__details 2']:
    if details == "null": 
        continue
    elif "Closes" in details:
        raw_df.loc[raw_df['rllt__details 2'] == details, 'closing_times'] = details
    elif "Opens" in details: 
        raw_df.loc[raw_df['rllt__details 2'] == details, 'opening_times'] = details
    elif "£" in details: 
        raw_df.loc[raw_df['rllt__details 2'] == details, 'price'] = details
    elif "07" in details:
        raw_df.loc[raw_df['rllt__details 2'] == details, 'phone_number'] = details
    elif "020" in details:
        raw_df.loc[raw_df['rllt__details 2'] == details, 'phone_number'] = details
    else:
        raw_df.loc[raw_df['rllt__details 2'] == details, 'location'] = details
      
for details in raw_df['rllt__details 3']:
    if details == "null": 
        continue
    elif "Closes" in details:
        raw_df.loc[raw_df['rllt__details 3'] == details, 'closing_times'] = details
    elif "Opens" in details: 
        raw_df.loc[raw_df['rllt__details 3'] == details, 'opening_times'] = details
    elif "£" in details: 
        raw_df.loc[raw_df['rllt__details 3'] == details, 'price'] = details
    elif "07" in details:
        raw_df.loc[raw_df['rllt__details 3'] == details, 'phone_number'] = details
    elif "020" in details:
        raw_df.loc[raw_df['rllt__details 3'] == details, 'phone_number'] = details
    else:
        raw_df.loc[raw_df['rllt__details 3'] == details, 'location'] = details
        
for details in raw_df['rllt__details 4']:
    if details == "null": 
        continue
    elif "Closes" in details:
        raw_df.loc[raw_df['rllt__details 4'] == details, 'closing_times'] = details
    elif "Opens" in details: 
        raw_df.loc[raw_df['rllt__details 4'] == details, 'opening_times'] = details
    elif "£" in details: 
        raw_df.loc[raw_df['rllt__details 4'] == details, 'price'] = details
    elif "07" in details:
        raw_df.loc[raw_df['rllt__details 4'] == details, 'phone_number'] = details
    elif "020" in details:
        raw_df.loc[raw_df['rllt__details 4'] == details, 'phone_number'] = details
    else:
        raw_df.loc[raw_df['rllt__details 4'] == details, 'location'] = details

# Dropping 'rllt__detail' columns 
drop_column_details = ['rllt__details 2', 'rllt__details 3', 'rllt__details 4']
        
raw_df.drop(drop_column_details, inplace = True, axis = 1)

# Splitting 'closing_times' and 'opening_times' column to only have time 
raw_df[['dot1', 'close','closing_time']] = raw_df['closing_times'].str.split(' ', n = 2, expand = True)
raw_df[['dot2', 'open','opening_time']] = raw_df['opening_times'].str.split(' ', n = 2, expand = True)

# Dropping unesscessary details columns 
drop_columns_times = ['dot1', 'dot2','close','open', 'closing_times', 'opening_times']

raw_df.drop(drop_columns_times, inplace = True, axis = 1)

# Most values in the 'price' column use £, ££ and £££ to indicate cost of product. 
# However, there are some values that give a range of '£1-10' which doesn't align with this. 
# From doing some research a single £ indicates a budget friendly shop with low prices usually from £5 - 10 
# And ££ indicates a mid range store and £££ for higher end 
# I'll be replacing values with '£1-10' with a single '£'.

# Changing '£1-10' values to £ in 'price' column
for x in raw_df['price']: 
    if x == '£1–10': 
        raw_df.loc[raw_df['price'] == x, 'price'] = '£'
        continue


# Changing 'closing_time' and 'opening_time' columns to more readable/manipulatable formats
# Setting Columns data type to str to allow for loops
# raw_df['closing_time'] = raw_df['closing_time'].astype("string")

# for x in raw_df['closing_time']: 

# from datetime import datetime 

# for x in raw_df['closing_time']: 
#     if ':' in x: 
#         raw_df.loc[raw_df['closing_time'] == x, 'closing_time'] = datetime.strptime(x, '%-I:%M %p')
#     elif ':' not in x:  
#         raw_df.loc[raw_df['closing_time'] == x, 'closing_time'] = datetime.strptime(x, '%-I %p')
#     continue

# Removing · from 'phone_number' Columns 
raw_df['phone_number'] = raw_df['phone_number'].str.replace('·','')
raw_df['phone_number'] = raw_df['phone_number'].str.replace(' ','')

raw_df.head(100)
