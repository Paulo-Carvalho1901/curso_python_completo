# LEGB, Global, Nonlocal, Enclosing e Call Stack

# PARTE 2
# A regra LEGB e como o Python a usa para resolver names
# Modificar o comportamento do Python com gloval e nonlocal
# * PARA NEERDS freevars e cellvars

# O Python segue uma ordem especifica e unidurecional para busca por names
# Ordem sempre vai do escopo mais interno para o mais externo

# Certo: Local -> Enclosing -> Global -> Built-in -> NoneError
# Errado: Built-in -> Global -> Enclosing -> local

# De nemhum espaço externo é possivel usar algo de espaço interno

##############################################################################


nome_global = 'nome_global'


def func_global() -> None:
    nome_enclosing = 'nome_enclosing' # Enclosing (local)

    def funcao_interna() -> None:
        nome_local = 'nome_local' # local

        print(
            'LOCAL:',
            nome_local,
            nome_enclosing,
            'funcao_interna',
            nome_global,
            '+builting',
        )

    funcao_interna()
    print(
        'ENCLOSING',
        nome_enclosing,
        'funcao_interna',
        'funcao_global',
        nome_global,
        '+builtins',
    )

func_global()
print('GLOBAL:', nome_global, 'func_global', '+builtins')
