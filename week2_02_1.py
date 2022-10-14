import pandas as pd

df = pd.read_csv('pig.csv', encoding='utf8', sep=',')
df = pd.DataFrame(df)
df.columns = ['mnt', 'weight', 'price']
print(df.columns)
print(df.describe())
print(df[df['weight']].sum())