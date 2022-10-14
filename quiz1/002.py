import json
import urllib.request
url ='https://data.ntpc.gov.tw/api/datasets/1688B7B8-106E-4967-AA38-DBD86D81D495/json/preview'
jsonFile = 'bike.json'
urllib.request.urlretrieve(url, jsonFile)
with open('bike.json') as file:
    data = json.load(file)
    for item in data:
        #print(item)
        if (item['cha'] == '是' and item['ope'] == '否'):
            print(item['sta'], item['add'], item['no'])
    # data = sorted(data, key = lambda item : item['bemp'])
    # for item in data:
    #     if int(item['bemp']) > 6:
    #         print([item['sno'], item['sna'], item['sbi'], item['ar'], item['bemp']])

