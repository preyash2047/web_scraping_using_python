from selenium import webdriver
from bs4  import BeautifulSoup
import time
import csv

def website(url,filename):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get(url)
    time.sleep(30)
    
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


pages = 47
for i in range(1,pages):
    url = "https://www.justdial.com/Ahmedabad/B-Com-Tutorials/nct-10966967/page-"+str(i)
    filename = "bcom"
    website(url,filename)
    print("Page No "+ str(i) +" done")
    

