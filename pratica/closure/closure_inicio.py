# Closure e funções que retornam outras funções

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao} {nome}'
    return saudar


saudacao_1 = criar_saudacao('Bom dia', 'Paulo')
saudacao_2 = criar_saudacao('Boa noite', 'Paulo')

print(saudacao_1()) # clouse saudacao_1()
print(saudacao_2())
