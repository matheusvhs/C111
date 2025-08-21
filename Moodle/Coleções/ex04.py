pessoas = {}

for i in range(5):
    nome = input().strip()
    peso = float(input().strip())
    pessoas[nome] = peso

# Encontrar pessoa mais pesada e mais leve
mais_pesada = max(pessoas, key=pessoas.get)
mais_leve = min(pessoas, key=pessoas.get)

print(f"Pessoa mais leve: {mais_leve}")
print(f"Pessoa mais pesada: {mais_pesada}")