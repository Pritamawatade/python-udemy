import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL="https://books.toscrape.com/"
START_PAGE="catalogue/page-1.html"
OUTPUT_PAGE="books_data.json"
TARGET_COUNT=70



def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Not able to fetch url")
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select('article.product_pod'):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price = article.select_one("p.price_color").text.strip()

        print(f"{title} - {price}")


scrape_page(BASE_URL)






