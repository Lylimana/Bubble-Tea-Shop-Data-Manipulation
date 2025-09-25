import pandas as pd
import numpy as np
import string
import csv


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

cleaned_data_array = [cleaned_data1, cleaned_data2, cleaned_data3, cleaned_data3, cleaned_data4, cleaned_data5, cleaned_data6, cleaned_data7, cleaned_data8, cleaned_data9]

raw_cleaned_data = pd.concat(cleaned_data_array)

# ----------------------------------------------------------------------------------------------------------------------------------

# PLAN OF ACTIONS 

    # Inital Data Exploration 
        # To understand the data im manipulating
    # Data Preprocessing 

# ----------------------------------------------------------------------------------------------------------------------------------

# INITIAL DATA EXPLORING 
raw_cleaned_data.head(100)

raw_cleaned_data.shape # Output suggest 201 shops and 16 features. 
    
raw_cleaned_data.columns 
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

raw_cleaned_data.drop(drop_columns, inplace = True, axis = 1)

raw_cleaned_data.columns

# Renaming Columns 
raw_cleaned_data = raw_cleaned_data.rename(columns = {
                        'OSrXXb': 'shop_name', 
                        'rllt__details': 'type_of_store',
                        'yi40Hd': 'ratings', 
                        'RDApEe': 'number_of_ratings', 
                        })

# Checking data types
raw_cleaned_data.dtypes
    # shop_name - object 
    # type_of_store - object
    # ratings - float64
    # number_of_ratings - object
    # rllt_details 2 - object
    # rllt_details 3 - object
    # rllt_details 4 - object

# Dropping null values
raw_cleaned_data = raw_cleaned_data.dropna(subset ={'number_of_ratings'})

# Standardization 

# Removing · from 'type_of_store' Columns 
raw_cleaned_data['type_of_store'] = raw_cleaned_data['type_of_store'].str.replace('·','')

# Standardizing 'number_of_ratings columns'
# Removing '()' from 'number_of_ratings'

raw_cleaned_data['number_of_ratings'] = raw_cleaned_data['number_of_ratings'].str.strip('()')
    # raw_cleaned_data['number_of_ratings'] = raw_cleaned_data['number_of_ratings'].str.slice(1,-1) 


# Changing values in 'number_of_ratings' from objects with K to int

    # my attempt to use regex to replace all the floats and convert to normal integers
        # mapping = {'K': '* 1e3'}
        # raw_cleaned_data['number_of_ratings'] = pd.eval(raw_cleaned_data['number_of_ratings'].replace(mapping, regex = True))


for number_ratings in raw_cleaned_data['number_of_ratings']:
    if "K" in number_ratings:
    # This can also be used: if number_ratings[-1] == "K": 
        raw_cleaned_data.loc[raw_cleaned_data['number_of_ratings'] == number_ratings, 'number_of_ratings'] = number_ratings[0:-1:2]+"00"
        continue
   
raw_cleaned_data['number_of_ratings'] = raw_cleaned_data['number_of_ratings'].astype(int)
# If I find a better solution for this, I will replace it. 


# Splitting values in 'rllt__details' columns 

# Create new columns for values to be arranged into
    # raw_cleaned_data['closing_times'] = np.nan
    # raw_cleaned_data['opening_times'] = np.nan
    # raw_cleaned_data['price'] = np.nan
    # raw_cleaned_data['phone_number'] = np.nan
    # raw_cleaned_data['location'] = np.nan
    
raw_cleaned_data[['closing_times', 'opening_times','price', 'phone_number', 'location']] = np.nan

# Setting Columns data type to object
    # raw_cleaned_data['closing_times'] = raw_cleaned_data['closing_times'].astype(object)
    # raw_cleaned_data['opening_times'] = raw_cleaned_data['opening_times'].astype(object)
    # raw_cleaned_data['price'] = raw_cleaned_data['price'].astype(object)
    # raw_cleaned_data['phone_number'] = raw_cleaned_data['phone_number'].astype(object)
    # raw_cleaned_data['location'] = raw_cleaned_data['location'].astype(object)
    
