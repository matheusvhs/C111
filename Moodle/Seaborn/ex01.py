import pandas as pd

try:
    df = pd.read_csv('linguagens.csv')
except FileNotFoundError:
    data = {
        'Linguagem': ['C', 'Java', 'Python', 'C', 'Java', 'Python'],
        'Valor': [16.04, 16.25, 9.85, 16.21, 11.68, 12.12],
        'Ano': [1, 1, 1, 2, 2, 2]
    }
    df = pd.DataFrame(data)

df_pivot = df.pivot(index='Linguagem', columns='Ano', values='Valor')
df_pivot.columns = ['Ano 1', 'Ano 2']

df_pivot['Crescimento (%)'] = ((df_pivot['Ano 2'] - df_pivot['Ano 1']) / df_pivot['Ano 1']) * 100

print("A popularidade das linguagens de programação varia com o passar dos anos, de acordo com a sua adequação às necessidades do momento.")
print("-" * 70)

print("## 1. Porcentagem Total no Mercado")
total_ano1 = df_pivot['Ano 1'].sum()
total_ano2 = df_pivot['Ano 2'].sum()

print(f"As 3 linguagens juntas representam {total_ano1:.2f}% do mercado no **Ano 1**.")
print(f"As 3 linguagens juntas representam {total_ano2:.2f}% do mercado no **Ano 2**.")
print("-" * 70)

print("## 2. Crescimento/Declínio de Cada Linguagem (Ano 1 -> Ano 2)")
for index, row in df_pivot.iterrows():
    crescimento = row['Crescimento (%)']
    status = "crescimento" if crescimento >= 0 else "declínio"
    print(f"**{index}**: {crescimento:+.2f}% ({status})")
print("-" * 70)

df_crescimento = df_pivot[df_pivot['Crescimento (%)'] > 0]

print("## 3. Linguagens que Tiveram Crescimento")
if not df_crescimento.empty:
    print("Linguagens com Crescimento:")
    print(df_crescimento[['Ano 1', 'Ano 2', 'Crescimento (%)']].to_string(float_format="%.2f"))
else:
    print("Nenhuma linguagem teve crescimento neste período.")
print("-" * 70)

print("## 4. Previsão de Linguagem Mais Popular (Depois de 2 Anos - Ano 4)")

taxa_crescimento = df_pivot['Crescimento (%)'] / 100
df_pivot['Ano 4 (Previsto)'] = df_pivot['Ano 2'] * ((1 + taxa_crescimento) ** 2)

linguagem_mais_popular_ano4 = df_pivot['Ano 4 (Previsto)'].idxmax()
popularidade_max_ano4 = df_pivot['Ano 4 (Previsto)'].max()

print("Previsão de Popularidade no Ano 4:")
print(df_pivot[['Ano 4 (Previsto)']].to_string(float_format="%.2f"))
print(f"\nSe as tendências se mantiverem, a linguagem mais popular depois de 2 anos (no Ano 4) seria **{linguagem_mais_popular_ano4}** com **{popularidade_max_ano4:.2f}%**.")