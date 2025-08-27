# Manipulando chaves e valores em dicionários

pessoa = {}

# add algo em um dicionário vazio
chave = 'nome'
pessoa[chave] = 'Paulo Carvalho'

# add chave sobrenome com valor
pessoa['sobrenome'] = 'Carvalho'
# print(pessoa[chave])

# reatribuindo a chave a outro valor 'rescrevendo o valor'
pessoa[chave] = 'Davi'

# apagando chave do dicionário
del pessoa['sobrenome']
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE!')
else:
    print(pessoa['sobrenome'])

# acessando o valor pela chave do dicionário
# print(pessoa['nome'])
