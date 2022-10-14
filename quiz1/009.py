import requests as rq
from bs4 import BeautifulSoup

def f (ticket, target):
    i = len(ticket) - 1
    count = 0
    for i in range(len(ticket)-1, 0, -1):
        if (ticket[i] == target[i]):
            count += 1
        else:
            return count
        

n = int(input('n = '))
m =input('m = ')
ticket = []
for i in range(n):
    t = input()
    ticket.append(t)

if (m == '1' or m == '2'):
    with open ('month2.html') as file:
        soup = BeautifulSoup(file, "html.parser") #內建parser分析轉成BeautifulSoup物件
        data = soup.find_all("div", class_='col-12 mb-3')
        i = 0
        total = 0
        flag = 0
        a = set()
        for i in range(len(data)):
            for t in ticket:
                if (t == data[i].text.strip()):
                    if (i == 0):
                        print(t,'特別獎', 10000000)
                        a.add(t)
                        total += 10000000
                    elif (i == 1):
                        print(t,'特獎', 2000000)
                        a.add(t)
                        total += 2000000
                    elif (i == 2 or i == 3 or i == 4):
                        print(t,'頭獎', 200000)
                        a.add(t)
                        total += 200000
                else:
                    if (i != 0 and i != 1):
                        count = f(t, data[i].text.strip())
                        if (count == 7):
                            print(t, '二獎', '400000')
                            a.add(t)
                            total += 40000
                        if (count == 6):
                            print(t, '三獎', '10000')
                            a.add(t)
                            total += 10000
                        if (count == 5):
                            print(t, '四獎', '4000')
                            a.add(t)
                            total += 4000
                        if (count == 4):
                            print(t, '五獎', '1000')
                            a.add(t)
                            total += 1000
                        if (count == 3):
                            print(t, '六獎' '200')
                            a.add(t)
                            total += 200
        for t in ticket:
            if t not in a:
                print(t, 'no', 0)
        print('total: ', total)

if (m == '3' or m == '4'):
    with open ('month4.html') as file:
        soup = BeautifulSoup(file, "html.parser") #內建parser分析轉成BeautifulSoup物件
        data = soup.find_all("div", class_='col-12 mb-3')
        i = 0
        total = 0
        a=set()
        for i in range(len(data)):
            for t in ticket:
                if (t == data[i].text.strip()):
                    if (i == 0):
                        print(t, '特別獎', 10000000)
                        a.add(t)
                        total += 10000000
                    elif (i == 1):
                        print(t, '特獎', 2000000)
                        a.add(t)
                        total += 2000000
                    elif (i == 2 or i == 3 or i == 4):
                        print(t, '頭獎', 200000)
                        a.add(t)
                        total += 200000
                else:
                    if (i != 0 and i != 1):
                        count = f(t, data[i].text.strip())
                        if (count == 7):
                            print(t, '二獎', '400000')
                            a.add(t)
                            total += 40000
                        if (count == 6):
                            print(t, '三獎', '10000')
                            a.add(t)
                            total += 10000
                        if (count == 5):
                            print(t, '四獎', '4000')
                            a.add(t)
                            total += 4000
                        if (count == 4):
                            print(t, '五獎', '1000')
                            a.add(t)
                            total += 1000
                        if (count == 3):
                            print(t, '六獎' '200')
                            a.add(t)
                            total += 200
        for t in ticket:
            if t not in a:
                print(t, 'no', 0)
        print('total: ', total)

if (m == '5' or m == '6'):
    with open ('month6.html') as file:
        soup = BeautifulSoup(file, "html.parser") #內建parser分析轉成BeautifulSoup物件
        data = soup.find_all("div", class_='col-12 mb-3')
        i = 0
        total = 0
        a = set()
        for i in range(len(data)):
            for t in ticket:
                if (t == data[i].text.strip()):
                    if (i == 0):
                        print(t, '特別獎', 10000000)
                        a.add(t)
                        total += 10000000
                    elif (i == 1):
                        print(t, '特獎', 2000000)
                        a.add(t)
                        total += 2000000
                    elif (i == 2 or i == 3 or i == 4):
                        print(t, '頭獎', 200000)
                        a.add(t)
                        total += 200000
                else:
                    if (i != 0 and i != 1):
                        count = f(t, data[i].text.strip())
                        if (count == 7):
                            print(t, '二獎', '400000')
                            a.add(t)
                            total += 40000
                        if (count == 6):
                            print(t, '三獎', '10000')
                            a.add(t)
                            total += 10000
                        if (count == 5):
                            print(t, '四獎', '4000')
                            a.add(t)
                            total += 4000
                        if (count == 4):
                            print(t, '五獎', '1000')
                            a.add(t)
                            total += 1000
                        if (count == 3):
                            print(t, '六獎' '200')
                            a.add(t)
                            total += 200
        for t in ticket:
            if t not in a:
                print(t, 'no', 0)
        print('total: ', total)

if (m == '7' or m == '8'):
    with open ('month8.html') as file:
        soup = BeautifulSoup(file, "html.parser") #內建parser分析轉成BeautifulSoup物件
        data = soup.find_all("div", class_='col-12 mb-3')
        i = 0
        total = 0
        a = set()
        for i in range(len(data)):
            for t in ticket:
                if (t == data[i].text.strip()):
                    if (i == 0):
                        print(t, '特別獎', 10000000)
                        a.add(t)
                        total += 10000000
                    elif (i == 1):
                        print(t, '特獎', 2000000)
                        a.add(t)
                        total += 2000000
                    elif (i == 2 or i == 3 or i == 4):
                        print(t, '頭獎', 200000)
                        a.add(t)
                        total += 200000
                else:
                    if (i != 0 and i != 1):
                        count = f(t, data[i].text.strip())
                        if (count == 7):
                            print(t, '二獎', '400000')
                            a.add(t)
                            total += 40000
                        if (count == 6):
                            print(t, '三獎', '10000')
                            a.add(t)
                            total += 10000
                        if (count == 5):
                            print(t, '四獎', '4000')
                            a.add(t)
                            total += 4000
                        if (count == 4):
                            print(t, '五獎', '1000')
                            a.add(t)
                            total += 1000
                        if (count == 3):
                            print(t, '六獎' '200')
                            a.add(t)
                            total += 200
        for t in ticket:
            if t not in a:
                print(t, 'no', 0)
        print('total: ', total)
