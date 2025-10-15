# O que são funções de ordem superior?
# São funções que podem aceita outras funções
# como argumentos retorna funções, ou ambas

# função importantes no python
# Map, Filter

# def filtro(t):
#     return t > 25


nums = [1, 23, 365, 25, 263, 245, 5, 4, 88, 52, 62, 67, 54, 14, 23]
maior_25 = list(filter(lambda x: x > 25, nums))

print(list(map(lambda x: x ** 2, maior_25)))
