# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

import pprint


def p(v):
    pprint.pprint(novo_produtos, sort_dicts=False, width=40)




lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# List comprehension
lista = [n for n in range(10)]
# print(lista)

# List comprehension colocando uma logica mapeamento
lista = [numero * 2 for numero in range(10)]
# print(lista)


# Mapeamento de dados em list comprehenrion
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
# novo_produtos = [produto for produto in produtos] # list comprehenrion simples
# novo_produtos = [{'nome': produto['nome'], 'preco': produto['preco']} for produto in produtos]
novo_produtos = [{**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos]

# print(*novo_produtos, sep='\n')
# print(novo_produtos)
p(novo_produtos)
