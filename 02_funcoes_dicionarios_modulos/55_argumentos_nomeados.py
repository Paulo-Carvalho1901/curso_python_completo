"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# definição da função
def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)


# print(soma(1, 2)) # retorna None
soma(1, 2, 5) # execução da função
soma(y=2, z=5, x=1) # colocando argumento normados

print(1, 2, 3, sep='-')
