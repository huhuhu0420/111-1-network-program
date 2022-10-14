import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
ans = []
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"): #針對匯率表格分析
    cell = single_tr.findAll("td") #找到每一個表格
    #print(cell)
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] #找到表格中幣別
    currency_name = currency_name.replace("\r","") #取代不需要的字元
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate_out = cell[2].contents[0] #找到幣別匯率
    currency_rate_in = cell[1].contents[0]
    #print(currency_name, currency_rate)
    if(currency_rate_out == '-'):
        continue
    temp = float(currency_rate_out)- float(currency_rate_in)
    if(temp<0):
        temp*=-1
    if(ans == []):
        ans.append([currency_name,temp])
        continue
    judge = 0
    for i in range(len(ans)):
        if(temp > ans[i][1]):
            ans.insert(i,[currency_name,temp])
            judge = 1
            break
    if(judge == 0):
        ans.append([currency_name,temp])
    #file_name = "bankRate" + currency_name + ".csv" #每種幣別存一個檔案
    #now_time = strftime("%Y-%m-%d %H:%M:%S", localtime()) #記錄目前時間
print(ans)
