# enumerate - enumera iteráveis (índices)

lista = ['Paulo', 'Andreia', ' Davi']
lista.append('João')

# lista_enumerada = enumerate(lista)

# for indice, item in enumerate(lista):
#     indice, item = item
#     print(indice, item)

for indice, item in enumerate(lista):
    print(indice, item, lista[indice])

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

# print('O que tem na lista enumerada', lista_enumerada)

# for nomes in lista_enumerada:
#     print(nomes)