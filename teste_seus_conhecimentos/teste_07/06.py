import copy

pessoas = ['Luiz', 'Maria', 'João', ['outras']]
# copia_de_pessoas = pessoas.copy() # shallow copy
copia_de_pessoas = copy.deepcopy(pessoas) # deep copy

copia_de_pessoas[0] = 'Paulo'
copia_de_pessoas[3][0] = 'Andreia'
print(pessoas)
print(copia_de_pessoas)

