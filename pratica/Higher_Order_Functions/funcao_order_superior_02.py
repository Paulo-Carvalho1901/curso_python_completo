# Funções de ordem superior em Python

# O que são funções de ordem superior?

# Por exemplo, considere a seguinte função que recebe uma função e um
# iterável como argumentos e retorna o resultado da aplicação da função a
# cada elemento no iterável:

def apply_to_each(func, iterable):
    return [func(x) for x in iterable]

def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]
square_numbers = apply_to_each(square, numbers)
print(square_numbers) # Saída [1, 4, 9, 16, 25]

# Aqui, apply_to_eaché uma função de ordem superior porque recebe uma função, square, como argumento.
