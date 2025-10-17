import pandas as pd

file_name = input("Digite o nome do arquivo CSV: ")

df = pd.read_csv(file_name)

df_cleaned = df.dropna()
df_cleaned = df_cleaned.drop_duplicates()

df_cleaned['Age'] = df_cleaned['Age'].astype(int)
df_cleaned['Purchase Amount (USD)'] = df_cleaned['Purchase Amount (USD)'].astype(int)
df_cleaned['Previous Purchases'] = df_cleaned['Previous Purchases'].astype(int)
df_cleaned['Review Rating'] = df_cleaned['Review Rating'].astype(float)

total_compras = len(df_cleaned)
compras_venmo = (df_cleaned['Payment Method'] == 'Venmo').sum()

porcentagem_venmo = (compras_venmo / total_compras) * 100

print(f"A porcentagem de compras realizadas com Venmo é: {porcentagem_venmo:.2f}%")