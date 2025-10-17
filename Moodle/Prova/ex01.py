import pandas as pd

df = pd.read_csv('shopping_trends_dirty.csv')

df_silver = df.dropna()

age_mean = df_silver['Age'].mean()

print(age_mean)