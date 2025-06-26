"""
É possível adicionar um if dentro de outro fazendo várias condições ]
aninhadas. Com isso em mente, o que você acha que o 
código abaixo exibe na tela?
"""

numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')