# coding=utf-8 
from selenium import webdriver 
import re 
import time 
import os 
import math
import pandas as pd
import numpy as np
print ("start") 
#打开Firefox浏览器 设定等待加载时间 
driver = webdriver.Firefox() #定位节点 
url = 'http://hbj.wuhan.gov.cn/viewAirDarlyForestWaterInfo.jspx' 
print (url) 
driver.get(url) 
#切换到表格
driver.switch_to_frame("iframepage")
area = driver.find_element_by_xpath("//select[@id='typedictionary' and @name='Dic']/option[13]" )
area.click()
#输入时间
driver.find_element_by_id('cdateBeginDic').send_keys('2018-01-01')
driver.find_element_by_id('cdateEndDic').send_keys('2018-10-28')

driver.find_element_by_xpath("//a[@href = '#' and @onclick='toQuery(2);']").click()#点击查询
time.sleep(5)#等待5秒刷新
num_itesms = driver.find_element_by_xpath("//div[@class='serviceitempage fr']/span[@class='fl']").text
num = re.match(r'\d+',num_itesms).group()
pages_num = math.ceil(int(num)/22)
i=1
with open('b.txt','w',encoding='utf-8') as f:
    while i<=pages_num:
        
        driver.find_element_by_id('goPag').send_keys(str(i))
        driver.find_element_by_id('_goPag').click()#跳转到下一页
        time.sleep(5)
        i=i+1
        content = driver.find_elements_by_xpath("//tbody/tr/td")#找到提取内容
        k=1
        for u in content:
            if k%12!=0:
                f.write(u.text+' ')
                k=k+1
            else:
                f.write(u.text+'\n')
                k=k+1
        

    
    
