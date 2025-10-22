"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetrizar (argumentos)
e retornar um valor especifico.
por padrão, funções Python retornam None (nada).
"""
# https://docs.python.org/pt-br/3.13/library/functions.html
# https://docs.python.org/pt-br/3.13/c-api/function.html

# Ex de funções
# https://www.codaqui.dev/trilhas/python/page-5/?gad_source=1&gad_campaignid=23058687337&gclid=CjwKCAjwgeLHBhBuEiwAL5gNESFQ3Mriy2glJB9lCxtI1xftBNpCzii6xknPnm6aFBCg1bBQHGcB7RoCIxwQAvD_BwE


# definindo uma função em python (def)
# def Print(a, b, c): # parâmetros
#     print('Variavel1')
#     print('Variavel2')
#     print('Variavel3')
#     print('Variavel4')

def imprimir(a, b, c): # parâmetros
    print(a, b, c)


# executandoa a função com os parenteses ()
# Como foi colocado parâmetros nessa função agora na chamada temos que passar para função
imprimir(1, 2, 3) # argumentos
imprimir(4, 5, 6)
