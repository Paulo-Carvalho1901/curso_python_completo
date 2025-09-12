# Empacotamento e desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a
# print(a, b)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoas = {
    'idade': 16,
    'altura': 1.60,
}

# desempacotamento
# a, b = pessoa.values()
# # print(a, b)

# # desempacotamento interno
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)


# # itenrando com for
# for chave, valor in pessoa.items():
#     print(chave, valor) # retorna uma tupla com valor


pessoa_completa = {**pessoa, **dados_pessoas}
# print(pessoa_completa)

# args e Kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# utilizando argumento nomeados para desempacotamento
mostro_argumentos_nomeados(1, 2, nome='Paulo', qlq=123)

