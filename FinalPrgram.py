# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 08:21:48 2016

@author: manisha_pc
"""

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt


log_file=input("enter log file name:")
df=pd.read_csv(log_file)

df['Connect']=df['Connect'].convert_objects(convert_numeric=True)
df['ElapseTime'] = pd.to_timedelta(df['ElapseTime'])

#range for admin 10.10.0.0 - 10.10.7.256
admin_pattern= re.compile(r'^10.10.[0-7].*$')

#range for som 10.10.8.0 - 10.10.15.256
som_pattern= re.compile(r'^10.10.1[0-5].*$')

#range for library 10.10.16.0 - 10.10.19.256
library_pattern= re.compile(r'^10.10.1[6-9].*$')

#range for kamban 10.10.20.0 - 10.10.23.256
kamban_pattern= re.compile(r'^10.10.2[0-3].*$')

#range for kavery 10.10.24.0 - 10.10.27.256
kavery_pattern= re.compile(r'^10.10.2[4-7].*$')

#range for voice 10.10.28.0 - 10.10.31.256
voice_pattern= re.compile(r'^10.10.(2[8-9])|(3[0-1]).*$')

#range for sb-II 10.10.32.0 - 10.10.47.256
sbII_pattern= re.compile(r'^10.10.(3[2-9])|(4[0-7]).*$')

#range for soss 10.10.48.0 - 10.10.63.256
soss_pattern1= re.compile(r'^10.10.(4[7-9])|(5[0-9]).*$')
soss_pattern2= re.compile(r'^10.10.6[0-3].\d+$')

#range for wireless 10.10.64.0 - 10.10.87.256
wireless_pattern1= re.compile(r'^10.10.(6[4-9])|(7[0-9]).*$')
wireless_pattern2= re.compile(r'^10.10.8[0-7].\d+$')

#range for static 10.10.88.0 - 10.10.256.256
static_pattern= re.compile(r'^10.10.8[0-9].*$')

admin_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))

som_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))
library_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))
kamban_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))
kavery_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))
voice_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))
sbII_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))
soss_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))
wireless_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))
static_df=pd.DataFrame(columns=('SourceIp','SiteName','Connect','Bytes','ElapseTime'))


#admin_counter=0
#som_counter=0
#library_counter=0
#kamban_counter=0
#kavery_counter=0
#voice_counter=0
#sbII_counter=0
#soss_counter=0
#wireless_counter=0
#static_counter=0


#        
def total(df):
    #print(df)
    total_usr = ((df["SourceIp"].unique())).tolist()
    print("Total_Users")
    print(len(total_usr))
   

    total_site = df["SiteName"].tolist()
    print("Total_sites")
    print(len(total_site))
   

    total_bytes = df["Bytes"].tolist()
    print("Total_Bandwidth_in Bytes")
    print(sum(total_bytes))

        
def ipGenByConnects(df):
    
    print("Generating ip reports...")
    
    aggregations={
               'Connect':'sum',
               'Bytes':'sum',
               'ElapseTime':'sum'         }
               
    df1=df.groupby('SourceIp',as_index=False).agg(aggregations)
    if(len(df1)<5):
        print("Very less data")
        print(df1)
    else:
        print("Ip with maximum no. of connection:\n")
        top10=df1.nlargest(10,'Connect')
        top10=top10.reset_index(drop=True)
        print(top10)
        
        df2=df1.nlargest(5,'Connect')
        df2 = df2.reset_index(drop=True)
        objects = df2["SourceIp"].head(5)
        y_pos = np.arange(len(objects))
        performance = df2["Connect"].head(5)
        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel('connects')
        plt.title('top 5 Users by Session')
        plt.tight_layout()
        plt.plot()
        fig=plt.gcf()
        plt.show()
        plt.draw()
        fig.savefig("topipConnectBar.png",  dpi=300)
        
        #pie chart
        label = (df2["SourceIp"].head(5))
        y = (df2["Connect"].head(5))
        plt.pie(y,labels=label,autopct="%1.1f%%")
        fig=plt.gcf()
        plt.show()
        plt.draw()
        fig.savefig("topipConnectpie.png",  dpi=300)
        
def ipGenByBytes(df):
    aggregations={
               'Connect':'sum',
               'Bytes':'sum',
               'ElapseTime':'sum'         }
               
    df1=df.groupby('SourceIp',as_index=False).agg(aggregations)
    if(len(df1)<5):
        print("Very less data")
        print(df1)
    else:
        print("Ip with Bytes:\n")
        top10=df1.nlargest(10,'Bytes')
        top10=top10.reset_index(drop=True)
        print(top10)
        
        df2=df1.nlargest(5,'Bytes')
        df2 = df2.reset_index(drop=True)
        objects = df2["SourceIp"].head(5)
        y_pos = np.arange(len(objects))
        performance = df2["Bytes"].head(5)
        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel('Bytes')
        plt.title('top 5 Users by Data Usage')
        plt.tight_layout()
        plt.plot()
        fig=plt.gcf()
        plt.show()
        plt.draw()
        fig.savefig("topipBytesBar.png",  dpi=300)
        
        #pie chart
        label = (df2["SourceIp"].head(5))
        y = (df2["Bytes"].head(5))
        plt.pie(y,labels=label,autopct="%1.1f%%")
        fig=plt.gcf()
        plt.show()
        plt.draw()
        fig.savefig("topipBytespie.png",  dpi=300)


def ipGenByElapseTime(df):
    aggregations={
               'Connect':'sum',
               'Bytes':'sum',
               'ElapseTime':'sum'         }
               
    df1=df.groupby('SourceIp',as_index=False).agg(aggregations)
    if(len(df1)<5):
        print("Very less data")
        print(df1)
    else:
        print("Ip with maximum no. of Time:\n")
        top10=df1.nlargest(10,'ElapseTime')
        top10=top10.reset_index(drop=True)
        print(top10)

def siteGenByConnects(df):
    aggregations={
               'Connect':'sum',
               'Bytes':'sum',
               'ElapseTime':'sum'         }
               
    df2=df.groupby('SiteName',as_index=False).agg(aggregations)
    
    if(len(df2)<5):
        print("Very less data")
        print(df2)
    else:
        print("Site with maximum no. of connection:\n")
        top10=df2.nlargest(10,'Connect')
        top10=top10.reset_index(drop=True)
        print(top10)
        
        df3=df2.nlargest(5,'Connect')
        df3=df3.reset_index(drop=True)
    
        objects = df3["SiteName"].head(5)
        y_pos = np.arange(len(objects))
        performance = df3["Connect"].head(5)
        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel('Connect')
        plt.title('top 5 Sites by Session')
        plt.tight_layout()
        plt.plot()
        fig=plt.gcf()
        plt.show()
        plt.draw()
        fig.savefig("topsiteConnectBar.png",  dpi=300)
        #pie chart
        label = (df3["SiteName"].head(5))
        y = (df3["Connect"].head(5))
        plt.pie(y,labels=label,autopct="%1.1f%%")
        fig=plt.gcf()
        plt.show()
        plt.draw()
        fig.savefig("topsiteConnectPie.png",  dpi=300)

def siteGenByBytes(df):
    aggregations={
               'Connect':'sum',
               'Bytes':'sum',
               'ElapseTime':'sum'         }
               
    df2=df.groupby('SiteName',as_index=False).agg(aggregations)
    
    if(len(df2)<5):
        print("Very less data")
        print(df2)
    else:
        print("Site with maximum Data Usage:\n")
        top10=df2.nlargest(10,'Bytes')
        top10=top10.reset_index(drop=True)
        print(top10)
        
        df3=df2.nlargest(5,'Bytes')
        df3=df3.reset_index(drop=True)
    
        objects = df3["SiteName"].head(5)
        y_pos = np.arange(len(objects))
        performance = df3["Bytes"].head(5)
        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel('Bytes')
        plt.title('top 5 Sites by Session')
        plt.tight_layout()
        plt.plot()
        fig=plt.gcf()
        plt.show()
        plt.draw()
        fig.savefig("topsiteBytesBar.png",  dpi=300)
        #pie chart
        label = (df3["SiteName"].head(5))
        y = (df3["Bytes"].head(5))
        plt.pie(y,labels=label,autopct="%1.1f%%")
        fig=plt.gcf()
        plt.show()
        plt.draw()
        fig.savefig("topsiteBytesPie.png",  dpi=300)  
        
def siteGenByElapseTime(df):
    aggregations={
               'Connect':'sum',
               'Bytes':'sum',
               'ElapseTime':'sum'         }
               
    df1=df.groupby('SiteName',as_index=False).agg(aggregations)
    if(len(df1)<5):
        print("Very less data")
        print(df1)
    else:
        print("Sites with maximum no. of Time:\n")
        top10=df1.nlargest(10,'ElapseTime')
        top10=top10.reset_index(drop=True)
        print(top10)                              

def reportGenerator(df):
    print("""Enter Report type
                1.Based on top IP
                2.Based on top Sites
                3.total
                4.return to main menu""")
    report_type=input("Your Choice: ")
    if(report_type=='3'):
        total(df)
        reportGenerator(df)
    if(report_type=='4'):
       option()     
    else:    
        print("""Select Quantifier
                1.No. Of Connects
                2.Data Usage
                3.ElapseTime""")
        quanti=input("Your Choice:")
    
        if (report_type=='1' and quanti=='1'):
            ipGenByConnects(df)
            reportGenerator(df)
        elif(report_type=='1' and quanti=='2'):
            ipGenByBytes(df)
            reportGenerator(df)
        elif(report_type=='1' and quanti=='3'):
            ipGenByElapseTime(df)
            reportGenerator(df)
        elif(report_type=='2' and quanti=='1'):
            siteGenByConnects(df)
            reportGenerator(df)
        elif(report_type=='2' and quanti=='2'):
            siteGenByBytes(df)
            reportGenerator(df)
        elif(report_type=='2' and quanti=='3'):
            siteGenByElapseTime(df)
            reportGenerator(df)
        else:
            exit()

def option():
    admin_counter=0
    som_counter=0
    library_counter=0
    kamban_counter=0
    kavery_counter=0
    voice_counter=0
    sbII_counter=0
    soss_counter=0
    wireless_counter=0
    static_counter=0
    print("""
        1.admin
        2.som
        3.library
        4.kamban
        5.kavery
        6.voice
        7.sbII
        8.soss
        9.wireless
        10.static
        11.exit
        """)
    selection=input("select option: ")

    if(selection=='1'):
        print("fetching admin area ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
    
            if re.match(admin_pattern,ip):
                admin_df.loc[admin_counter]=(df.loc[index])
                admin_counter+=1
        reportGenerator(admin_df)

    elif(selection=='2'):
        print("fetching som area ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
        
            if re.match(som_pattern,ip):
                som_df.loc[som_counter]=(df.loc[index])
                som_counter+=1
        reportGenerator(som_df)

    elif(selection=='3'):
        print("fetching library area ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
        
            if re.match(library_pattern,ip):
                library_df.loc[library_counter]=(df.loc[index])
                library_counter+=1
            
        reportGenerator(library_df)

    elif(selection=='4'):
        print("fetching kamban area ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
        
            if re.match(kamban_pattern,ip):
                kamban_df.loc[kamban_counter]=(df.loc[index])
                kamban_counter+=1
            
        reportGenerator(kamban_df)
    
    elif(selection=='5'):
        print("fetching kavery area ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
        
            if re.match(kavery_pattern,ip):
                kavery_df.loc[kavery_counter]=(df.loc[index])
                kavery_counter+=1
            
        reportGenerator(kavery_df)

    elif(selection=='6'):
        print("fetching voice ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
        
            if re.match(voice_pattern,ip):
                voice_df.loc[voice_counter]=(df.loc[index])
                voice_counter+=1
            
        reportGenerator(voice_df)

    elif(selection=='7'):
        print("fetching sbII area ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
        
            if re.match(sbII_pattern,ip):
                sbII_df.loc[sbII_counter]=(df.loc[index])
                sbII_counter+=1 
            
        reportGenerator(sbII_df)

    elif(selection=='8'):
        print("fetching soss area ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
        
            if re.match(soss_pattern1,ip) or re.match(soss_pattern2,ip):
                soss_df.loc[soss_counter]=(df.loc[index])
                soss_counter+=1
            
        reportGenerator(soss_df)
    
    elif(selection=='9'):
        print("fetching wireless ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
        
            if re.match(wireless_pattern1,ip) or re.match(wireless_pattern2,ip):
                wireless_df.loc[wireless_counter]=(df.loc[index])
                wireless_counter+=1
            
        reportGenerator(wireless_df)

    elif(selection=='10'):
        print("fetching static ip from log file...")
        for index,row in df.iterrows():
            ip=df['SourceIp'][index]
        
            if re.match(static_pattern,ip):
                static_df.loc[static_counter]=(df.loc[index])
                static_counter+=1
            
        reportGenerator(static_df)

    else:
        print("Exiting....")
        exit()

option()
