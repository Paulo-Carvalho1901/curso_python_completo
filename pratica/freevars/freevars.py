# Variaveis livres + nonlocal

def fora(x):
    a = x # a é uma varivel livre

    def dentro():
        return a
    return dentro

dentro = fora(10)
dentro2 = fora(20)

print(dentro())
print(dentro2())
