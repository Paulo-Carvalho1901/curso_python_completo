# Closure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao} {nome}'
    return saudar


saudacao_1 = criar_saudacao('Bom dia')
saudacao_2 = criar_saudacao('Boa noite')

print(saudacao_1('Paulo')) # clouse saudacao_1()
print(saudacao_2('Paulo'))
