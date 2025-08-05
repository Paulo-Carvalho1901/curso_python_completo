"""
Introdução às funções (def) en Python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código
Eles podem receber valores por parâmetros (argumentos)
e retornar um valor especifico.
por padrão, funções Python retornam None (nada)
"""

# def Python(a, b, c):
#     print('Varias1')
#     print('Varias2')
#     print('Varias3')
#     print('Varias4')

# def imprimir(a, b, c): # parametros
#     print(a, b, c)



# imprimir(1, 2, 3) # Argumentos
# imprimir(4, 5, 6) 

def saudacao(nome='Sem nome'):
    print(f'Bem vindo! {nome}')


saudacao('Paulo Carvalho')
saudacao('Andreia Carvalho')
saudacao('Davi Carvalho')
saudacao()

def soma(a, b):
    print(a + b)

def subtracao(a, b):
    print(a - b)

soma(10, 10)
soma(5, 3)
subtracao(10, 3)
