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