raw_cleaned_data[['closing_times', 'opening_times', 'price', 'phone_number', 'location']] = raw_cleaned_data[['closing_times', 'opening_times', 'price', 'phone_number', 'location']].astype(object)

# Setting Columns data type to str to allow for loops
    # raw_cleaned_data['rllt__details 2'] = raw_cleaned_data['rllt__details 2'].astype(str)
    # raw_cleaned_data['rllt__details 3'] = raw_cleaned_data['rllt__details 3'].astype(str)
    # raw_cleaned_data['rllt__details 4'] = raw_cleaned_data['rllt__details 4'].astype(str)

raw_cleaned_data[['rllt__details 2','rllt__details 3','rllt__details 4']] = raw_cleaned_data[['rllt__details 2','rllt__details 3','rllt__details 4']].astype(str)

# Loop to funnel values into appropriate columns for each 'rllt__details' column
for details in raw_cleaned_data['rllt__details 2']:
    if details == "null": 
        continue
    elif "Closes" in details:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 2'] == details, 'closing_times'] = details
    elif "Opens" in details: 
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 2'] == details, 'opening_times'] = details
    elif "£" in details: 
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 2'] == details, 'price'] = details
    elif "07" in details:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 2'] == details, 'phone_number'] = details
    elif "020" in details:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 2'] == details, 'phone_number'] = details
    else:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 2'] == details, 'location'] = details
      
for details in raw_cleaned_data['rllt__details 3']:
    if details == "null": 
        continue
    elif "Closes" in details:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 3'] == details, 'closing_times'] = details
    elif "Opens" in details: 
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 3'] == details, 'opening_times'] = details
    elif "£" in details: 
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 3'] == details, 'price'] = details
    elif "07" in details:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 3'] == details, 'phone_number'] = details
    elif "020" in details:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 3'] == details, 'phone_number'] = details
    else:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 3'] == details, 'location'] = details
        
for details in raw_cleaned_data['rllt__details 4']:
    if details == "null": 
        continue
    elif "Closes" in details:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 4'] == details, 'closing_times'] = details
    elif "Opens" in details: 
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 4'] == details, 'opening_times'] = details
    elif "£" in details: 
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 4'] == details, 'price'] = details
    elif "07" in details:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 4'] == details, 'phone_number'] = details
    elif "020" in details:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 4'] == details, 'phone_number'] = details
    else:
        raw_cleaned_data.loc[raw_cleaned_data['rllt__details 4'] == details, 'location'] = details

# Dropping 'rllt__detail' columns 
drop_column_details = ['rllt__details 2', 'rllt__details 3', 'rllt__details 4']
        
raw_cleaned_data.drop(drop_column_details, inplace = True, axis = 1)

# Splitting 'closing_times' and 'opening_times' column to only have time 
raw_cleaned_data[['dot1', 'close','closing_time']] = raw_cleaned_data['closing_times'].str.split(' ', n = 2, expand = True)
raw_cleaned_data[['dot2', 'open','opening_time']] = raw_cleaned_data['opening_times'].str.split(' ', n = 2, expand = True)

# Dropping unesscessary details columns 
drop_columns_times = ['dot1', 'dot2','close','open', 'closing_times', 'opening_times']

raw_cleaned_data.drop(drop_columns_times, inplace = True, axis = 1)

# Most values in the 'price' column use £, ££ and £££ to indicate cost of product. 
# However, there are some values that give a range of '£1-10' which doesn't align with this. 
# From doing some research a single £ indicates a budget friendly shop with low prices usually from £5 - 10 
# And ££ indicates a mid range store and £££ for higher end 
# I'll be replacing values with '£1-10' with a single '£'.

# Changing '£1-10' values to £ in 'price' column
for x in raw_cleaned_data['price']: 
    if x == '£1–10': 
        raw_cleaned_data.loc[raw_cleaned_data['price'] == x, 'price'] = '£'
        continue


# Changing 'closing_time' and 'opening_time' columns to more readable/manipulatable formats
# Setting Columns data type to str to allow for loops

