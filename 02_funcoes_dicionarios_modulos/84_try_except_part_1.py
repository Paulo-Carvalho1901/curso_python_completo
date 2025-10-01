# Try execept e finally

# imprimindo The Zen of Python, by Tim Peters (python -c 'import this')


try:
    a = 18
    b = 0
    # print(b[0])
    print('linha 1'[100])
    c = a / b
    print('linha 2')
except ZeroDivisionError:
    print('ERRO: Dividiu por zero')
except NameError:
    print('ERRO: is not defined')
except (TypeError, IndexError):
    print('ERRO: erro de tipo')
except Exception:
    print('ERRO: Desconhecido')


print('continuar...')