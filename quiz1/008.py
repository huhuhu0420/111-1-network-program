import requests #抓取網頁的套件
import pandas as pd #分析資料的套件

def getNum (data):
    num = ''
    intFlag = 0
    for d in data:
        try:
            int_d = int(d)
            num += d
            intFlag = 1
        except ValueError:
            if (d == '號'):
                break
            if (intFlag == 1):
                intFlag = 0
                num = ''
            continue
    return num

city = ['台北市', '新北市', '桃園市', '台中市', '台南市', '高雄市', '新竹縣', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '宜蘭縣', '花蓮縣', '台東縣', '澎湖縣', '金門縣', '連江縣']
#city = ['青年路']
target = input()
roadAddressRecord ={}
for index, city in enumerate(city):
    data = {'strTargetField':'COUNTY','strKeyWords':'%s' % city}
    res = requests.post('https://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    count = pd.read_html(res.text , header=0)[0].shape[0]
    data = pd.read_html(res.text, header=0)[0]
    outcome = []
    # print(data)
    # target = '青年路'
    for i in range(count):
        fullAddress = data.iloc[i,2]
        num = getNum(fullAddress)
        if target in fullAddress:
            outcome.append([data.iloc[i, 0], data.iloc[i, 1], data.iloc[i, 2], num])
        start = fullAddress.find(city[0])
        end = fullAddress.find('路')+1
        if end<3: continue #空的資料跳過
        roadAddress = fullAddress[start:end]
        if roadAddress not in roadAddressRecord:
            roadAddressRecord[roadAddress]=1
        else:
            roadAddressRecord[roadAddress]+=1
    out_sort =  sorted(outcome, key = lambda o:int(o[3]))
    for o in out_sort:
        print(o[0], o[1], o[2])