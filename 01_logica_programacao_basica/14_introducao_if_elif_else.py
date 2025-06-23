# if / elif       / else
# if / se não     / se não

"""
LINKS PARA ESTUDOS
https://www.devmedia.com.br/estruturas-de-condicao-em-python/37158

Documentação oficial
https://docs.python.org/pt-br/3/tutorial/controlflow.html

"""

entrada = input('Você quer "entrar" ou "sair"? ' )

if entrada == 'entrar':
    print('Você entrou no sistema.')
    
    print(1234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar nem sair')

print('FORA DOD BLOCOS')