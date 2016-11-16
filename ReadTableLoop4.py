# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 03:40:38 2016

@author: manisha-pc
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 03:24:11 2016

@author: 
"""

import pandas as pd

dproxy=pd.read_csv("urlproxy_list_9th_nov_2016.txt")
for index,row in dproxy.iterrows():
    site_val=row[0]
    site_val1=row[1]
    url="http://10.10.80.5/squid-reports/09Nov2014-11Nov2014/%s/tt%s-%s.html"%(site_val,site_val,site_val1)
    print(url)
       
