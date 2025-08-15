try:
    km = int(input())

    if km <= 200:
        resultado = km * 0.50
        print(resultado)
    else:
        resultado = km * 0.45
        print(f"{resultado:.2f}")
except EOFError:
    pass