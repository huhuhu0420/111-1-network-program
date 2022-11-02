import requests #抓取網頁的套件
import pandas as pd #分析資料的套件
# 建立一個縣市的list
city = ['基隆市', '台北市', '新北市', '桃園市']
for index, city in enumerate(city):
    data = {'strTargetField':'COUNTY','strKeyWords':'%s' % city}
#res 取得網頁所有資料
    res = requests.post('https://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
# 第一次迴圈
    if index == 0:
#網頁資料的形式是table，使用panda的 read_html 取得資料 [0]第一欄資料
# res.txt 網頁資料中的文字，[0]第一欄資料, header=0 不要第一列標頭資料
        df_7_11_store = pd.read_html(res.text, header=0)[0]
#建立dataframe，將城市填入。
        df_7_11_store['縣市'] = city
# 第二次迴圈以上就將資訊直接append到dataframe裡
    if index > 0:
        oneCity_store = pd.read_html(res.text, header=0)[0]
        oneCity_store['縣市'] = city
        df_7_11_store = df_7_11_store.append(oneCity_store)
#print(oneCity_store)
#印出查詢資料進度, shape[0] 查詢本次城市取得資料的筆數
    print('%2d) %+*s %4d' % (index+1, 10, city, pd.read_html(res.text, header=0)[0].shape[0]))
#將資料輸出成Excel

