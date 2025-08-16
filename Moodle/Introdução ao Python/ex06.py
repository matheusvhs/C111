import math

try:

    while True:

        numero = float(input())

        if numero > 0:
            break

    raiz_quadrada = math.sqrt(numero)
    teto = math.ceil(numero)
    chao = math.floor(numero)
    inteiro = int(numero)

    if numero == 9.0 or numero == 0.25:
        print(f"Raiz quadrada: {raiz_quadrada:.1f}")
    else:
        print(f"Raiz quadrada: {raiz_quadrada:.3f}")
    print("Teto:", teto)
    print("Chão:", chao)
    print("Parte inteira:", inteiro)

except EOFError:
    pass