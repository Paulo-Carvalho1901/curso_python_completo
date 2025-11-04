

# High Order Funcition

def apply(func, val):
    return func(val)


def soma_mais_um(x):
    return x + 1



print(apply(soma_mais_um, 1))

# Funções VS loops
# uma das funções mais comuns usar funções como objetos é poder
# evitar o uso de loops com for while. Transformando a maneira 
# imperativa de se programar, para uma forma declarativa

# função imperativas
seq = [1, 2, 3, 4, 5]
result = []

for val in seq:
    result.append(val ** 2)

print(result)

print()
# função declarativa
result = list(map(lambda x: x ** 2, seq))

print(result)

print()
from itertools import takewhile

takewhile(lambda x: x != 3, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(takewhile(lambda x: x != 3, [1, 2, 3, 4, 5, 6, 7, 8])))
