import requests as rq
from bs4 import BeautifulSoup
# url='https://scweb.cwb.gov.tw/zh-tw/earthquake/world/#'
# html=rq.get(url) # 讀取靜態網頁 html
# html.raise_for_status() # 若沒讀到網頁,回傳error

with open ('7.html') as file:
    soup = BeautifulSoup(file, "html.parser") #內建parser分析轉成BeautifulSoup物件
    data = soup.find("table", class_="Btable worldTable").find('tbody').find_all("td")
    #context = soup.find_all("div",class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)")
    i = 0
    a = []
    tmp = []
    for d in data:
        if (i%6 == 0 or i%6 == 3 or i%6 == 5 or i%6 == 4):
            tmp.append(d.text)
        if (i%6 == 5 and i != 0):
            a.append(tmp)
            tmp = []
        i += 1
    a = sorted(a, key=lambda m:m[2], reverse=True)
    i = 0
    for b in a:
        for c in b:
            print(c, end=' ')
        print()
        i += 1
        if (i==3):
            break