import pandas as pd

df1 = pd.read_csv('president_heights.csv', encoding='utf8', sep=",")
df1 = pd.DataFrame(df1)
df1.columns = ['order', 'name', 'height']
print(df1.columns)
print(df1.describe())
print(df1.sort_values("height", ascending=False).head(5))
print(df1[df1.height > 180].sort_values("height", ascending=False).tail(5))
