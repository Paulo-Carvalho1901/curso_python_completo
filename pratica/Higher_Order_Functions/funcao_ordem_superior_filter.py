# filter: filterrecebe uma função e um iterável como argumentos e 
# retorna um novo iterável que contém apenas os elementos do iterável original 
# para os quais a função retorna True. Por exemplo:

def is_evev(x):
    return x % 2 == 0


numeros = [1, 2, 3, 4, 5]
numero_quadrado = list(filter(is_evev, numeros))
print(numero_quadrado)
