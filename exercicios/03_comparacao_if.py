"""
Crie um programa que compare dois valores
e exiba na tel qual é o maior
"""

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior ou igual do que {primeiro_valor=}')
    