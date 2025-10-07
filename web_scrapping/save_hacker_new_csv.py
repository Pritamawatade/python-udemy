import os
import csv
import requests
from bs4 import BeautifulSoup

HN_URL="https://news.ycombinator.com/"
NEWS_FILE="hn_top20.csv"

def fetch_top_post():
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Network error \n ", e)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    post_links = soup.select('span.titleline > a')
    print(f"posts = {post_links}")

    links = []

    for link in post_links[:10]:
        title = link.text.strip()
        content = link.get('href').strip()
        links.append({"title": title, "content": content})
        
    return links

def save_to_csv(data):
    
    with open(NEWS_FILE, 'w', encoding="utf-8")as f:
        writer = csv.writer(f)
        writer.writerow(["title", "links"])

        for row in data:
            writer.writerow([row['title'], row['content']])
        


links = fetch_top_post()
print(f"\n\n\n links = {links}\n\n\n")

if links:
    save_to_csv(links)
    print(f"Data saved to {os.path.abspath(NEWS_FILE)}")
    
    