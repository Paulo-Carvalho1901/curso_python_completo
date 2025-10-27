# As funções lambdas tem um comportamento diferentes
# de funções tradicionais, elas não necessitam palavras return.
# O resultado da expressão sempre será o retorno dela

lambda x: x + 1
lambda x: 10 if x < 10 else x

