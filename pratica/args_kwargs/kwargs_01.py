# Argumentos nomeados

def info_pessoa(**kwargs):
    """Imprimindo informações sobre uma pessoa"""
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')


info_pessoa(nome='Otavio', idade=30, profissao='Programador')
