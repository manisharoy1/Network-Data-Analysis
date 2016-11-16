# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:45:38 2016

@author:
"""

import pandas as pd
df=pd.read_csv("newFile1_9th_may_2013.txt")
df['Connect']=df['Connect'].convert_objects(convert_numeric=True)
df['ElapseTime'] = pd.to_timedelta(df['ElapseTime'])
#print(df.dtypes)
aggregations={
           'Connect':'sum',
           'Bytes':'sum',
           'ElapseTime':'sum'         }
           
df1=df.groupby('SiteName',as_index=False).agg(aggregations)

print("Sites with maximum no. of connection:\n")
top100=df1.nlargest(100,'Connect')
#print(type(top100))
for i,row in top100.iterrows():
    with open('top_connect_9th_may.txt','a') as f:
        f.write(str(top100['SiteName'][i])+","+str(top100['Bytes'][i])+","+str(top100['Connect'][i])+","+str(top100['ElapseTime'][i])+"\n")
    
print("Sites with maximum no. of Bytes:\n")
top100=df1.nlargest(100,'Bytes')
#print(top100)
for i,row in top100.iterrows():
    with open('top_bytes_9may.txt','a') as f:
        f.write(str(top100['SiteName'][i])+","+str(top100['Bytes'][i])+","+str(top100['Connect'][i])+","+str(top100['ElapseTime'][i])+"\n")
    

print("Sites with maximum no. of ElapseTime:\n")
top100=df1.nlargest(100,'ElapseTime')
#print(top100)
for i,row in top100.iterrows():
    with open('top_elapsetime_9may.txt','a') as f:
        f.write(str(top100['SiteName'][i])+","+str(top100['Bytes'][i])+","+str(top100['Connect'][i])+","+str(top100['ElapseTime'][i])+"\n")
    