#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:07:48 2020

@author: home
system specification: ubuntu, python 3.7
"""

from selenium import webdriver
from bs4  import BeautifulSoup
import time
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get("http://www.injectsolar.com/portal/#/login")
#time.sleep(10) it is used to enter credential 
time.sleep(10)

content = driver.page_source
soup = BeautifulSoup(content)
#print(soup)
contents = soup.findAll('div',href=False, attrs={'class':'col-md-3'})
power_gen = contents[2].div.h6.text #Get daily generation


driver.get("http://www.injectsolar.com/portal/#/inject-solar/errore-log")
#time.sleep(20) it is used to enter period for the report 
time.sleep(20)
content = driver.page_source
soup = BeautifulSoup(content)
#print(soup)
t_head_content = soup.findAll('th')
t_head = [i.text for i in t_head_content ]
t_row_content = soup.findAll('td')
t_row = [i.text for i in t_row_content]

#Databes
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='root',
                                         password='@Googlekeep1')
    
    
    create_table = """CREATE TABLE error_log(device VARCHAR(30) NOT NULL,
                          alarm VARCHAR(30) NOT NULL,
                          occuranceTime VARCHAR(30) NOT NULL,
                          message VARCHAR(30) NOT NULL
                          );"""
    
    cursor = connection.cursor()
    cursor.execute(create_table)
    connection.commit()
    print(cursor.rowcount, "Table Created Succesfully")
    cursor.close()

    """
    mySql_insert_query = "INSERT INTO error_log (device, alarm,occuranceTime, message) VALUES " + () 

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()
    """

except mysql.connector.Error as error:
    print("Connection Error {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")