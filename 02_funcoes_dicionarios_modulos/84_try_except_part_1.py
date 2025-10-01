# Try execept e finally

# imprimindo The Zen of Python, by Tim Peters (python -c 'import this')

a = 18
b = 0
# c = a / b

try:
    c = a / b # desta maneira o erro esta sendo silenciado
except:
    ...


print('continuar...')