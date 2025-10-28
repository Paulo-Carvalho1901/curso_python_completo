# Geradores

# for val in [1, 2, 3]:
#     print(val)


# def gerador():
#     yield 1
#     yield 2
#     yield 3

# for val in gerador():
#     print(val)



# def gerador():
#     yield 1
#     yield 2
#     yield 3


# g =  gerador()
# print(next(g))
# print(next(g))
# print(next(g))


# def gerador():
#     val = 0
#     while True:
#         yield val
#         val += 1


# g = gerador()
# print(next(g))
# print(next(g))
# print(next(g))


"""
Essa condição de só calcular quando for chamado,
por conta da simetria, se chama "avaliação preguiçosa"
[Lazy Evaluation]
"""

def gerador(start=0, step=1):
    while True:
        yield start
        start += step


g = gerador()
print(next(g))
print(next(g))
print(next(g))