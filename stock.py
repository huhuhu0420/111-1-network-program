import requests as rq
from bs4 import BeautifulSoup
url="https://tw.stock.yahoo.com/quote/0050.TW/dividend" #網址
html=rq.get(url) # 讀取靜態網頁 html
html.raise_for_status() # 若沒讀到網頁,回傳error
#print(html.text) # 輸出讀取到的 html
soup = BeautifulSoup(html.text,"html.parser") #內建parser分析轉成BeautifulSoup物件
year = soup.find_all("div",class_="D(f) W(98px) Ta(start)")
context = soup.find_all("div",class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)")
print(year[0].text, year[1].text, year[2].text) #year[i].text,i=0 為第一個 row (標題)
#year[i].text,i=1 為第二個 row (內容題)
print(context[0].text, context[1].text,context[2].text) # context [i].text, i = 0, 1, 2, 3 為第一個 row(標題)
print(context[3].text, context[4].text,context[5].text)
print(context[6].text, context[7].text,context[8].text)