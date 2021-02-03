from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import json
import os
import time



def Crawl_data(url):
# List to store a dict of the data we extracted
 extracted_records = []
 next_page = 1
 while True:
   print(next_page)
   main_url=url+"&page="+str(next_page)
   print(main_url)
   session = HTMLSession()
   r = session.get(main_url)
   r.html.render(timeout=8) #timeout can be adjusted to let the webpage load compeletely.
   soup = BeautifulSoup(r.html.raw_html, "html.parser")

   pages = soup.findAll(class_="page-item")
   Total_pages = len(pages)

   #content scrape
   products = soup.findAll("li", class_="b-catalogList__itm hasOverlay unit size1of3") #title
   for product in products:
      Brand_name = product.find('span', class_='brand-name').text  # Brand_name
      try:  #In case there is no discount for the product
        Actual_price = product.find('span', class_='b-catalogList__itmPrice old').text  # Actual_price
        Discounted_price = product.find('span',class_='b-catalogList__itmPrice special').text  # Discounted_price----must remove "NOW" from outputstring
        Discounted_price=Discounted_price.replace('NOW','')
      except:
        Actual_price = product.find('span', class_='b-catalogList__itmPrice').text  # Actual_price
        Discounted_price='Discount Not Available'

      Product_link = product.find('a', {'class': 'b-catalogList__itmLink itm-link'})['href']   # product_link
      link=("https://www.zalora.com.my/"+Product_link)

    #create function
      headers = {'User-Agent': 'Mozilla/5.0'}
      r = requests.get(link, headers=headers)
      soup = BeautifulSoup(r.text, "html.parser")
      try:
       div = soup.find(id="prdImage")
       Product_img_Link = (str(div['src']))
      except:
       Product_img_Link="Item not Available"

      #store a dict of the data we extracted for each product
      record = {
          'Brand': Brand_name,
          'ActualPrice': Actual_price,
          'Discounted_price': Discounted_price,
          'Product_img_link': Product_img_Link,
               }
      extracted_records.append(record)


   # write output to a JSON file

   if not os.path.isfile('data.json'):
       with open('data.json', mode='w') as f:
           f.write(json.dumps(extracted_records, indent=2))
           extracted_records=[]
   else:  #Update exisiting json file
       with open('data.json') as feedsjson:
           feeds = json.load(feedsjson)

       feeds.append(extracted_records)
       with open('data.json', mode='w') as f:
           f.write(json.dumps(feeds, indent=2))
           extracted_records=[]

   #Pagination code
   # Using try&except to handle url for crawling has only 1 page
   try:
     if pages[Total_pages - 1].text == ">":
       next_page = next_page+1
     else:
      break
   except:
       break


def main():
    Urls=['https://www.zalora.com.my/women/shoes/?from=header',
          'https://www.zalora.com.my/men/shoes/?from=header',
          'https://www.zalora.com.my/women/shoes/?from=header&occasion=Casual&brand=aldo']
    for url in  Urls:
        Crawl_data(url)
        time.sleep(4)



if __name__ == "__main__":
    main()
