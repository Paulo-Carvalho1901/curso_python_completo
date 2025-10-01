# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


# exemplo de levantando um erro.
# print(123)
# raise ValueError('Deu erro!')
# print(456)


def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('dividiu por zero')


divide(8, 0)