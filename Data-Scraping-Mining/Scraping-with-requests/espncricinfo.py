import requests 
import json


# url = "https://www.espncricinfo.com//ci/content/story/data/index.json/?;type=7;page=8"
# res = requests.get(url)
# data = json.loads(res.text)
# for news in data:
#     print(data['author'], news['summary'])
with open('News.txt', 'w') as f:
    for i in range(1, 6):   
        url = f"https://www.espncricinfo.com//ci/content/story/data/index.json/?;type=7;page={i}"
        res = requests.get(url)
        data = json.loads(res.text)

        for news in data:
            f.write(news['author'] + '|' + news['summary'])
            f.write('\n')
            

