numeros = [1, 2, 3, 4, 5] # criando uma lista de números

# Criando uma nova variavel e copiando o valor com list comprehention
# novos_numeros = [numero for numero in numeros]

# Utilizando o for, o mesmo que tilizando list comprehention
novos_numeros = []
for numero in numeros:
    novos_numeros.append(numero)

# modificando a variavel numeros, indice 0, novo_valor = 20
numeros[0] = 20
print('numeros', numeros) # aqui a variavel tera seu valor alterado
print('novos_numeros', novos_numeros) # aqui a variavel permanecerá com os valores iniciais

