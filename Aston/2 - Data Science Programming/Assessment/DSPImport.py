# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:37:06 2019

@author: durandt
"""
# Data manipulation
import pandas as pd

# Filehandling 
import os

# Function to combine all files in a given directory
def importcombine(datadir):
    # Get a list of all the files
    filelist = os.listdir(datadir)
    # For each file in the dir, read each one skipping the title at the top
    allfiles = [pd.read_excel(datadir + file, header=1) for file in filelist]
    # Combine the files into one dataframe
    df = pd.concat(allfiles,ignore_index=True)
    return df
