# Variaveis livres + nolocals (locals, globals)
def fora(x):
    a = x # vairavel livre

    def dentro():
        return a # free vars
    return dentro


dentro1 = fora(10)
demtro2 = fora(20)

print(dentro1())
print(demtro2())