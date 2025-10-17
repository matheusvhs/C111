import pandas as pd

df = pd.read_csv('shopping_trends_dirty.csv')

df_silver = df.dropna()
df_silver = df_silver.drop_duplicates()

filtrado = df_silver['Purchase Amount (USD)'] > 80

media = df_silver.loc[filtrado, 'Purchase Amount (USD)']

print(len(media))



