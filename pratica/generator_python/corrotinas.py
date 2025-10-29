# Corrotinas

def corrotinas():
    while True:
        print('Estou na corrotina')
        valor = yield
        print(f'Recebi: {valor}')


c = corrotinas()
next(c)
c.send('Davi')
c.send('Paulo')
