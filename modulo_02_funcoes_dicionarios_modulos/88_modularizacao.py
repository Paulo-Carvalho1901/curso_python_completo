# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
# try:
#     import sys
#     sys.path.append()
# except ModuleNotFoundError:
#     ...
# import aula_88_modularizacao

# print('Esse modulo se chama:', __name__)
# print(*sys.path, sep='\n')

# import aula89
# from aula89 import variavel_modulo

# print(aula89.variavel_modulo)
# print(variavel_modulo)
