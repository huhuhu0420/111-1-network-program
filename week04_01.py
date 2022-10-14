import requests as rq
from bs4 import BeautifulSoup
url="https://tw.stock.yahoo.com/quote/2330.TW/dividend" #網址
html=rq.get(url) # 讀取靜態網頁 html
html.raise_for_status() # 若沒讀到網頁,回傳error
#print(html.text) # 輸出讀取到的 html
soup = BeautifulSoup(html.text,"html.parser") #內建parser分析轉成BeautifulSoup物件
years = soup.find_all("div",class_="D(f) W(98px) Ta(start)")
context = soup.find_all("div",class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)")
year1 = 2008
year2 = 2011
total = 0
for i in range(len(years)):
    try:
        year_int = int(years[i].text[0:4])
        if (year1 <= year_int <= year2):
            index = (i - 6) * 4
            print(year_int, context[index].text)
            total += float(context[index].text)
    except ValueError:
        continue
print(total)
    