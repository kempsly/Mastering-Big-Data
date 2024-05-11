from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")