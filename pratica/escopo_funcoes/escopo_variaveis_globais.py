# Modificando variaveis globais

contador = 0

def incrementar():
    global contador # Declara que contador se refere à variavel global
    contador += 1
    print(f'Contador dentro da função: {contador}')


print(f'Contador antes: {contador}') # Saída: contador antes 0
incrementar() # Saída: Contador  dentro da função: 1
print(f'Contador depois: {contador}') # Saída contador depois: 1
