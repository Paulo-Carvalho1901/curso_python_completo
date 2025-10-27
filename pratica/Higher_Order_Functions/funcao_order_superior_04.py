# Uma propridade especial de função em Python é 
# o fato delas serem objetos também. O quer dizer as funções também pode ser passadas
# como argumentos. Chamamos isso de função de ordem superior (High Order Function)
# Aqui onde as funções anônimas brilham.

def aplica_em_tudo(func, *args):
    result = []
    for val in args:
        result.append(func(val))
    return result

print(aplica_em_tudo(lambda x: x + 1, 1, 2))
print(aplica_em_tudo(lambda x: x + 1, 1, 2, 3))
print(aplica_em_tudo(lambda x: x + 1, 1, 2, 3, 4))
print(aplica_em_tudo(lambda x: x + 1, 1, 2, 3, 4, 5))
