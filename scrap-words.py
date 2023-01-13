import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

visited = []

words = []

def web_words(url):
    if url in visited:
        return
    visited.append(url)
    print(f'Scraping {url}')

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    elements = soup.find_all(text=True)
    for element in elements:
        text = element.strip()
        for word in text.split():
            word = re.sub(r'^[^a-zA-Z0-9]*|[^a-zA-Z0-9]*$', '', word)
            if len(word) >= 4 and len(word) <= 10:
                words.append(word)
    links = soup.find_all('a')
    for link in links:
        if 'href' in link.attrs:
            new_url = link.get('href')
            if urlparse(new_url).netloc == urlparse(url).netloc or new_url.startswith('/'):
                if new_url.startswith('/'):
                    new_url = urlparse(url).scheme + "://" + urlparse(url).netloc + new_url
                scrape_website(new_url)

start_url = 'https://redtm.com'

web_words(start_url)

words = list(set(words))

with open('words.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')

print(f'{len(words)} words written to file.')
