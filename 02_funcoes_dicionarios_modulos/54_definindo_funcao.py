"""
Introdução às funções (def) en Python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código
Eles podem receber valores por parâmetros (argumentos)
e retornar um valor especifico.
por padrão, funções Python retornam None (nada)
"""

# def Print():
#     print('variavel 1')
#     print('variavel 2')
#     print('variavel 3')


# Print()
# Print()


# def soma(a, b, c):
#     print('Qualquer coisa')


# soma(1, 5, 3)
# soma(1, 5, 3)
# soma(1, 5, 3)


def imprimir(a, b, c):
    print(a, b, c)



imprimir(1, 2, 3)
imprimir(4, 5, 6)


def saudacao(nome='Sem nome.'):
    print(f'Olá, {nome}')


saudacao('Paulo Carvalho')
saudacao('Andreia Carvalho')
saudacao('Davi Carvalho')
saudacao()

#################################################

def imprima(): # estrutura da função
    print('Olá') # valor a ser retornado pela função


imprima() # executando a função '()' 
