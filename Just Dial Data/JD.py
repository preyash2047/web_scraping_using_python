#!/usr/bin/env python
# coding: utf-8

# In[31]:


from selenium import webdriver
from bs4  import BeautifulSoup
import time
import csv

def website(url,filename):
    driver = webdriver.Chrome("C:/chromedriver.exe")
    driver.get(url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    time.sleep(10)
    
    content = driver.page_source
    soup = BeautifulSoup(content)
    #print(soup)
    contents = soup.findAll('div',href=False, attrs={'class':'col-sm-5 col-xs-8 store-details sp-detail paddingR0'})
    print(len(contents))
    #to find contact no
    switcher = {
        'dc':"+",
        'fe':"(",
        'ji':"9",
        'yz':"1",
        'hg':")",
        'ba':"-",
        'ac':"0",
        'yz':"1",
        'wx':"2",
        'vu':"3",
        'ts':"4",
        'rq':"5",
        'po':"6",
        'nm':"7",
        'lk':"8",
        'ji':"9"
    }
    
    with open(r''+filename+".csv", 'a') as f:
        writer = csv.writer(f)    
        for content in contents:
            name = content.a.text
            address = content.find('span',href=False, attrs={'class':'cont_fl_addr'}).text
            x = str(content.find('p',href=False, attrs={'class':'contact-info'})).split("mobilesv icon-")
            x = [i[0:2] for i in x[1:]]
            c_number = ""
            for i in x:
                c_number += switcher.get(i)
            #print(f"Name: {name}\nAddress: {address}\nContact No: {c_number}\n")
            fields = [name, address, c_number]
            writer.writerow(fields)
    return contents

