# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 03:53:47 2016

@author: Avin
"""

import pandas as pd
import urllib

#importing list of sites to iterate
df = pd.read_csv("dfFile_new_9th_may_2013.txt")

#importing list to ip to iterate
df2= pd.read_csv("Cmplt_iplist_9th_may_2013.txt")

#counting total data saved
foundSite=0
notfound=0
nohostname = 0

#for loop for all the site list in file
for index, row in df.iterrows():
    site_val=df["SiteName"][index]
    ip_val=df2["ip_list"][index]
    try:
        url="http://10.10.80.5/squid-reports/09May2013-09May2013/%s/tt%s-%s.html"%(ip_val,ip_val,site_val)
        print("Copy Table from %s ..."%(url) )
        SitePage = pd.read_html(str(url))
        
        foundSite=foundSite+1
        
        SiteTable = pd.DataFrame.from_records(SitePage[1])
        TableLen=len(SiteTable.index)
        i=1
        with open('doc_9th_may_2013.txt','a') as f:
            while(TableLen>1):
                f.write(df["SourceIp"][index]+","+SiteTable[0][i]+","+SiteTable[1][i]+","+SiteTable[2][i]+"\n")
                TableLen=TableLen-1
                i=i+1
    except urllib.error.HTTPError:
        print("Site Not found")
        nohostname=nohostname+1
        continue

print("Total record found: %s"%(foundSite))
print("Total record not found: %s"%(notfound))
print("Total hostname not found: %s"%(nohostname))