"""
Considere duas listas de inteiros ou floats (lista A e lista B)
soma os valores nos listas retornando um a nova lista com os valores somados

se uma lista for maior que a outra, a soma só vai considerar o tamanho de menor

exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

--------------------------
lista_soma = [2, 4, 6, 8]
"""

# primeira solução 

def soma_listas(lista_a, lista_b):
    return [a + b for a, b in zip(lista_a, lista_b)]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = soma_listas(lista_a, lista_b)
print(lista_soma)

# segunda solução

from itertools import islice

def soma_listas_itertools(lista_a, lista_b):
    tamanho = min(len(lista_a), len(lista_b))
    # islice limita cada lista até o tamanho da menor
    return [a + b for a, b in zip(islice(lista_a, tamanho), islice(lista_b, tamanho))]

print(soma_listas_itertools([1,2,3,4,5], [10,20]))  
print(soma_listas([1, 2, 3], [4, 5, 6]))
print(soma_listas([0.5, 1.5], [2.0, 3.0, 4.0]))
print(soma_listas([10, 20, 30], [1]))
print(soma_listas([], [1, 2, 3]))

