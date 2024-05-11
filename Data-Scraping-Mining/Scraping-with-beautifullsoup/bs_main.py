from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
# print(soup.title.string)
# print(soup.title.parent)
# print(soup.title.parent.name)
# print(soup.span.string)

# for tag in soup.findAll('a'):
#     print(tag)
# print(soup.findAll('a'))
# print("_________________________________________")
# print(soup.findAll('span'))

with open('bs4quotes.txt', 'w') as f:
    
    for tag in soup.findAll('span', {'class':'text'}):
        f.write(tag.string)
        f.write('\n')