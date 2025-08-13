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

# nome definido no escopo global (módulo)
um_nome = "um_nome (GLOBAL)"

