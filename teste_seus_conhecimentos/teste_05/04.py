"""
Funções podem usar parâmetros para receber valores. Parâmetro é o nome da "variável" 
entro dos parênteses, argumento é o valor passado para o parâmetro no momento 
da execução da função.

Sabendo disso, o código a seguir exibe o que na tela?
"""

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)