# reduce - faz a redução de um iteravel em um valor
# reduzindo um iteravel em um unico valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 3},
]

# def funcao_do_reduce(acumulador, produto):
#     print('Acumulador', acumulador)
#     print('Produto', produto)
#     print()
#     return acumulador + produto['preco']


total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('O total é', total)

# função acumuladora

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))
