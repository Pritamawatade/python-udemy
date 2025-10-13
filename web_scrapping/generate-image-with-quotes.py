import os
from bs4 import  BeautifulSoup
import requests
import textwrap
from PIL import Image, ImageDraw, ImageFont


URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "output_images"

def fetch_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select("div.quote")   
    quotes_data = []
    for q in quotes[:5]:
        text = q.find("span", class_="text").text.strip("“”")
        author = q.find("small", class_="author").text
        quotes_data.append((text, author))
    return quotes_data

def create_image_with_quote(quote, author, index):
    WIDTH, HEIGHT = 600,300
    background_color = "#0D0F0F"
    text_color = "#CECACA"
    image = Image.new("RGB", (WIDTH, HEIGHT), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    authot_font = ImageFont.load_default()
    
    wrapped = textwrap.fill(quote, width=60)
    author_text = f"- {author}"
    
    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)
    
    y_text += wrapped.count("\n") * 15 + 40
    draw.text((500, y_text), author_text, font=font, fill=text_color)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    image.save(f"{OUTPUT_DIR}/quote_{index + 1}.png")


def scrape_and_generate_images():
    quotes = fetch_quotes(URL)
    for index, (quote, author) in enumerate(quotes):
        create_image_with_quote(quote, author, index)
        print(f"Generated image for quote {index + 1}")

if __name__ == "__main__":
    scrape_and_generate_images()