# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:51:29 2019

@author: durandt
"""
# Data manipulation
import pandas as pd

# Dates
from datetime import datetime

# Cleanse x < 0
def cleanseltzero(x):
    if x < 0:
        x = 0
    return x

# Cleanse x > 1
def cleansegtone(x):
    if x > 1:
        x = 1
    return x

# Cleanse column names
def cleansecolumns(df):
    try:
        # Get a list of the columns 
        oldcolumns = list(df.columns)
        # Replace spaces with underscores and brackets with empty. Also format to title case for each string in the list
        newcolumns = [column.replace(" ","_").replace("(","").replace(")","").title() for column in oldcolumns]
        # Assign the new columns to the dataframe
        df.columns = newcolumns
        return df
    except Exception as e:
        print(e)

# Cleanse Categories
def cleansecategories(s):
    try:
        s.str.title()
        return s
    except Exception as e:
        print(e)

# Cleanse Decimals
def cleansedecimals(s):
   try:
        # Replace commas with points and points with with empty for each string in the list
        x = s.replace(".","")
        x = x.replace(",",".")
        return x
   except Exception as e:
        print(e)
        
# Cleanse Decimals
def reduceby1000(n):
   try:
        # Replace commas with points and points with with empty for each string in the list
        if n > 1000:
           x=  n / 1000
        else:
            x=n
        return x
   except Exception as e:
        print(e)


def testdates (datetotest,inputformat):
    """
    Define a function to determine if a date conforms to "%d/%m/%Y" 
    """
    try:
        datetime.strptime(datetotest, inputformat).strftime("%Y-%m-%d %H:%M:%S")
        # Results will be added to a list of unparsable dates so need to return false
        return False
    except Exception as e:
        # Return true if unable to parse
        return True
"""
Define a function to Convert dates to "%Y-%m-%d %H:%M:%S" 
Accepts a list; first element is the date to be converted, the second element is the expected format
"""
def convertdates (x):
    try:
        datetotest = x[0]
        inputformat = x[1]
        if inputformat == 'excel':
            y = pd.to_datetime('1899-12-30') + pd.DateOffset(days=int(datetotest))
        else:
            y = datetime.strptime(datetotest, inputformat).strftime("%Y-%m-%d %H:%M:%S")
        return y
    except Exception as e:
        print(e)
