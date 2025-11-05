# Variaveis livres + nolocals (locals, globals)

# Uma variavel livre é quando utilizamos uma variavel interna
# de uma função que esta declarada em uma função externa

# print(globals())

# def fora(x):
#     a = x # vairavel livre

#     def dentro():
#         print(locals())
#         return a # free vars
#     return dentro


# dentro1 = fora(10)
# demtro2 = fora(20)

# print(dentro1())
# print(demtro2())


def concatenar(string_inicial):
    valor_final = string_inicial


    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)