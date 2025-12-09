# Ordem dos decoradores
def paramatros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)


        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@paramatros_decorador(nome='5')
@paramatros_decorador(nome='4')
@paramatros_decorador(nome='3')
@paramatros_decorador(nome='2')
@paramatros_decorador(nome='1')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
