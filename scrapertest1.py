import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
root_url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
data = soup.find_all("article", class_="product_pod")
for el in data:
    a_href = el.find("a").get("href")
    index_a = a_href.rfind("..") + 2
    card_url = root_url + "/catalogue" + a_href[index_a:]
    card_response = requests.get(card_url)
    card_soup = BeautifulSoup(card_response.text, "lxml")
    card_data = card_soup.find("article", class_="product_page")
    image_src = card_data.find("img").get("src")
    index_image_src = image_src.rfind("..") + 2
    image_src_full = root_url + image_src[index_image_src:]
    print(image_src_full)
