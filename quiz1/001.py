from fileinput import filename
import urllib.request
import zipfile
import csv
import numpy as np
import pandas as pd

url = 'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
zipName = 'F.zip'
urllib.request.urlretrieve(url, zipName)
f = zipfile.ZipFile(zipName)
file_dir = './'
for fileName in f.namelist():
    f.extract(fileName, file_dir)
f.close()

df = pd.read_csv(fileName, encoding='utf8')
df = pd.DataFrame(df)
print(df.sort_values(["bemp"], ascending=[False]).head(5).sort_values("sno", ascending=True)[['sno', 'sna','bemp']].to_string(index=False))
f = open(fileName, 'r', encoding='utf8')
plots = csv.reader(f, delimiter=',')
next(plots)
n = int(input('n = '))
for row in plots:
    if int(row[12]) > n:
        print('%5s'%row[0], '%20s'%row[1], '%5s'%row[12])

f.close()
