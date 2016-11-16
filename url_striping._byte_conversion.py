# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 06:17:56 2016

@author: manisha-pc
"""
import re
import pandas as pd


df = pd.read_csv("dfFile_new_24th_mar_2013.txt")

pattern1 = re.compile(r"^\d*[.]?\d*G$")
pattern2 = re.compile(r"^\d*[.]?\d*M$")
pattern3 = re.compile(r"^\d*[.]?\d*K$")
pattern4 = re.compile(r"^\d*[.]?\d*$")

for index,row in df.iterrows():
    url=df['SiteName'][index]
    
    byte=df['Bytes'][index]
#    print(row[7])
    par1 = re.compile(r'\d*\.\d*\.\d*\.\d*')
    domain1=re.findall(par1,url)
    domain1_str=''.join(domain1)
    par2=re.compile(r'\w*.com|\w*.net|\w*.org|\w*.info|\w*.coop|\w*.int|\w*.co\.uk|\w*.co\.in|\w*.org\.uk|ac\.uk|.uk')
    domain = (re.findall(par2,url))
    domain_str=''.join(domain)
    Tablelength = len(df.index)
    if  par1.findall(url):
        site_val=domain1_str
#        print(str(site_val))
    elif par2.findall(url):
        site_val = domain_str 
#        print(str(site_val)) 
##
        
    
#  
    if re.search(pattern1,byte):
        val=re.sub('G$',' ',byte)
        new_val= float(val)*1024*1024
#        print(new_val)
#        break
#        
    elif re.search(pattern2,byte):
        val=re.sub('M$','',byte)
        new_val=float(val)*1024
#        print(new_val)
        
    elif re.search(pattern3,byte):
        val=re.sub('K$','',byte)
        new_val=float(val)
#        print(new_val)
#        break
        
    elif re.search(r"^\d*[.]?\d*$",byte):
        val=pattern4.findall(byte)
        val_str=''.join(val)
        new_val=float(val_str)/1024
#        print(val_str)
#        
    with open("newFile2_24th_mar_2013.txt",'a')as f:
        f.write(row[0]+","+str(site_val)+","+row[2]+","+str(new_val)+","+row[7]+"\n")
#        print(row[0]+","+str(site_val)+","+row[2]+","+str(new_val)+","+row[7]+"\n")
print("done")               