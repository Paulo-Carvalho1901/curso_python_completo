# Corrotinas

def corrotinas():
    print('Estou na corrotina')
    valor = yield
    print(f'Recebi: {valor}')


c = corrotinas()
next(c)
