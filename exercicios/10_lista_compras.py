'''
Faça uma lista de compras com listas
o usuario deve ter a possibilidade de
inserir, apagar, e lista valores de sua lista
não permita que o programa quebre com
erros de indices inexistentes na lista
'''
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        print('i')
    elif opcao == 'a':
        print('a')
    elif opcao == 'l':
        print('l')
    else:
        print('Por favor, escolha i, a ou l. ')()