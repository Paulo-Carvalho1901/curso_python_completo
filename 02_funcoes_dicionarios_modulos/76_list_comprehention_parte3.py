lista_original = [1, 2, 3, 4, 5] # criando uma lista de números

# Criando uma nova variavel e copiando o valor com list comprehention
divisao = [numero / 2 for numero in lista_original] # mapeamento de lista para outra lista

# Utilizando o for, o mesmo que tilizando list comprehention
# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)

# modificando a variavel numeros, indice 0, novo_valor = 20

print('lista original', lista_original) # aqui a variavel permanecerá com os valores iniciais
print('lista alterada', divisao) # aqui a variavel tera seu valor alterado

