times = []

for x in range(0, 5):
    nome_time = input()

    times.append(nome_time)

busca_time = input()

print("Os 3 primeiros colocados sao:")
for time in times[0:3]:
    print(time)
print()
print("Os 2 ultimos colocados sao:")
for time in times[3:5]:
    print(time)
print()
print("Times em ordem alfabetica:")
for time in sorted(times):
    print(time)
print()
print("O ", busca_time, " esta na posicao ", times.index(busca_time) + 1)


