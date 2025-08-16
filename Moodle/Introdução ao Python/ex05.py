try:

    while True:

        numero = int(input())

        if 1000 <= numero <= 9999:
            break

    unidade = numero / 1000
    dezena = (numero % 1000) / 100
    centena = (numero % 100) / 10
    milhar = numero % 10

    print("Unidade:", int(milhar))
    print("Dezena:", int(centena))
    print("Centena:", int(dezena))
    print("Milhar:", int(unidade))

except EOFError:
    pass