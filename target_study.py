from selenium import webdriver
from bs4  import BeautifulSoup
import time
import csv

def website(url,filename):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get(url)
    #time.sleep(30)
    
    content = driver.page_source
    soup = BeautifulSoup(content)
    #print(soup)
    contents = soup.findAll('div',href=False, attrs={'class':'card pmd-card college-card'})
    print(len(contents)) 
    with open(r''+filename+".csv", 'a') as f:
        writer = csv.writer(f)    
        for content in contents:
            name = content.a.text
            sub_content = content.findAll('p',href=False, attrs={'class':'card-subtitle mt-0'})
            if len(sub_content) == 2:
                address = str(sub_content[0].text)
                address = address.replace("location_on ", "")
                address = address.replace(" ","")
                address = address.replace("\n","")
                c_number = str(sub_content[1].text)
                c_number = c_number.replace("call", "")
                c_number = c_number.replace("phone_iphone ", "")
                c_number = c_number.replace(" ","")
                c_number = c_number.replace("\n","")
                fields = [name, address, c_number]
                writer.writerow(fields)
            else:
                address = str(sub_content[0].text)
                address = address.replace("location_on ", "")
                address = address.replace(" ","")
                address = address.replace("\n","")
                fields = [name, address, ""]
                writer.writerow(fields)

urls = ["https://targetstudy.com/coaching/mcom-coaching-in-ahmedabad.htm",
        "https://targetstudy.com/coaching/mcom-coaching-in-ahmedabad.htm?recNo=20",
        "https://targetstudy.com/coaching/mcom-coaching-in-ahmedabad.htm?recNo=40" ,
        "https://targetstudy.com/coaching/mcom-coaching-in-ahmedabad.htm?recNo=60", 
        "https://targetstudy.com/coaching/mcom-coaching-in-jamnagar.htm",
        "https://targetstudy.com/coaching/mcom-coaching-in-kutch.htm" ,
        "https://targetstudy.com/coaching/mcom-coaching-in-porbandar.htm" ,
        "https://targetstudy.com/coaching/mcom-coaching-in-rajkot.htm" ,
        "https://targetstudy.com/coaching/mcom-coaching-in-surat.htm" ,
        "https://targetstudy.com/coaching/mcom-coaching-in-vadodara.htm" ,
        "https://targetstudy.com/coaching/mcom-coaching-in-palanpur.htm"]
for i in urls:
    website(i,"targetstudy mcom")