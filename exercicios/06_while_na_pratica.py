# Iterando strings com while

nome = 'Paulo Carvalho'
indice = 0

novo_nome = ''
while indice < len(nome):
    letra = nome[indice]

    novo_nome += letra
    indice += 1

print(novo_nome)