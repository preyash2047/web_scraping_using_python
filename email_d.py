from selenium import webdriver
from bs4  import BeautifulSoup
import time
import csv
import re
import pandas as pd

data_file = pd.read_csv("datat.csv")
final_email_list = pd.DataFrame(columns=['college','url','email'])
final_email_list



for i in range(len(data_file.url)):
    try:
        driver = webdriver.Chrome("c:\chromedriver.exe")
        driver.get(data_file.url.iloc[i])
        time.sleep(30)
        
        content = driver.page_source
        soup = BeautifulSoup(content)
        
        #getting email
        temp_email_list = re.findall(r'[\w\.-]+@[\w\.-]+', soup)
        email_text = ""
        for j in temp_email_list:
          email_text += j+", "
        
        final_email_list.loc[i] = [data_file.Coollege.iloc[i], data_file.url.iloc[i], email_text]
        
    
    except:
        print(data_file.url.iloc[i])
