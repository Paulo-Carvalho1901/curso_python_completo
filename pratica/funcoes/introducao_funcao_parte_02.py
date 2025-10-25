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

# Parâmetros Nomeados

def saudacao(nome, mensagem):
    """Cria uma saudação personalizada."""
    return f"{mensagem}, {nome}!"

# Argumentos nomeados (a ordem não importa)
msg = saudacao(mensagem="Bom dia", nome="Ana")
print(msg)  # Saída: Bom dia, Ana!

# Misturando posicionais e nomeados
# Posicionais vêm primeiro, depois os nomeados
msg = saudacao("Carlos", mensagem="Boa tarde")
print(msg)  # Saída: Boa tarde, Carlos!

# Parâtros Padão

def saudacao(nome, mensagem="Olá"):
    """Cria uma saudação com mensagem padrão opcional."""
    return f"{mensagem}, {nome}!"

print(saudacao("Maria"))         # Saída: Olá, Maria!
print(saudacao("João", "Oi"))    # Saída: Oi, João!
