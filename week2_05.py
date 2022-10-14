import pandas as pd
import json

with open('bike.json') as file:
    data = json.load(file)
    # for d in data:
    #     if (int(d['bemp']) > 10):
    #         print(d['sna'], d['sarea'], d['ar'], d['bemp'])
    df = pd.DataFrame(data)
    print(df)
    print(df[df['bemp'].astype(int) > 10][['sna', 'sarea', 'ar', 'bemp']])
    print(df[df['bemp'].astype(int) > 10].groupby(['sarea'])['bemp'].count())
    df['bemp'] = pd.to_numeric(df['bemp'])
    print(df[df['bemp'].astype(int) > 10].groupby(['sarea'])['bemp'].sum())

