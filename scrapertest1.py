from time import sleep

import requests
from bs4 import BeautifulSoup


def counter_pages(n):
    i = n // 20
    if n > 20 and n % 20 != 0:
        m = i + 1
    elif n > 20 and n % 20 == 0:
        m = i
    else:
        m = 1
    return m


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
}


url = "https://books.toscrape.com/index.html"
# url_ = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
root_url = "https://books.toscrape.com/"

response = requests.get(url, headers)
soup = BeautifulSoup(response.text, "lxml")
data = soup.find("ul", class_="nav nav-list")
links_ = data.find_all("a")
links = []
for link in links_:
    link_ = root_url + link.get("href")
    links.append(link_)

for page in links[1:]:
    sleep(1)
    response_page = requests.get(page, headers)
    soup_page = BeautifulSoup(response_page.text, "lxml")
    data_page = soup_page.find("form", class_="form-horizontal")
    counter_el = int(data_page.find("strong").text)
    print(page, "   :  ", counter_el, " : ", counter_pages(counter_el))

url_page7 = "https://books.toscrape.com/catalogue/category/books/default_15/index.html"

for i in range(1, 9):
    if i == 1:
        response_page7 = requests.get(url_page7, headers)
        soup_page7 = BeautifulSoup(response_page7.text, "lxml")
        data_page7 = soup_page7.find_all("article", class_="product_pod")

        for el in data_page7:
            image_src = el.find("img").get("src")
            index_image_src = image_src.rfind("..") + 3
            image_src_full = root_url + image_src[index_image_src:]
            print(image_src_full)
        print("--------------------------------------------------------------")
    else:
        url_page7 = f"https://books.toscrape.com/catalogue/category/books/default_15/page-{i}.html"
        soup_page7 = BeautifulSoup(response_page7.text, "lxml")
        data_page7 = soup.find_all("article", class_="product_pod")

        for el in data_page7:
            image_src = el.find("img").get("src")
            index_image_src = image_src.rfind("..") + 3
            image_src_full = root_url + image_src[index_image_src:]
            print(image_src_full)
        print("--------------------------------------------------------------")
# print(links[1:])

# data = soup.find_all("article", class_="product_pod")
# for el in data:
#    a_href = el.find("a").get("href")
#    index_a = a_href.rfind("..") + 3
#    card_url = root_url + "/catalogue" + a_href[index_a:]
#    card_response = requests.get(card_url)
#    card_soup = BeautifulSoup(card_response.text, "lxml")
#   card_data = card_soup.find("article", class_="product_page")
#   image_src = card_data.find("img").get("src")
#   index_image_src = image_src.rfind("..") + 3
#   image_src_full = root_url + image_src[index_image_src:]
#   print(image_src_full)
