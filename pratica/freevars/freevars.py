# Variaveis livres + nonlocal (locals, globals)

def fora(x):
    a = x # a é uma varivel livre

    def dentro():
        # print(locals())
        print(dentro.__code__.co_freevars)
        return a
    return dentro

dentro = fora(10)
dentro2 = fora(20)

print(dentro())
print(dentro2())
