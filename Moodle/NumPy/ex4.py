import numpy as np

dados_matriz = []

try:
    num_linhas = int(input())
except (ValueError, EOFError):
    num_linhas = 0

for _ in range(num_linhas):
    try:
        linha_str = input().strip().split()
        if not linha_str:
            continue
        linha_int = [int(numero) for numero in linha_str]
        dados_matriz.append(linha_int)
    except (ValueError, EOFError):
        break

if not dados_matriz:
    exit()

matriz = np.array(dados_matriz)

linhas, colunas = matriz.shape

total_elementos = linhas * colunas

print(f"{linhas} linhas")
print(f"{colunas} colunas")

if total_elementos % 2 == 0:
    print("O vetor resultante teria um número par de elementos.")
else:
    print("O vetor resultante teria um número ímpar de elementos.")