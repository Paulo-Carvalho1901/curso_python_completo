print('Calculando o IMC')
nome = 'Paulo'
altura = 1.80
peso = 96
imc = peso / (altura * altura)
# imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'

print(linha_1)
print(linha_2)
print(f'{imc:.2f}')