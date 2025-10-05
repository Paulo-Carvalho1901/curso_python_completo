# from sys import path

# # Tipos de importações
# import aula91_packages
# from aula91_packages import modulo
# from aula91_packages.modulo import *


# # print(*path, sep='\n')

# print(modulo.soma(1, 3))
# print(aula91_packages.modulo.soma(1, 2))
# print(variavel)
# print(nova_variavel)

from aula91_packages.modulo import soma, fala_01

print(__name__)
print(soma(2, 2))
fala_01()