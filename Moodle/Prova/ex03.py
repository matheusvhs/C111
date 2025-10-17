import pandas as pd

file_name = "shopping_trends_dirty.csv"

df = pd.read_csv(file_name)
total_rows_initial = len(df)

rows_before_dropna = len(df)
df_cleaned = df.dropna()
missing_removed = rows_before_dropna - len(df_cleaned)

rows_before_drop_duplicates = len(df_cleaned)
df_cleaned = df_cleaned.drop_duplicates()
duplicates_removed = rows_before_drop_duplicates - len(df_cleaned)

df_cleaned['Age'] = df_cleaned['Age'].astype(int)
df_cleaned['Purchase Amount (USD)'] = df_cleaned['Purchase Amount (USD)'].astype(int)
df_cleaned['Previous Purchases'] = df_cleaned['Previous Purchases'].astype(int)
df_cleaned['Review Rating'] = df_cleaned['Review Rating'].astype(float)

string_cols = [
    'Gender', 'Item Purchased', 'Category', 'Location', 'Size', 'Color',
    'Season', 'Subscription Status', 'Shipping Type', 'Discount Applied',
    'Promo Code Used', 'Payment Method', 'Frequency of Purchases'
]

for col in string_cols:
    if col in df_cleaned.columns:
        df_cleaned[col] = df_cleaned[col].astype('object')

total_sales = len(df_cleaned)

item_counts = df_cleaned['Item Purchased'].value_counts()

least_sold_item = item_counts.index[-1]
count_least_sold = item_counts.iloc[-1]

percentage_least_sold = (count_least_sold / total_sales) * 100

# Apenas a linha abaixo foi alterada para imprimir somente o número
print(percentage_least_sold)