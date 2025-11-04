

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

# funções imperativas
seq = [1, 2, 3, 4, 5]
result = []

for val in seq:
    result.append(val ** 2)

print(result)
