# Try execept e finally

# imprimindo The Zen of Python, by Tim Peters (python -c 'import this')


try:
    a = 18
    b = 0
    print('linha 1')
    c = a / b
    print('linha 2')
except:
    print('ERRO: Dividiu por zero')


print('continuar...')