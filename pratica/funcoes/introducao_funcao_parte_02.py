# sintax básica

def nome_da_funcao(parametro1, parametro2):
    """Docstring: Documentaçao da função"""
    # Corpo da função
    # Código que será executada quando a função for chamada
    return # valor opcional 

#  exemplo simples

def saudacao():
    """Imprimindo uma saudação."""
    print('Olá, mundo!')

#chamada da função
saudacao() # Sáida: Olá, mundo!

# Parâmetros e Argumentos
 
# Parâmetro posicionais
def somar(a, b):
    """Soma dois números e retorna o resultado"""
    return a + b


# Chamada com argumentos posicionais
resultado = somar(5, 3) # resultado 8
print(resultado)
