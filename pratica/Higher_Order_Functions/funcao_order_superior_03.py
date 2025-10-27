# Funções como Objetos de Primeira Classe

# Em Python, funções são objetos de primeira classe, o que significa que podem ser: - Atribuídas a
# variáveis - Passadas como argumentos para outras funções - Retornadas por outras funções -
# Armazenadas em estruturas de dados

# Funções com variáveis
def saudacao(nome):
    return f'Olá, {nome}'

# Atribuindo função e uma variável
f = saudacao

print(f('Maria'))
