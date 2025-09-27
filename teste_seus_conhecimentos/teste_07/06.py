import copy

pessoas = ['Luiz', 'Maria', 'João', ['outras']]
# copia_de_pessoas = pessoas.copy() # shallow copy
copia_de_pessoas = copy.deepcopy(pessoas) # deep copy

copia_de_pessoas[0] = 'Paulo'
copia_de_pessoas[3][0] = 'Andreia'
print(pessoas)
print(copia_de_pessoas)

names = {
    'firstname': 'Paulo',
    'lastname': 'Carvalho',
    'adresses': [
        {'linha1': 'AV Brasil', 'linha2': 30},
        {'linha1': 'Rua Teste', 'linha2': 15},
    ]
}

# copy_of_names = names.copy() # shallow
copy_of_names = copy.deepcopy(names) # deepcopy


copy_of_names['firstname'] = 'Andreia'
copy_of_names['adresses'][1]['linha1'] = 'Mudei'
copy_of_names['adresses'][1]['linha2'] = 33
print(names)
print(copy_of_names)
