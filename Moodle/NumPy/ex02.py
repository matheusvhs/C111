import numpy as np

n1, n2, n3, n4 = map(int, input().split())

inicio1 = min(n1, n2)
fim1 = max(n1, n2)

inicio2 = min(n3, n4)
fim2 = max(n3, n4)

lista1 = []
lista2 = []

for numeros in range(inicio1, fim1+1):
    if numeros % 2 == 0:
        lista1.append(numeros)

for numeros in range(inicio2, fim2+1):
    if numeros % 2 == 0:
        lista2.append(numeros)

array1 = np.array(lista1)
array2 = np.array(lista2)

array_concatenado = np.concatenate((array1, array2))

print(np.sort(array_concatenado))

