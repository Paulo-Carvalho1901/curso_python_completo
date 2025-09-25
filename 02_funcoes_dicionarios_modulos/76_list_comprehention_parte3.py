def divisaoFn(x, y):
    return x / y


def multiplicacaoFn(x, y):
    return x * y


def potenciacaoFn(x, y):
    return x ** y

lista_original = [1, 2, 3, 4, 5] # criando uma lista de números
# Criando uma nova variavel e copiando o valor com list comprehention
divisao = [divisaoFn(numero, 2) for numero in lista_original] # mapeamento de lista para outra lista
multiplicacao = [multiplicacaoFn(numero, 2) for numero in lista_original] # mapeamento de lista para outra lista
quadrados = [potenciacaoFn(numero, 2) for numero in lista_original] # mapeamento de lista para outra lista

# Utilizando o for, o mesmo que tilizando list comprehention
# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)

# modificando a variavel numeros, indice 0, novo_valor = 20

print('lista original', lista_original) # aqui a variavel permanecerá com os valores iniciais
print('lista divisao', divisao) # aqui a variavel tera seu valor alterado
print('lista multiplicacao', multiplicacao) # aqui a variavel tera seu valor alterado
print('lista quadrados', quadrados) # aqui a variavel tera seu valor alterado

