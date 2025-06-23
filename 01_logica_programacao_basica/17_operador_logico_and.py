# LINK PARA ESTUDO
# https://www.datacamp.com/pt/tutorial/python-logical-operators-introduction
# https://www-wscubetech-com.translate.goog/resources/python/logical-operators?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc&_x_tr_hist=true


# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('senha: ')
# senha_permitida = '1234'

# # if condição
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Operação de curto circuito
print(True and False and True)
print(True and 0 and True)
print(bool(''))