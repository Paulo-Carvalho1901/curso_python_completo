# Empacotamento e desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a
# print(a, b)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# desempacotamento
# a, b = pessoa.values()
# # print(a, b)

# # desempacotamento interno
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)


# # itenrando com for
# for chave, valor in pessoa.items():
#     print(chave, valor) # retorna uma tupla com valor

# args e Kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
