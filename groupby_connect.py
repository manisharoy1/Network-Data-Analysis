# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 09:02:56 2016

@author: manisha-pc
"""

import pandas as pd
import matplotlib .pyplot as plt
df=pd.read_csv("newFile1_9th_may_2013.txt")
#df['Connect']=df['Connect'].convert_objects(convert_numeric=True)
#df['ElapseTime'] = pd.to_timedelta(df['ElapseTime'])
#print(df.dtypes)
aggregations={
           'Bytes':'sum',}
           
df1=df.groupby('SiteName',as_index=False).agg(aggregations)
print("Site with maximum bandwidth:\n")
top10=df1.nlargest(10,'Bytes')
print(top10)
colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]
plt.pie(
    top10['Bytes'].head(5),
    labels=top10['SiteName'].head(5),
    shadow=False,
    colors=colors,
    startangle=90,
   
    autopct='%1.1f%%',
    )
plt.tight_layout()
plt.show()
plt.savefig('fig9nov_Bytes.png')

