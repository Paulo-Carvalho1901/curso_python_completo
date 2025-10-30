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


print(apply(lambda x: x + 1, 2))
