# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
os.chdir('e:\\2')
train = pd.read_csv("3.csv",sep='\t',header=None)
trainhead=train.head()
