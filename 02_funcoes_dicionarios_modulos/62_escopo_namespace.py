# Escopo e Namespace no python

# O que você vai aprender neste video:
# ** O que é escopo
# ** O que é namespace
# ** Uso de 'global()' e 'locals()' para introspecção do namespace
# ** Uso de 'vars()' e 'dir()' para introspecção do namespace
# ** Relação entre escopo e namespace
# ** A regra LEGB e como o Python a usa para resolver names
# ** Modificar o comportamento do Python com 'global' e 'nonlocal'


# Nota: quando eu usar a palavra "nome" sempre estarei me referindo
# indentificadores de algo: variáveis, funçao, classes, importes, etc...

#################################################################################

# O que é escopo

# Escopo é a região do código onde um nome está diretamente acessivel
# Ele determina os limites e o tempo de vida dos nomes definidos internamente

# Escopos é usados para encapsular o código e evitar colisões de nomes e efeitos
# colaterais indesejados

# o Python tem quatro tipo de escopo: Built-in, Global, Enclosing e Local
# esses escopos são dinâmicos. O interpretador pode criar e apagar em tempo de 
# execução

# Cada escopo tem seu "espaço de nomes" (namespace), que é um local onde os
# nomes e seus respectivos objetos são armazenados

##################################################################################

# O que é namespace?

#Namaspace é um estrutura de dados real que mapeia names para objetos. Cada
# chave é o nome que você define e o valor é o objeto correspondente no seu
# código. Sempre que você criar um name, essa associação é guardada dentro de um 
# namespace
# 
# Vamos usar glabals() e locals() no mesmo código anterior e confirmar isso
# 
# globals(): Retorna um dicionario que representa o namespace global no módulo
#            atual. isso inclui todos os nomes definidos na raiz do arquivo.
# locals():  Retorna um dicionario com os nomes definidos no escopo local onde
#            a função está sendo executada. Importante: ela só inclui nomes que 
#            já forem definidos antes da sua chamada.

#######################################################################################


# nome definido no escopo global (módulo)
um_nome = "um_nome (GLOBAL)"

# nome definido no escopo global (módulo)
def func_global(sou_local: str) -> None:
    # Escopo local (função e seus parametros)

    # um_nome no escopo local é OUTRA VARIAVEL (sem relação outro escopo)
    um_nome = "um_nome (LOCAL)" # nome definido no escopo local
    outro_nome = "outro_nome (LOCAL)" # nome definido no escopo local

    # Parâmetros de funções também são de escopo local no função
    print(f'Dentro da função: {um_nome}, {outro_nome}, {sou_local}')


# ISSO NÃO FUNCIONA
# print(outro_nome, sou_local)

# Isso é injetado automaticamente pelo Python no escopo Global
print('Nome do módulo:', __name__)
print('Arquivo do módulo:', __file__)
print('Documentação do módulo:', __doc__)
print() # apenas uma quebra de linha

func_global('arg (local)')
# saída - Dentro da função: um_nome (LOCAL), outro_nome (LOCAL), org (local)

print(f'Fora da função: {um_nome}') # Acessa a variável GLOBAL
# saída - Fora da função: um_nome (GLOBAL)
