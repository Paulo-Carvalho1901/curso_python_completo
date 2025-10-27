# O que são subprograma

# Explicando args

def somatorio(*args):
    acumulador = 0
    for val in args:
        acumulador += val
    return acumulador


print(somatorio(2, 2, 2))


def soma(*args):
    cont = 0
    for val in args:
        cont += val
    return cont


print(soma(2, 3))