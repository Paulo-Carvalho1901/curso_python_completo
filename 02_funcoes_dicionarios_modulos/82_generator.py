# Introdução às Generator functions em Python
# generator = (n for n in range(10000))

def generator(n=0, max=10):
    while True:
        yield n
        n += 1

        if n >= max:
            return

    # yield 1 # pausar
    # print('continuando...')
    # yield 2 # pausar
    # print('mais um...')
    # yield 3 # pausar
    # print('vou terminar')
    # return 'fim'


gen = generator(n=5, max=15)
# print(gen.__iter__())
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)