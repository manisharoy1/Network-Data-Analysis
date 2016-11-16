# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:54:45 2016

@author: 
"""
import pandas as pd

df = pd.read_csv("dfFile_new_9th_may_2013.txt")

for index, row in df.iterrows():
    with open('Cmplt_iplist_9th_may_2013.txt','a') as f:
        f.write(df["SourceIp"][index]+"\n")