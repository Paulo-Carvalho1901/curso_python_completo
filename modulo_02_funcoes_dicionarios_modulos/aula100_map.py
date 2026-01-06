from functools import partial
from types import GeneratorType

# map - para mapear dados
def print_iter(iterador):
    print(*list(iterador), sep='\n' )
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# list comprehention
# novos_produtos = [
#     {**produto, 'preco': aumentar_porcentagem(produto['preco'], 1.1)} for produto in produtos
# ]

# novos_produtos = [
#     {**produto, 'preco': aumentar_dez_porcento(produto['preco'])} for produto in produtos
# ]

def mudo_preco_de_produto(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

novos_produtos = map(
    mudo_preco_de_produto,
    produtos
)

# mapeamento
print_iter(produtos)
print_iter(novos_produtos)
# print(hasattr(novos_produtos, '__iter__'))
# print(hasattr(novos_produtos, '__next__'))
# print(isinstance(novos_produtos, GeneratorType))
