from selenium import webdriver
from bs4  import BeautifulSoup
import time
import csv

def website(url,filename):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get(url)
    
    content = driver.page_source
    soup = BeautifulSoup(content)
    #print(soup)
    contents = soup.findAll('div',href=False, attrs={'class':'cmpN txtC bdr1'})
    #print(len(contents))
    #to find contact no
    
    with open(r''+filename+".csv", 'a') as f:
        writer = csv.writer(f)    
        for content in contents:
            name = content.h2.text
            #print(name)
            c_number = soup.find('span',href=False, attrs={'class':'bo duet'}).text
            #print(c_number)
            fields = [name, c_number, url]
            writer.writerow(fields)

urlList = [
        'https://www.indiamart.com/proddetail/designer-rakhi-22312717273.html', 'https://www.indiamart.com/proddetail/designer-rakhi-availble-wholesale-price-22364069648.html', 'https://www.indiamart.com/proddetail/rakhi-22349673462.html', 'https://www.indiamart.com/proddetail/rakhis-traditonal-22379477133.html', 'https://www.indiamart.com/proddetail/fancy-rakhi-19705470948.html', 'https://www.indiamart.com/proddetail/white-stone-dora-rakhi-12356048062.html', 'https://www.indiamart.com/proddetail/rakhi-22391740833.html', 'https://www.indiamart.com/proddetail/photo-print-fancy-rakhi-21167326055.html', 'https://www.indiamart.com/proddetail/designer-rakhi-availble-wholesale-price-22364064497.html', 'https://www.indiamart.com/proddetail/brother-and-sister-rakhi-22379467873.html', 'https://www.indiamart.com/proddetail/traditional-rakhi-22379457412.html', 'https://www.indiamart.com/proddetail/rakhi-thread-22409242273.html', 'https://www.indiamart.com/proddetail/card-rakhi-21995067788.html', 'https://www.indiamart.com/proddetail/dori-rakhi-flag-collection-20868464530.html', 'https://www.indiamart.com/proddetail/rakhi-dori-19182594533.html', 'https://dir.indiamart.com/impcat/rakhi.html', 'https://www.indiamart.com/proddetail/fancy-zari-rakhi-19841080788.html', 'https://www.indiamart.com/proddetail/handmade-designer-rakhi-14968913297.html', 'https://www.indiamart.com/proddetail/handmade-bougainvillea-rakhi-6115180433.html', 'https://www.indiamart.com/proddetail/rakhi-22349746548.html', 'https://www.indiamart.com/proddetail/rakhi-22373978962.html', 'https://www.indiamart.com/proddetail/diamond-rakhi-22379446873.html', 'https://www.indiamart.com/proddetail/rakhi-21674795430.html', 'https://www.indiamart.com/proddetail/rainbow-arts-rakhi-016-21062204762.html', 'https://www.indiamart.com/proddetail/designer-kids-rakhi-20546958873.html'
        ]
for i in range(len(urlList)):
    filename = "rakhi seller info"
    website(urlList[i],filename)
    print(str(i) +" done")
    

