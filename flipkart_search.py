from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request

my_url = Request('https://www.flipkart.com/search?q=milton+bottle&sid=upp%2Cf2k%2C0zz&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_9_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_9_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=milton+bottle&requestId=1bf34864-8809-4e05-b0a3-3f797c784048&as-backfill=on',
                 headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(my_url).read()

uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll('div', {'class':'_3liAhj _1R0K0g'})
#print (len(containers))

#for testing purpose
"""
print(soup.prettify(containers[0]))

container = containers[0]
print(container.div.img['alt'])

price = container.findAll("div", {"class":"_1vC4OE"})
print(price[0].text)

ratings = container.findAll("div", {"class":"hGSR34"})
print(ratings[0].text)
"""

filename = "products.csv"
f = open(filename,"w")

headers = "Product_Name, Pricing ,Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]
    #print(product_name)
    
    price_container = container.findAll("div", {"class":"_1vC4OE"})
    price = price_container[0].text.strip()
    
    
    rating_container = container.findAll("div", {"class": "hGSR34"})
    rating = rating_container[0].text
    

    #print ("product name:" + product_name)
    #print( "price:" + price)
    #print ( "ratings:" + rating)
    
    #string parsing
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split('₹')
    
    add_rs_price = "Rs." + rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]
    
    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    #print(product_name.replace(",", "|") + final_price.replace(",", "|") + "\n")#final_rating.replace(",", "|") + "\n")    
    f.write(product_name.replace(",", "|") + "," + final_price + "\n")#final_rating.replace(",", "|") +  "\n")    

f.close()