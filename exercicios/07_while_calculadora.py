# Exercicio calculadora

while True:
    # Solicitando campos ao usuário
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um outro numero: ')
    operador = input('Digite o operador (+-/*): ')
    
    numero_validos = None # criado a flag
    numero_1_float = 0
    numero_2_float = 0

    # Tratando os erros
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    # Verificando os operadores
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    # Criado a lógica do calculo
    print('Realizando sua conta: Confira o resultado a baixo.')
    if operador == '+':
        print(f'{numero_1_float}+{numero_2_float}=', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float}-{numero_2_float}=', numero_1_float - numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float}/{numero_2_float}=', numero_1_float / numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float}*{numero_2_float}=', numero_1_float * numero_2_float)

    # Validando campo sair
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
     