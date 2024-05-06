import requests 

for i in range(1,11):
    url = f"https://quotes.toscrape.com/page/{i}/"
    r = requests.get(url)

    html = r.text
    with open('Authon_quotes.csv', 'a',encoding='utf-8') as f:
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
                quote = line.strip()
     
            if '<small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '')
                author = line.strip()
                
                result=author + ","+ quote 
                f.write(result)
                f.write("\n")