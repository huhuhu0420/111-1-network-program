import json
import urllib.request

url = 'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json/preview'
jsonFile = 'bike.json'
urllib.request.urlretrieve(url, jsonFile)
with open('bike.json') as file:
    data = json.load(file)
    data = sorted(data, key = lambda item : item['bemp'])
    for item in data:
        if int(item['bemp']) > 6:
            print([item['sno'], item['sna'], item['sbi'], item['ar'], item['bemp']])
