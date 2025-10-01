import requests
from bs4 import BeautifulSoup

URL = "https://pritamm.tech"

def get_h2_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
    except requests.RequestException as e:
        print("Something went wrong..", {e})
        
    
    soup = BeautifulSoup(response.text, 'html.parser')

    h2_tags = soup.find_all("h2")

    print(h2_tags)
    tags = []

    for tag in h2_tags:
        
        hearder_text = tag.get_text()
        tags.append(hearder_text)
    
    print(tags)




get_h2_headers(URL)






