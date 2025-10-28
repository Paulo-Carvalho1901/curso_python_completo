# Geradores

# for val in [1, 2, 3]:
#     print(val)


# def gerador():
#     yield 1
#     yield 2
#     yield 3

# for val in gerador():
#     print(val)



def gerador():
    yield 1
    yield 2
    yield 3


g =  gerador()
print(next(g))
print(next(g))
print(next(g))
