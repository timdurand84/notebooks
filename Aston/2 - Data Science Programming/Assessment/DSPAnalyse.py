# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:57:00 2019

@author: durandt
"""

import pandas as pd
import re

def dataprofile(df):
    # Initalise empty lists
    collist = []
    vallistmax = []
    lenlistmax = []
    vallistmin = []
    lenlistmin = []
    nulllist = []
    nullpercentlist = []
    dtypelist = []
    uniqueslist = []
    valcountlist = []
    # For each column in df gather metrics on the data
    for c in df:
        field_length = df[c].astype(str).map(len)
        is_null = df[c].isnull().sum()
        per_null = round(is_null/df[c].shape[0]*100,2)
        valcount = df[c].shape[0]
        unique = df[c].nunique()
        types = str(df[c].dtypes)
        dtypelist.append(types.replace('object','string'))
        nulllist.append(is_null)
        nullpercentlist.append(per_null)
        uniqueslist.append(unique)
        collist.append(c)
        vallistmax.append(df.loc[field_length.values.argmax(), c])
        lenlistmax.append(max(field_length))
        vallistmin.append(df.loc[field_length.values.argmin(), c])
        lenlistmin.append(min(field_length))
        valcountlist.append(valcount)
    profiledf = pd.DataFrame({'Column':collist, 'Max Length Value':vallistmax, 'Max Length':lenlistmax, 'Min Length Value':vallistmin, 'Min Length':lenlistmin, 'Null #': nulllist, 'Null %': nullpercentlist, 'Data Type': dtypelist, 'Unique Values': uniqueslist, 'Row Count':valcountlist})
    return profiledf


def dateprofile(s):
    x = re.sub("[a-zA-Z]", "a", s)
    x = re.sub("\d", "d", x)
    return x


