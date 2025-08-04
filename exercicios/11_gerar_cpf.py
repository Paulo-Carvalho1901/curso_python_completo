import random

for _ in range(10):
    nove_digito = ''
    for i in range(9):
        nove_digito += str(random.randint(0, 9))

    contador_regresivo_1 = 10 

    resultado_digito_1 = 0
    for digito in nove_digito:
        resultado_digito_1 += int(digito) * contador_regresivo_1
        contador_regresivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11 
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digito + str(digito_1)
    contador_regresivo_2 = 11
    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regresivo_2
        contador_regresivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11

    cpf_gerado_pelo_calculo = f'{nove_digito}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)
    