# Iterando com while

"""
Geralmente a estrutura while se utiliza com
iterações que não sabemos sua parada (quando éla termina)
"""

# texto = 'Python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i])

#     i += 1

# print()
# exemplo de while com senha

# senha_salva = '1234'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print('Teve', repeticoes, 'repetiçoes')
# print('Aquele laço acima pode ter repetições infinitas!')


"""
Agora com o for é para as vezes que sabemos quantas iterações (repetiçoes terá)
"""

string = 'Python'

for letra in string:
    print(letra)
