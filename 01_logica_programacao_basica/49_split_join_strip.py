"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = '      Olha só que    ,      coisa interessante       '
lista_frases_cruas = frase.split(',') # mantendo a lista original

lista_frases = [] # alterando a lista com novas informaçoes alterando a lisa original
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())


# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
