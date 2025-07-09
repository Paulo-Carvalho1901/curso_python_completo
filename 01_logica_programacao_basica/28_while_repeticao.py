"""
Repetições
while (enqunto)
Excutar uma ação enquanto uma condicão for verdaeira
Loop infinito -> Quando um código não tem fim 
"""
# criando a condição a ser testada
condicao = True

# inicio do while
while condicao:
    nome = input('Qual é seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
    # condição de parada
        break

print('ACABOU!')