# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

# shallow copy (copia rasa)
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

# d2 apenas está referenciando o mesmo valor na memoria d1
# d2 = d1

# print(id(d1))
# print(id(d2))

# d2['c1'] = 100
# print(d1)

######################################################################
# shallow copy
# d2 = d1.copy()

# copia profunda
d2 = copy.deepcopy(d1)

d2['c1'] = 100
d2['l1'][1] = 999

print(d1)
print(d2)
