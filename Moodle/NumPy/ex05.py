import numpy as np

try:
    semente = int(input())
except (ValueError, EOFError):
    exit()

np.random.seed(semente)

matriz = np.random.randint(1, 51, size=(4, 4))

medias_linhas = np.mean(matriz, axis=1)
medias_colunas = np.mean(matriz, axis=0)

maior_media_linha = np.max(medias_linhas)
maior_media_coluna = np.max(medias_colunas)

valores_unicos, contagens = np.unique(matriz, return_counts=True)

numeros_com_2_aparicoes = valores_unicos[contagens == 2]

print(f"Média das linhas: {medias_linhas}")
print(f"Média das colunas: {medias_colunas}")
print(f"Maior média das linhas: {maior_media_linha}")
print(f"Maior média das colunas: {maior_media_coluna}")
print(f"Valores: {valores_unicos}")
print(f"Contagens: {contagens}")
print(f"Números que aparecem 2 vezes: {numeros_com_2_aparicoes.tolist()}")