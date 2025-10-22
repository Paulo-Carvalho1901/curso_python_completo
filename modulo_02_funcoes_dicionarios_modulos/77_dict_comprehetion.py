# Dictionary comprehention e Set comprehention

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categaria': 'Escritorio'
}

# for chave, valor in produto.items():
#     print(chave, valor)


# dict comprehenrion
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in 
    produto.items()
    if chave != 'categaria'
}

# lista dict comprehention
lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }

print(dict(lista))

print('=-' * 40)
print('Set comprehention')

s1 = {i for i in range(10)}
print(s1)
