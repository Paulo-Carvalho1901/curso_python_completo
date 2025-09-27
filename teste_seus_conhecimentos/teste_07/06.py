pessoas = ['Luiz', 'Maria', 'João']
copia_de_pessoas = pessoas.copy() # shallow copy


copia_de_pessoas[0] = 'Paulo'
print(pessoas)
print(copia_de_pessoas)
