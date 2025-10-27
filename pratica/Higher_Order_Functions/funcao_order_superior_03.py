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

# Função com argumentos
def aplicar_operação(func, valor):
    """Aplicando uma função a valor e retorna o resultado"""
    return func(valor)

def dobro(x):
    return x * 2

def quadrado(x):
    return x ** 2


print(aplicar_operação(dobro, 5))
print(aplicar_operação(quadrado, 5))
