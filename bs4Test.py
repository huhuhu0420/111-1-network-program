import pandas as pd #匯入pandas套件
df=pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2', encoding='big5hkscs'
,header=0)
newdf=df[0][df[0]['產業別'] > '0'] #產業別資料大於 0
#del newdf['國際證券辨識號碼(ISIN Code)'],newdf['CFICode'],newdf['備註']
del newdf['CFICode'],newdf['備註'] #刪除兩個不需要欄位
df2=newdf['有價證券代號及名稱'].str.split('', expand=True) #分成兩個欄位回存
df2 = df2.reset_index(drop=True) #重設索引值
newdf = newdf.reset_index(drop=True) #重設索引值
for i in df2.index:
#有價證券代號及名稱這個欄位，中間有空格
    if ' ' in df2.iat[i,0]: #將有價證券代號及名稱
        df2.iat[i,0]=df2.iat[i,0].split(' ')[0] #欄位資料內容分割為2，回存df2物件中。
        df2.iat[i,1]=df2.iat[i,0].split(' ')[1] #回存df2物件中。
newdf=df2.join(newdf) #將df2合併到newdf物件
newdf=newdf.rename(columns = {0:'股票代號',1:'股票名稱'}) #修改欄位名稱
del newdf['有價證券代號及名稱'] #將"有價證券代號及名稱"欄位刪除
# newdf.to_excel('stock_.xlsx', sheet_name='Sheet1',index=False) #存入excel
