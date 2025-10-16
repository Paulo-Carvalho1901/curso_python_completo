# Closure e funções que retornam outras funções

def criar_saudacao(saudacao, nome):
    return f'{saudacao} {nome}'


saudacao_1 = criar_saudacao('Bom dia', 'Paulo')
print(saudacao_1)