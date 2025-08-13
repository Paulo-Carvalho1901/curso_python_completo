# Closure e funções que retornan outras funções

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar



s1 = criar_saudacao('Bom dia', 'Paulo')
s2 = criar_saudacao('Bom noite', 'Paulo')

print(s1())
print(s2())