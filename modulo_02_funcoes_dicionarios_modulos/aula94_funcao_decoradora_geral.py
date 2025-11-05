# Função decoradora e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções 
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções

# Função decoradora
def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna # clousure


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser uma string!')




invertendo_string_checando_parametro = criar_funcao(inverte_string)
invertida = invertendo_string_checando_parametro(123)
print(invertida)
