# Exercicio calculadora

while True:
    # Solicitando campos ao usuário
    numero_1 = input('Digite um número.')
    numero_2 = input('Digite um outro numero')
    operador = input('Digite o operador (+-/*): ')
    
    numero_validos = None # criado a flag

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

    # Validando campo sair
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
     