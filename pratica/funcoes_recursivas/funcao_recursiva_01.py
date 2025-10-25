# Uma função recursiva é uma função que chama a si mesma dentro de sua definição.

def fatorial(n):
    """Calcula o fatorial de n recursivamente."""
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))
