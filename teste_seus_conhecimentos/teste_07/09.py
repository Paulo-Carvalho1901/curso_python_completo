# Calculadora do Imposto de Renda

# Função para calcular o imposto com base no salario bruto
def calcular_imposto(salario):
    # Verificar em qual faixa o salario se encaixa
    if salario <= 2112:
        imposto = 0
    elif salario <= 2826.65:
        imposto = salario * 0.075 - 158.40
    elif salario <= 3751.05:
        imposto = salario * 0.15 - 370.40
    elif salario <= 4664.68:
        imposto = salario * 0.225 - 651.73
    else:
        imposto = salario * 0.275 - 884.96

    if imposto < 0:
        imposto = 0

    return imposto

# exibe na tela perguntando ao usuário sobre o salario bruto
salario_bruto = float(input('Digite seu salario bruto: R$ '))

# Calcula o imposto e o salario líquido
imposto = calcular_imposto(salario_bruto)
salario_liquido = salario_bruto - imposto

# Mostra os resultados 
print('\nSalário Bruto: R$ {:.2f}'.format(salario_bruto))
print('Imposto de Renda: R$ {:.2f}'.format(imposto))
print('Salário Líquido: R$ {:.2f}'.format(salario_liquido))
