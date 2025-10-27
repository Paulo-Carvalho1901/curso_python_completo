def func():
    pass

result = func()
print(result) # O returno de uma função se nao for especificado sempre será None

def add(x):
    def inner(y):
        return x + y
    return inner


print(add(1)(2))

# High Order Function
def diga_oi(nome):
    def formata_nome():
        return f'Olá, {nome}'
    resultado = formata_nome()
    return resultado

print(diga_oi('Paulo'))


# Compartilhamento de escopo
def add(x):
    def inner(y):
        return x + y
    return inner

funcao_interna = add(1) 
print(funcao_interna)

print(funcao_interna(10))
# variavel livre
