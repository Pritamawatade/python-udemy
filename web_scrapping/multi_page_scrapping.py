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

        books.append({"title": title, "price": price})
        
    next_link = soup.select_one("li.next > a")
    # next_link.get("href") if next_link else None
    urljoin(url,next_link.get("href")) if next_link else None

    return books, next_link


scrape_page(BASE_URL)




def main():
    collected = []
    current_url = urljoin(BASE_URL, START_PAGE)
    while len(collected) < TARGET_COUNT and current_url:
        print(f"Scraping {current_url}...")
        books, next_page = scrape_page(current_url)
        collected.extend(books)
        current_url = next_page
        print(f"Collected {len(collected)} books so far...")
        
    with open(OUTPUT_PAGE, "w", encoding="utf-8") as f:
        json.dump(collected[:TARGET_COUNT], f, ensure_ascii=False, indent=4)
    print(f"Data saved to {OUTPUT_PAGE}")
    
    
if __name__ == "__main__":
    main()
