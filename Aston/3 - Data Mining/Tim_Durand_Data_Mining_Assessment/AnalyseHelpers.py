# -*- coding: utf-8 -*-
"""
@author: durandt
"""

import pandas as pd
import re

# Visualisation
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [8.0, 5.0]
import seaborn as sns
sns.set(font_scale=1)

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
    meanlist = []
    minlist = []
    maxlist = []
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
        if df[c].dtypes == 'object':
            meanlist.append('N/A')
            minlist.append('N/A')
            maxlist.append('N/A')
        else:
            meanlist.append(df[c].mean())
            minlist.append(df[c].min()) 
            maxlist.append(df[c].max())
    profiledf = pd.DataFrame({'Column':collist, 'Max Length Value':vallistmax, 'Max Length':lenlistmax, 'Min Length Value':vallistmin, 'Min Length':lenlistmin, 'Null #': nulllist, 'Null %': nullpercentlist, 'Data Type': dtypelist, 'Unique Values': uniqueslist, 'Row Count':valcountlist, 'Mean':meanlist, 'Max':maxlist, 'Min':minlist})
    return profiledf


def dateprofile(s):
    x = re.sub("[a-zA-Z]", "a", s)
    x = re.sub("\d", "d", x)
    return x

def plot_grid_results(model, param = None, name = None):
    param_name = 'param_%s' % param

    # Extract information from the cross validation model
    #train_scores = model.cv_results_['mean_train_score']
    test_scores = model.cv_results_['mean_test_score']
    train_time = model.cv_results_['mean_fit_time']
    param_values = list(model.cv_results_[param_name])
    
    # Plot the scores over the parameter
    plt.subplots(1, 2, figsize=(10, 5))
    plt.subplot(121)
    #plt.plot(param_values, train_scores, 'bo-', label = 'train')
    plt.plot(param_values, test_scores, 'go-', label = 'test')
    #plt.ylim(ymin = -10, ymax = 0)
    plt.legend()
    plt.xlabel(name)
    plt.ylabel('Mean Test Score')
    plt.title('Score vs %s' % name)
    
    plt.subplot(122)
    plt.plot(param_values, train_time, 'ro-')
    #plt.ylim(ymin = 0.0, ymax = 2.0)
    plt.xlabel(name)
    plt.ylabel('Training Time (sec)')
    plt.title('Training Time vs %s' % name)

    plt.tight_layout(pad = 4)

def computecost(cm):
    df = cm.copy()
    df.iloc[0,0] = df.iloc[0,0] * 0
    df.iloc[0,1] = df.iloc[0,1] * 1
    df.iloc[1,0] = df.iloc[1,0] * 5
    df.iloc[1,1] = df.iloc[1,1] * 0
    return df
    
def fn_fp_comp(x):
    fnlist = []
    fplist = []
    modellist = []
    costlist = []
    acclist = []
    for k,v in x.items():
        fplist.append(v.iloc[0,1])
        fnlist.append(v.iloc[1,0])
        costlist.append(v.iloc[0,1] + (v.iloc[1,0] * 5))
        acclist.append((v.iloc[0,0]+ v.iloc[1,1])/ (v.values.sum()))
        modellist.append(k)
    return (pd.DataFrame({'Model':modellist, 'Cost' : costlist, 'False Positive' : fplist, 'False Negative' : fnlist, 'Accuracy':acclist}))
