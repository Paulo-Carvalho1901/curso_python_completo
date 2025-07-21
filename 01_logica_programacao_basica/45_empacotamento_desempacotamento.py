# Introdução ao desempacotamento + tuple (tuplas)

# nome1, nome2, nome3 = ['Paulo', 'Andreia', 'Davi']
# print(nome1)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)