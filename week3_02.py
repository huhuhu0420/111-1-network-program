import requests
from bs4 import BeautifulSoup

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW") 
bsObj = BeautifulSoup(html.content, "lxml")
datas =  []
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"): 
    cell = single_tr.findAll("td") 
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] 
    #currency_name = currency_name.replace("\r","") 
    #currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace("\r\n","")
    currency_name = currency_name.replace(" ","")
    currency_in = cell[1].contents[0]
    currency_rate = cell[2].contents[0] 
    try:
        diff = float(currency_rate) - float(currency_in)
    except ValueError:
        diff = 'None'
    print(currency_name, currency_in, currency_rate, diff)
    if (diff != 'None'):
        datas.append([currency_name, diff])
datas = sorted(datas, key=lambda x:x[1], reverse=True)
i = 0
for data in datas:
    print(data)
    i += 1
    if (i == 3):
        break
