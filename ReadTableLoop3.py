# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 06:12:53 2016

@author: manisha-pc
"""
import pandas as pd
#import numpy as np

#url='http://10.10.80.5/squid-reports/31Jul2016-04Aug2016/topsites.html'
htmltext = pd.read_html('http://10.10.80.5/squid-reports/09May2013-09May2013/denied.html')
df=pd.DataFrame.from_records(htmltext[1])

#print (df)
#df2=df.to_csv(w 'c:\data\pandas.txt', header=None, index=None, sep=' ', mode='a')
df2 =pd.DataFrame.to_csv(df, sep="," ,header=None, index=None)
with open("denied_access_9th_may_2013.txt" , 'a') as f:
    f.write(df2)