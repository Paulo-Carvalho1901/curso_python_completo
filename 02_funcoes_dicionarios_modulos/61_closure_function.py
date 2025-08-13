# Closure e funções que retornan outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom noite')

# print(falar_bom_dia('Paulo'))
# print(falar_boa_noite('Paulo'))

for nome in ['Paulo', 'Davi', 'Maria']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))