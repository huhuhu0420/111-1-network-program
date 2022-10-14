
import requests as rq
from bs4 import BeautifulSoup

def isSoClose (num, red_num):
    same = 0
    for i in range(3):
        if num[i] == red_num.text[i]:
            same += 1
    if same == 2:
        return 1
    return 0

url="https://invoice.etax.nat.gov.tw/" #網址
html=rq.get(url) # 讀取靜態網頁 html
html.raise_for_status() # 若沒讀到網頁,回傳error
#print(html.text) # 輸出讀取到的 html
soup = BeautifulSoup(html.text,"html.parser") #內建parser分析轉成BeautifulSoup物件

red_nums = soup.find(class_="etw-table-bgbox etw-tbig").find_all("span", {"class":{"font-weight-bold etw-color-red"}})

num = '221'

for red_num in red_nums:
    if (len(red_num.text) == 3):
        if num == red_num.text:
            print('money:200')
        elif isSoClose(num, red_num) == 1:
            print("so close")
        print(red_num.text)