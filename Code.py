import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Apple-iPhone-7-Silver-32GB/dp/B01LZWFVHL/ref=sr_1_6?dchild=1&keywords=iphone&qid=1604473386&sr=8-6'

headers={"User-Agent" : 'Your user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/86.0.4240.111 Safari/537.36'}

page= requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content,'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_dealprice").get_text()
temp = price[2:4]
temp1 = price[5:8]
converted_price = int(temp+temp1)
print(converted_price)
if(converted_price > 24998):
    print("Price has been droped \n")
    print(URL+"\n")
else:
    print("Price Not droped")