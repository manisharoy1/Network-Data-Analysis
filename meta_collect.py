# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 07:01:33 2016

@author: manisha-pc
"""
import re
import pandas as pd
import urllib
import urllib.request as ur
from lxml import etree
import numpy
df = pd.read_csv("site_user_9th_may_2013.txt")

#print (length)
foundSite=0
notfound=0

for index,row in df.iterrows():
    url=df['ACCESSED_SITE'][index]

    pattern=re.compile(r':443$')
    par1 = re.compile(r'\d*\.\d*\.\d*\.\d*')
    domain1=re.findall(par1,url)
    domain1_str=''.join(domain1)
    par2=re.compile(r'\w*.com|\w*.net|\w*.org|\w*.info|\w*.coop|\w*.int|\w*.co\.uk|\w*.co\.in|\w*.org\.uk|ac\.uk|.uk')
    domain = (re.findall(r'\w*.com|\w*.net|\w*.org|\w*.info|\w*.coop|\w*.int|\w*.co\.uk|\w*.co\.in|\w*.org\.uk|ac\.uk|.uk',url))
    domain_str=''.join(domain)
#    print(domain1_str)
#    print(domain1_str)
    Tablelength = len(df.index)
##    print(Tablelength)
#    #print(domain_str)
    if pattern.findall(url) and par1.findall(url):
        site_val="https://"+domain1_str
#        print(str(site_val))
    elif pattern.findall(url) and par2.findall(url):
        site_val = "https://"+domain_str 
#        print(str(site_val)) 
    else:     
        if par2.findall(url):
            site_val="http://"+domain_str
#            print(str(site_val))
        else: 
            site_val="http://"+domain1_str
#            print(str(site_val))
    try:
        print("Collecting metadata  of  %s"%(site_val ))
        htmlfile = ur.urlopen(str(site_val))
        htmltext = htmlfile.read()
        tree = etree.HTML(htmltext)
        m = tree.xpath( "//meta" )
       
        for i in m:
            meta = etree.tostring(i)
#            print (etree.tostring( i ))
            with open ("meta_file.txt",'a') as f:
                while(Tablelength>1):
                    f.write(str(site_val) +","+str(meta)+"\n")
                    Tablelength=Tablelength-1
                  
    
    except urllib.error.HTTPError:
        
        print("Site Not found")
        notfound = notfound +1
        continue
    except urllib.error.URLError:
        print("No Host Name")
        notfound = notfound + 1  
        continue
print("Total record found: %s"%(foundSite))
print("Total record not found: %s"%(notfound))   