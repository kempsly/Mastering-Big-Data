import requests 

res = requests.get("https://quotes.toscrape.com/")
html = res.text
with open('Authors.txt','w',encoding='utf-8') as f:  
    for line in html.split("\n"):
        if '<small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '')
            author = line.strip()
            f.write(author)
            f.write('\n')