"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotameto)
"""

# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    args = list(args)
    print(args, type(args))

soma(1, 2, 3, 4, 5, 6)
