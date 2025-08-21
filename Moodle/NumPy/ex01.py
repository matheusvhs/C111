import numpy as np

# 1) Array de 1s
array1 = np.ones(8, dtype=int)

# 2) Lê 8 inteiros de uma única linha
array2 = np.array(list(map(int, input().split())), dtype=int)

# 3) Soma e soma total
array3 = array1 + array2
soma_total = int(array3.sum())

# 4) Remodelagem conforme a regra
if soma_total >= 40:
    matriz = array3.reshape(4, 2)
    formato = "4 x 2"
else:
    matriz = array3.reshape(2, 4)
    formato = "2 x 4"

# 5) Saída (mesmo formato do enunciado)
print("\nArray resultante da soma:")
print(array3)

print("\nSoma de todos os elementos:")
print(soma_total)

print(f"\nMatriz ({formato}):")
print(matriz)
