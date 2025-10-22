"""
Introdução ao try/execept
try -> tentar executar o código
execept -> ocorreu erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar: ')

#Fail fast

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um número!')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_float} é {numero_float * 2}')
# else:
#     print('Isso não é um número!')

