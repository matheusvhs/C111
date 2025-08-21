# Loja 1
N1 = int(input().strip())
loja1 = [input().strip() for _ in range(N1)]

# Loja 2
N2 = int(input().strip())
loja2 = [input().strip() for _ in range(N2)]

set1 = set(loja1)
set2 = set(loja2)

uniao = sorted(set1 | set2)     # ordenação padrão (case-sensitive)
intersec = sorted(set1 & set2)

print("Modelos disponiveis em pelo menos uma das lojas:")
print(uniao)
print()
print("Modelos disponiveis em ambas as lojas:")
print(intersec)