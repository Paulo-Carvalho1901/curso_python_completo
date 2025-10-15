# Higher Order Function
# Função de primeira classe

# Link para esudo
# https://docs.python.org/pt-br/3.14/library/functools.html

"""
Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

"""


def saudacao(msg, nome):
    return f'{msg} {nome}'


def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Bom dia', 'Paulo'))
