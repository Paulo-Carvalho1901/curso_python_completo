# args argumentos posicionais

def soma_tudo(*args):
    """Soma todos os argumentos poscionais."""
    total = 0
    for numero in args:
        total += numero
    return total


print(soma_tudo(1, 2, 3))
print(soma_tudo(1, 2, 3, 4, 5))
