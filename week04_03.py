import requests as rq
from bs4 import BeautifulSoup
url="https://www.cwb.gov.tw/V8/C/K/bilingual_glossary.html" #網址
html=rq.get(url) # 讀取靜態網頁 html
html.raise_for_status() # 若沒讀到網頁,回傳error
soup = BeautifulSoup(html.text,"html.parser") #內建parser分析轉成BeautifulSoup物件
volcabulary = list()

english = ""
chinese = ""
vols = soup.find('table', id="table1").find('tbody').findAll('td')
for i in range(len(vols)):
    if (i%3 == 1):
        english = vols[i].text
    if (i%3 == 2):
        chinese = vols[i].text
        volcabulary.append([english, chinese])
# for v in volcabulary:
#     print(v)

searchStr = "溫"

for v in volcabulary:
    if searchStr in v[0]:
        print(v[0], v[1])
    if searchStr in v[1]:
        print(v[0], v[1])