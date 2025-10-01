# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

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
novo_produtos = [{'nome': produto['nome'], 'preco': produto['preco']} for produto in produtos]

print(novo_produtos)
print(*novo_produtos, sep='\n')
