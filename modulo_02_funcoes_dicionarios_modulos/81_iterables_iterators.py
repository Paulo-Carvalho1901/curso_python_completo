# Generator expression, iterable e iterators em Python

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(10000)] # lista ja está todo na memoria
generator = (n for n in range(10)) # esta no primeiro ponto do generator, não esta na memoria

print(sys.getsizeof(lista)) # verifcando o tamanho em bytes
print(sys.getsizeof(generator))

# for n in generator:
#     print(n)