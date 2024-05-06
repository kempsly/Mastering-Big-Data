import requests 
import json


with open('Superstats.csv', 'w') as f:
    for i in range(1,3):
        url = f"https://www.espncricinfo.com//ci/content/story/data/index.json?genre=706;;page={i}"
        res = requests.get(url)
        # data = res.text
        data = json.loads(res.text)
        for headline in data:  
            newheadline = headline['headline']
            newheadline = newheadline.replace(",","")
            f.write(newheadline)
            f.write('\n')

            

