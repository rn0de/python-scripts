import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import certifi
import os

os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

def find_input_fields_and_parameters(url, visited=set()):
    # check if the url already visited
    if url in visited:
        return
    # add the current url to visited
    visited.add(url)
    # Make a GET request to the website with certifi
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all forms in the HTML
    forms = soup.find_all('form')
    # Iterate through each form
    for form in forms:
        # Check if the form uses the GET or POST method
        if form.get('method') in ['GET', 'POST']:
            # Find all input fields within the form
            inputs = form.find_all('input')
            # check if the form has any input fields
            if inputs:
                for input_field in inputs:
                    if input_field.get('name') in ['text', 'username', 'password', 'phone','userID']:
                        print(url)
                        with open('result.txt', 'a') as f:
                            f.write(f'{url} has {input_field.get("type")} type input field\n')
    # check if the url has parameters
    if '?' in url:
        with open('result.txt', 'a') as f:
            f.write(f'{url} has parameters\n')
    # Find all links within the HTML
    links = soup.find_all('a')
    # Iterate through each link
    for link in links:
        # Get the href attribute of the link
        href = link.get('href')
        # Check if the href is a valid URL
        if href and not href.startswith('http'):
            # construct the full url
            href = urljoin(url, href)
            # Check if the domain name of the link is the same as the initial URL
            parsed_url = urlparse(href)
            if parsed_url.netloc == urlparse(url).netloc:
                # Follow the link recursively
                find_input_fields_and_parameters(href, visited)
if __name__ == '__main__':
    initial_url = "https://redtm.com"
    find_input_fields_and_parameters(initial_url)
