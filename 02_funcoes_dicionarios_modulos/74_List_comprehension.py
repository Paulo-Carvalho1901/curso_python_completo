# List comprehension em Python
# List comprehension é uma form rápida para criar listas
# a partir de iteráveis

# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero) 
# print(lista)

# List comprehension
lista = [numero * 2 for numero in range(10)]
print(lista)