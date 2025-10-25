# Variavel global
x = 10

def funcao():
    # variavel local
    y = 5
    print(f'Dentro da função - x: {x}, y: {y}')


funcao() # executando a funcao

# A variavel y não está disponível aqui
print(f'Fora da função - x: {x}')
# print(f'y:', {y}) # erro NameError: name 'y' is not define
