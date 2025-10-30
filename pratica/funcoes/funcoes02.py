# Funções são Objetos

# Uma das propriedades interressantes do Python,
# e de outras linguagens também, é que funções são objetos.

# Quer dizer que funções podem ser usadas como quelquer outro objeto
# elas podem ser:

# * Atribuidos a variável
# * Inseridas em containers (listas, dicionarios, etc)
# * Passando como parâmetros
# * Retornadas por funções

# Função que recebe outra função
# High Order Function
def apply(func, val):
    return func(val)


def soma_mais_um(x):
    return x + 1


print(apply(soma_mais_um, 1))

# Esse é um conceitos por trás de diversas funções
# da biblioteca padrão do Python como:

# map, filter, sorted, functools.reduce, itertoos.takewhile

# Funções vs loops
# Uma das formas mais comuns de usar funções como objeto é
# poder evitar o uso de loops como for e while. Transformando a maneira
# imperativa de se programar, para uma forma declarativa

# Imperativa
seq = [1, 2, 3, 4, 5]
result = []

for val in seq:
    result.append(val ** 2)

print(result)

# declarativa
seq = [1, 2, 3, 4, 5]
result = map(lambda x: x ** 2, seq)

print(list(result))
