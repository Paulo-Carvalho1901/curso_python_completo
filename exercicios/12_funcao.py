# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
       total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)

# Criar uma função fala se um número é par ou impar.
# Retorno se o número é par ou impar


def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} digitado é PAR.'
    return f'{numero} digitado é IMPAR.'

print(par_impar(2))
print(par_impar(3))
print(par_impar(13))
print(par_impar(68))
