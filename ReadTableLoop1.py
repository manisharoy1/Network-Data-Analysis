# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 03:24:11 2016

@author: 
"""

import pandas as pd

dproxy=pd.read_csv('dfFile_proxy_list_24th_mar_2013.txt')
dproxy_list = pd.read_csv('dfFile_dproxy_list_24th_mar_2013.txt')
ip_list = dproxy_list["proxy_list"].tolist()

for index, row in dproxy.iterrows():
    site_val = row[0]
    j=index
    print(site_val)
    url="http://10.10.80.5/squid-reports/24Mar2013-26Mar2013/%s/%s.html"%(site_val,site_val)
    print("Writing Table From "+url+".....")
    df = pd.read_html(str(url))
    df2 = pd.DataFrame.from_records(df[1])
    
    #df2.drop(df2.columns[[0,5,10]], axis=1, inplace=True)
    abc=len(df2.index)
    i=1
    with open('dfFile_new_24th_mar_2013.txt', 'a') as f:
        while(abc>3):
            f.write(ip_list[j]+","+df2[1][i]+","+df2[2][i]+","+df2[3][i]+","+df2[4][i]+
            ","+df2[5][i]+","+df2[6][i]+","+df2[7][i]+","+df2[8][i]+","+df2[9][i]+"\n")
            abc = abc - 1
            i = i + 1
