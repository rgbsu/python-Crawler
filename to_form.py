# -*- coding: UTF-8 -*-
import os
import re
import pandas as pd
rate = re.compile(r'\d+.\d.') 
SO2 = re.compile(r'二氧化硫')
CO = re.compile(r'一氧化碳')
O3 = re.compile(r'臭氧')
NO2 = re.compile(r'二氧化氮')
PM10 = re.compile(r'可吸入颗粒物')
PM25 = re.compile(r'细颗粒物')
particles = [SO2,CO,O3,NO2,PM10,PM25]

def getFileText(filename):
    with open(filename, 'r',encoding = 'utf-8') as f:
        s = {}
        line = f.readline()
        sentences = line.split('。')
        num_goodday = sentences[0].split('，')
      

        a = re.findall(r'\d+',num_goodday[-2])
        s['date']=[a[0]+'-'+a[1]]
        s['达标天数']=a[2]

        b = re.findall(r'\d+.\d.',num_goodday[-1])
        s['优良率'] = b[0]
        
        c = re.sub(r'、',r'；',sentences[-2])
        c = re.sub(r'，',r'；',c)
        # print(c)
        particle = c.split('；')
        # print(particle)

        

        # a = particles[1].match(particle[1])
        # print(a.group())
        for j in range(len(particle)):
            for i in particles:
                try:
                    a = i.search(particle[j])
                    if a:
                        s[a.group()]=rate.findall(particle[j])[-1]

                    # print(a.group())
                except:
                    continue
    
        return s
def main():
    file_path = 'air_condition'
    files = os.listdir('air_condition')
    # with open('','w',encoding = 'utf-8') as f:
    dataframe = pd.DataFrame({'date':'', '达标天数': '', '优良率': '', '二氧化硫': '', '一氧化碳': '', '二氧化氮': '', '细颗粒物': '', '可吸入颗粒物': '', '臭氧': ''},index = [0])
    # dataframe = pd.DataFrame()
    for i in range(len(files)):
        e = getFileText(os.path.join(file_path,files[i]))
      
        df2 = pd.DataFrame(e,index=[i+1])
        # print(df2)
        dataframe = pd.concat([dataframe,df2])
        # print(dataframe)
    dataframe.to_csv("test2.csv", index=False,sep=',')
main()