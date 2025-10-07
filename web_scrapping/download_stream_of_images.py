import os 
import requests
from urllib.parse import urljoin
import csv
import re
from bs4 import BeautifulSoup

BASE_URL="https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(name):
    return re.sub(r'[^\w\-_.]', "", name).replace(" ", "_")


def download_image(img_url, filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} - {e}")


def scrape_and_downloand_images():
    url = BASE_URL
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select('article.product_pod')[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    
    for book in books:
        title = book.h3.a['href']
        relative_image_url = book.find('img')['src'] 
        img_url = urljoin(BASE_URL, relative_image_url)

        print(f"Downloading image for {title} from {img_url}")
        filename = sanitize_filename(title) + ".jpg"

        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"Saving to... {filepath}")

        download_image(img_url, filepath)
    print("Download completed.")    

if __name__ == "__main__":
    scrape_and_downloand_images()   