# Closing
# raw_cleaned_data['closing_am/pm'] = np.nan
raw_cleaned_data['closing_time'] = raw_cleaned_data['closing_time'].astype(str)

for x in raw_cleaned_data['closing_time']: 
    if x[-2:] == 'pm': 
        raw_cleaned_data.loc[raw_cleaned_data['closing_time'] == x, 'closing_am/pm'] = "pm"
    elif x[-2:] == 'am':
        raw_cleaned_data.loc[raw_cleaned_data['closing_time'] == x, 'closing_am/pm'] = "am"
    continue

for x in raw_cleaned_data['closing_time']: 
    if x[-2:] == 'pm' or x[-2:] == 'am': 
        raw_cleaned_data.loc[raw_cleaned_data['closing_time'] == x, 'closing_time'] = x[:-2]
    continue

for x in raw_cleaned_data['closing_time']: 
    if x != "None" and ':' not in x: 
        raw_cleaned_data.loc[raw_cleaned_data['closing_time'] == x, 'closing_time'] = x + ":00"
    continue

# Opening 
# raw_cleaned_data['opening_am/pm'] = np.nan
raw_cleaned_data['opening_time'] = raw_cleaned_data['opening_time'].astype(str)

for x in raw_cleaned_data['opening_time']: 
    if x[-2:] == 'pm': 
        raw_cleaned_data.loc[raw_cleaned_data['opening_time'] == x, 'opening_am/pm'] = "pm"
    elif x[-2:] == 'am':
        raw_cleaned_data.loc[raw_cleaned_data['opening_time'] == x, 'opening_am/pm'] = "am"
    continue

for x in raw_cleaned_data['opening_time']: 
    if x[-2:] == 'pm' or x[-2:] == 'am': 
        raw_cleaned_data.loc[raw_cleaned_data['opening_time'] == x, 'opening_time'] = x[:-2]
    continue

for x in raw_cleaned_data['opening_time']: 
    if x != "None" and ':' not in x: 
        raw_cleaned_data.loc[raw_cleaned_data['opening_time'] == x, 'opening_time'] = x + ":00"
    continue

# Removing · from 'phone_number' Columns 
raw_cleaned_data['phone_number'] = raw_cleaned_data['phone_number'].str.replace('·','')
raw_cleaned_data['phone_number'] = raw_cleaned_data['phone_number'].str.replace(' ','')

# Rearrange columns 
cleaned_data = raw_cleaned_data[[ 'shop_name',
                        'type_of_store',
                        'ratings',
                        'number_of_ratings',
                        'price',
                        'phone_number',
                        'location',
                        'closing_time',
                        'closing_am/pm',
                        'opening_time',
                        'opening_am/pm'
                       ]]

# Changing data types of each column 
    # cleaned_data['shop_name'] = cleaned_data['shop_name'].astype("string")
    # cleaned_data['type_of_store'] = cleaned_data['type_of_store'].astype("string")
    # cleaned_data['type_of_store'] = cleaned_data['type_of_store'].astype("string")
    # cleaned_data['phone_number'] = cleaned_data['phone_number'].astype("string")
    # cleaned_data['location'] = cleaned_data['location'].astype("string")
    # cleaned_data['closing_am/pm'] = cleaned_data['closing_am/pm'].astype("string")
    # cleaned_data['opening_am/pm'] = cleaned_data['opening_am/pm'].astype("string")

cleaned_data[[ 'shop_name',
                        'type_of_store',
                        'phone_number',
                        'location',
                        'closing_am/pm',
                        'opening_am/pm'
                       ]] = cleaned_data[[ 'shop_name',
                        'type_of_store',
                        'phone_number',
                        'location',
                        'closing_am/pm',
                        'opening_am/pm'
                       ]].astype("string")

# ----------------------------------------------------------------------------------------------------------------------------------

# Data Exploration 
# print(cleaned_data.isnull().sum().sum())
# Output: 
    # 462

# print(cleaned_data.isnull().sum())
# Output: 
    # shop_name              0
    # type_of_store          0
    # ratings                0
    # number_of_ratings      0
    # price                140
    # phone_number          64
    # location               2
    # closing_time           0
    # closing_am/pm         68
    # opening_time           0
    # opening_am/pm        188
    
