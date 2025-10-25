# Ordenando uma lista de tuplas pelo segundo elemento
pares = [(1, 'um'), (3, 'três'), (2, 'dois'), (4, 'quatro')]

# Usando lambda como função de chave para sorted()
pares_ordenados = sorted(pares, key=lambda x: x[1])
print(pares_ordenados)  # [(4, 'quatro'), (2, 'dois'), (3, 'três'), (1, 'um')]

# Usando com filter()
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Usando com map()
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]