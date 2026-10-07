import requests
import pandas as pd
from bs4 import BeautifulSoup


response = requests.get("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
print(response)



soup = BeautifulSoup(response.content,'html.parser')
# print(soup)




names = soup.find_all('div',class_ ='RG5Slk')
# print(names)

name = []
for i in names[0:10]:
    a = i.get_text()
    name.append(a)
print(name)




actual_prices = soup.find_all('div',class_ ='kRYCnD')
# print(actual_prices)

actual_price = []
for j in actual_prices[0:10]:
    b = j.get_text()
    actual_price.append(b)
print(actual_price)





discount_prices = soup.find_all('div',class_ ='hZ3P6w DeU9vF')
# print(discount_prices)

discount_price = []
for k in discount_prices[0:10]:
    c = k.get_text()
    discount_price.append(c)
print(discount_price)




# storages = soup.find_all('li',class_ ='DTBslk')
# print(storages)

storage = []
products = soup.find_all('ul', class_='HwRTzP')

for product in products[:10]:
    first_li = product.find('li')

    d = first_li.get_text()
    storage.append(d)

print(storage)
    
    




ratings = soup.find_all('div',class_ = 'MKiFS6')
# print(ratings)
rate = []
for i in ratings[0:10]:
    d = i.get_text()
    rate.append(float(d))
print(rate)






df = pd.DataFrame()

df["Names"] = name
df["Storage"] = storage
df["Ratings"] = rate
df["Actual Prices"] = actual_price
df["Discount Price"] = discount_price

print(df)
df.to_csv("Top 10 Mobiles.csv")



