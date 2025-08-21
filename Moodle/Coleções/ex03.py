nome = input()
media = int(input())  # converte para inteiro

if media >= 50:
    situacao = 'AP'
else:
    situacao = 'RP'

dados = {   # evite usar "dict" como nome de variável (sobrescreve o tipo dict)
    'nome': nome,
    'media': media,
    'situacao': situacao
}

print(dados)
