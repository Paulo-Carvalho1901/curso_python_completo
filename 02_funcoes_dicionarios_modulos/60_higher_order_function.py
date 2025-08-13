"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg} {nome}'


def executa(funcao, *args):
    return funcao(*args)


# saudacao_2 = saudacao
print(
    executa(saudacao, 'Bom dia', 'Paulo')
)

print(
    executa(saudacao, 'Bom dia', 'Davi')
)