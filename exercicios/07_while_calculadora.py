# Exercicio calculadora

while True:
    # Solicitando campos ao usuário
    numero_1 = input('Digite um número.')
    numero_2 = input('Digite um outro numero')
    operador = input('Digite o operador (+-/*): ')


    # Validando campo sair
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
     