# Funções são Objetos

# Uma das propriedades interressantes do Python,
# e de outras linguagens também, é que funções são objetos.

# Quer dizer que funções podem ser usadas como quelquer outro objeto
# elas podem ser:

# * Atribuidos a variável
# * Inseridas em containers (listas, dicionarios, etc)
# * Passando como parâmetros
# * Retornadas por funções

def apply(func, val):
    return func(val)


def soma_mais_um(x):
    return x + 1


print(apply(soma_mais_um, 1))

