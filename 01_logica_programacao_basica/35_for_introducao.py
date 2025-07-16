# texto = 'python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)


#     i += 1

senha_salva = '1234'
senha_digitada = ''
repeticaoes = 0


while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticaoes}x): ')

    repeticaoes += 1

print(repeticaoes)
print('Aquele laço acima pode ter repetições infinitas.')
