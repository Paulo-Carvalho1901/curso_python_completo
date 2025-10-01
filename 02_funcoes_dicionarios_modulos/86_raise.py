# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


# exemplo de levantando um erro.
# print(123)
# raise ValueError('Deu erro!')
# print(456)

def nao_pode_ser_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você esta tentando dividir por zero.')
    return True


def deve_ser_int_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou flot.'
            f'{tipo_n.__name__} enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    nao_pode_ser_zero(d)
    return n / d

print(divide(8, '0'))