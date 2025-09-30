# Introdução às Generator functions em Python
# generator = (n for n in range(10000))

def generator(n=0):
    yield 1 # pausar
    print('continueando...')
    yield 2 # pausar


gen = generator(n=0)
print(gen.__iter__())
print(next(gen))
print(next(gen))
