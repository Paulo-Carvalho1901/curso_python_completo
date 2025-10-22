# from sys import path

# https://stackoverflow.com/questions/2386714/why-is-import-bad

# # Tipos de importações
# import aula91_packages
# from aula91_packages import modulo
# from aula91_packages.modulo import *


# # print(*path, sep='\n')

# print(modulo.soma(1, 3))
# print(aula91_packages.modulo.soma(1, 2))
# print(variavel)
# print(nova_variavel)

# from aula91_packages.modulo import soma, fala_01

# print(__name__)
# print(soma(2, 2))
# fala_01()

from aula91_packages import soma, qualquer_coisa, variavel, nova_variavel

print(soma(2, 2))
qualquer_coisa()
