import requests
from bs4 import BeautifulSoup
import csv


url='https://www.newegg.com/Drones/SubCategory/ID-3708?cm_sp=Cat_Drones_1-_-VisNav-_-Drones//c1.neweggimages.com/WebResource/Themes/2005/Nest/logo_424x210.png'
html_data=requests.get(url)
soup=BeautifulSoup(html_data.text,'html.parser')
all_div=soup.find('div',class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
for item in all_div:
    title=item.find('a',class_='item-title').text
    link=item.find('a',class_='item-title').get('href')
    price_ul=item.find('ul',class_='price')
    price_li=price_ul.find('li',class_='price-current')
    try:
        price=price_li.find('strong').text
    except:
        price=''
    seller_div=item.find('div',class_='item-branding')
    seller_img=seller_div.find('img')
    try:
        seller=seller_img['title']
    except:
        seller=''
    rating=item.find('a',class_='item-rating')
    try:
        rated=rating['title']
    except:
        rated=''
    data={
        'Product_title':title,
        'Price':price,
        'Seller':seller,
        'Rated':rated,
        'Link':link
    }
    with open('scraped_info.csv','a') as file:
        writer=csv.writer(file)
        rows=[data['Product_title'],data['Price'],data['Seller'],data['Rated'],data['Link']]
        writer.writerow(rows)


