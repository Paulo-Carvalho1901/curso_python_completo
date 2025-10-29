# Subs geradores 

# Uma das condições especiais de geradores é que eles podem delegar
# uma tarefa e outro gerador. Chamamos de sub geradores.

def gerador():
    val = 0
    while True:
        yield val
        val += 1


def subgerador():
    yield from gerador()

g = subgerador()
# print(next(g))
# print(next(g))
# print(next(g))


# Aplicação gerador
def minigerador():
    yield 'Maria'
    yield 'Julio'


def subgerador():
    yield from minigerador()
    yield from gerador()


sg = subgerador()
print(next(sg))
print(next(sg))
print(next(sg))
print(next(sg))
print(next(sg))