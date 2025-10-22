# Try execept, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
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
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro.')
finally:
    print('FECHAR ARQUIVO')
