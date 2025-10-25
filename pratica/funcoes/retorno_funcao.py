# Retorno de valores das funçoes (return)


def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y # retun


# variavel = soma(1, 2) # None é não valor
# variavel = int('1')
# print(variavel)
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(11, 55)

# Sem retorno
def saudacao(nome):
    """Imprimir uma saudação e não retorna valor explícito."""
    print(f'Olá', {nome})


# A função retorna None implicitamente
resultado = saudacao('Maria')
print(f'Valor retornado:', {resultado}) # Saída: valor reotornado: None

# Retorno um valor
def quadrado(numero):
    """Retorno o quadrado de número."""
    return numero ** 2


resultado = quadrado(5)
print(f'O quadrado de 5 é {resultado}') 

# Retornando varios valores
def minmax(numeros):
    """Retornando o menor e o maior valor de um sequencia."""
    return min(numeros), max(numeros)


# Desempacotamento de tupla
menor, maior = minmax([5, 2, 8, 1, 9])
print(f'Menor: {menor}, Maior: {maior}')


# Retorno condicional
def divisao_segura(a, b):
    """Divide a por b, tratando divisão por zero."""
    if b == 0:
        return 'Erro: Divisão por zero.'
    else:
        return a / b
    
print(divisao_segura(10, 2))
print(divisao_segura(10, 0))
