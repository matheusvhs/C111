n = int(input().strip())

idades = []
mulheres_menos_20 = 0

for i in range(n):
    nome = input().strip()
    idade = int(input().strip())
    sexo = input().strip().lower()

    idades.append(idade)

    if sexo == "mulher" and idade < 20:
        mulheres_menos_20 += 1

# cálculo da média
media_idade = sum(idades) / n

print(f"Media de idade do grupo: {media_idade}")
print(f"Mulheres com menos de 20 anos: {mulheres_menos_20}")
