import requests
from bs4 import BeautifulSoup
from time import sleep


for count in range(1, 51):
    sleep(2)
    url = f"https://books.toscrape.com/catalogue/page-{count}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for i in data:
        name = i.find("h3").text
        price = i.find("div", class_="product_price")
        price_1 = price.find("p").text.replace("Â£", "")
        url_img = "https://books.toscrape.com/" + i.find("img").get("src")
        print(name, price_1, url_img, sep='\n', end='\n\n')



