import requests as rq
from bs4 import BeautifulSoup
url = "http://www.tcr.org.tw/a/table_blogs/index/21654"
html = rq.get(url)
soup = BeautifulSoup(html.text, "html.parser")

#print(soup.text)
allName = soup.find('table', {'class': 'table_blog table_blog_mode_2'}).find_all('a')
companyName = []
address = []
i = 0
for name in allName:
    if i % 5 == 0:
        companyName.append(name.text)
    if i % 5 == 4:
        address.append(name.text)
    i += 1
# for name in companyName:
#     print(name)
# for a in address:
#     print(a)

choose = input()
target = input()
if (choose == '1'):
    for name in companyName:
        if target in name:
            print(name)

if (choose == '2'):
    for add in address:
        if target in add:
            print(add)
