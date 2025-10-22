# Operador lógico "not"
# Usado para inverter expressão
# not True = False
# not False = True

senha = input('Senha: ')

# validando a senha 1
# if senha == '1234':
#     print('Entrou')
# else:
#     print('Senha incorreta!')

# validando senha invertendo 2 
# if senha != '1234':
#     print('Senha incorreta!')

# senha = input('Senha: ')

# velidando se usuário digitou algo
if not senha:
    print('Você não digitou nada')

print(not True)
print(not False)