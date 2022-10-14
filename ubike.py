import urllib.request
import zipfile
import csv

url = 'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
zipName = 'F.zip'
urllib.request.urlretrieve(url, zipName)
f = zipfile.ZipFile(zipName)
file_dir = './'
print(f)
print(f.namelist())
for fileName in f.namelist():
    f.extract(fileName, file_dir)
    print(fileName)
f.close()
f = open(fileName, 'r', encoding='utf8')
plots = csv.reader(f, delimiter=',')
for row in plots:
    if row[12] != 'bemp' and int(row[12]) > 5:
        print('%5s'%row[0], '%20s'%row[1], '%10s'%row[2], '%30s'%row[8], '%5s'%row[3], '%5s'%row[12])
f.close()
