# Try execept, else e finally

# No caso do finally ele sempre será executado

try:
    print('ABRIR ARQUIVO')
    # print(2 / 0)
except ZeroDivisionError:
    print('ERRO: Dividiu por zero.')
else:
    print('Não deu erro.')
finally:
    print('FECHAR ARQUIVO')