# print(cleaned_data.isna().sum())
# Output: 
    # shop_name              0
    # type_of_store          0
    # ratings                0
    # number_of_ratings      0
    # price                140
    # phone_number          64
    # location               2
    # closing_time           0
    # closing_am/pm         68
    # opening_time           0
    # opening_am/pm        188
  
# 'type_of_store' We would assume all values in this column would be 'bubble tea store' but in fact there are diferent values.
# Checking values in 'type_of_store' 
values_in_tos = cleaned_data['type_of_store'].tolist()

# Running the code above produces all the values in 'type_of_store' - many values came back with empty spaces 
# Removing empty spaces 
cleaned_data['type_of_store'] = cleaned_data['type_of_store'].apply(lambda x: x.strip())

# Checking all unique values in 'type_of_store' column
values_in_tos = cleaned_data['type_of_store'].unique()
print(values_in_tos)

    # ['Bubble tea store' 'Dessert restaurant' 'Tea room' 'Tea Shop'
    #  'Dessert shop' 'Wholesaler' 'Cafe' 'Convenience Store' 'Shop'
    #  'Ice cream shop' 'Internet cafe']
    
    # Will need to check individually if stores labelled anything but 'bubble tea store' actually serves bubble tea.
    # But for now, all values that are not 'Bubble tea store' can be dropped
    
# cleaned_data.shape
    # Output: 
    # (191, 11)
    
# keeping rows where 'type of store' is 'Bubble tea store'
    
cleaned_data = cleaned_data[cleaned_data['type_of_store'] == 'Bubble tea store']

# Converting addresses to coordinates using geopy
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.extra.rate_limiter import RateLimiter

# Creating columns for latitude, longitude and location
cleaned_data[['latitude', 'longitude', 'location1']] = np.nan

# Testing if coordinates locator works
    # geolocator = Nominatim(user_agent="boba_tea_shop_coordinate_finder")
    # location = geolocator.geocode("23 Powis St")
    # print((location.latitude, location.longitude))
    
# Dropping duplicate locations
cleaned_data = cleaned_data.drop_duplicates('location')

# Dropping rows with no address
cleaned_data = cleaned_data.dropna(axis = 0, subset = 'location')

# Dropping shops where locations are not addresses
cleaned_data = cleaned_data.drop(cleaned_data[cleaned_data['location'] == 'Open'].index)
cleaned_data = cleaned_data.drop(cleaned_data[cleaned_data['location'] == 'nan'].index) 
cleaned_data = cleaned_data.drop(cleaned_data[cleaned_data['location'] == '⋅ 3 pm'].index) 
cleaned_data = cleaned_data.drop(cleaned_data[cleaned_data['location'] == 'Temporarily closed'].index)

# Finding coordinates for boba shop locations and adding it to latitude and longitude columns
geolocator = Nominatim(user_agent = "manalili.mig@gmail.com")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds = 1)
cleaned_data['location1'] = cleaned_data['location'].apply(geocode)

cleaned_data['latitude'] = cleaned_data['location1'].apply(lambda loc: loc.latitude if loc else None)
cleaned_data['longitude'] = cleaned_data['location1'].apply(lambda loc: loc.longitude if loc else None)

cleaned_data.dtypes
cleaned_data.head(100)

# Going over columns and dropping unecessary columns 
cleaned_data.columns.tolist()
'''
    ['shop_name',
    'type_of_store',
    'ratings',
    'number_of_ratings',
    'price',
    'phone_number',
    'location',
    'closing_time',
    'closing_am/pm',
    'opening_time',
    'opening_am/pm',
    'latitude',
    'longitude',
    'location1']
'''

columns_to_drop = ['type_of_store','location','closing_time','closing_am/pm','opening_time','opening_am/pm',]

cleaned_data = cleaned_data.drop(columns_to_drop, axis = 1)

cleaned_data.head(100)

# Placing Dataset into excel file 
# cleaned_data.to_excel('Bubble Tea Dataset.xlsx', index = False)