import pandas as pd

df = pd.read_excel("gapminder.xlsx")
print(df)
print(df[df['year'].isin([2002])]['pop'].mean())
print(df[df['year'].isin([2002])].groupby('continent')['lifeExp'].mean())
print(df[df['year'] == 2002].groupby('continent')['gdpPercap'].mean())
