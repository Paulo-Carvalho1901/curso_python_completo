# Try execept, else e finally

# No caso do finally ele sempre será executado

try:
    print('ABRIR ARQUIVO')
    print(2 / 0)
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('ERRO: Dividiu por zero.')
except IndexError as error:
    print('IndexError')
else:
    print('Não deu erro.')
finally:
    print('FECHAR ARQUIVO')
