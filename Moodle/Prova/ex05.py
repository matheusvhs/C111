import pandas as pd

file_name = "shopping_trends_dirty.csv"

df = pd.read_csv(file_name)

df_cleaned = df.dropna()
df_cleaned = df_cleaned.drop_duplicates()

df_cleaned['Age'] = df_cleaned['Age'].astype(int)
df_cleaned['Purchase Amount (USD)'] = df_cleaned['Purchase Amount (USD)'].astype(int)
df_cleaned['Previous Purchases'] = df_cleaned['Previous Purchases'].astype(int)
df_cleaned['Review Rating'] = df_cleaned['Review Rating'].astype(float)

total_por_metodo = df_cleaned.groupby('Payment Method')['Purchase Amount (USD)'].sum()

print(total_por_metodo)