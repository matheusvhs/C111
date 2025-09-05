import pandas as pd

# Carregar o arquivo CSV
dfpaises = pd.read_csv("../../datasets/paises.csv", sep=";")

# Limpar e padronizar os nomes das regiões
dfpaises['Region'] = dfpaises['Region'].str.strip().str.title()

# Agrupar países por região
df_grouped = dfpaises.groupby('Region')['Country'].apply(list)

# Exibir países da Oceania
print("Países da OCEANIA:")
for region in df_grouped['Oceania']:
    print(region)

# Contar quantidade de países na Oceania
print("\nQuantidade de países na OCEANIA:", (len(df_grouped['Oceania'])))

most_populous_country = dfpaises.groupby('Country')['Population'].sum().idxmax()
most_populous_region = dfpaises.groupby('Region')['Population'].sum().idxmax()

print("\nPaís com maior população:", most_populous_country)
print("Região:", most_populous_region)

# Média de alfabetização por região
print("\nMédia de alfabetização por região:")
df_grouped_literacy = dfpaises.groupby('Region')['Literacy (%)'].mean()
for region, literacy in df_grouped_literacy.items():
    print(f"{region}: {literacy:.2f}%")

# Países sem costa marítima
print("\nPaíses sem costa marítima")
df_grouped_nocoast = dfpaises.groupby('Country')['Coastline (coast/area ratio)'].first()
for country, coastline in df_grouped_nocoast.items():
    if coastline == 0.0:
        print(country)
