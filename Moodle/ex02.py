N = int(input())
intervalo1 = int(input())
intervalo2 = int(input())

inicio = min(intervalo1, intervalo2)
fim = max(intervalo1, intervalo2)

#Exibir a tabuada do número N no intervalo [intervalo1, intervalo2]
for i in range(inicio, fim + 1):
    print(f"{N} x {i} = {N * i}")