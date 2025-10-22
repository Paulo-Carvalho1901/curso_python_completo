# dir, hasattr e getattr em Python

# dir(string) verificando os metodos

string = 'Luiz'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o metodo', metodo)