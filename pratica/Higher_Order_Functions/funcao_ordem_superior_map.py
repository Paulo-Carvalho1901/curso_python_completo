"""
map: maprecebe uma função e um iterável como argumentos e 
retorna um novo iterável que é o resultado da aplicação da função a 
cada elemento no iterável original:
"""

def quadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]
numero_quadrado = list(map(quadrado, numeros))
print(numero_quadrado)
