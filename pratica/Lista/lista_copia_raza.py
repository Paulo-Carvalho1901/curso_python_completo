# Estudando sobre listas


# Lista com strings
lista_a = [1, 2, 3]
lista_b = lista_a[:]
lista_a.append(4)

print(lista_a)
print(lista_b)

print(id(lista_a))
print(id(lista_b))