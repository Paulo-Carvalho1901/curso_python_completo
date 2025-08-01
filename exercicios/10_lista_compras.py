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
        indice_str = input('Escolha uma índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro.')
        except IndexError:
            print('índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Não há nada para listar!')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l. ')()