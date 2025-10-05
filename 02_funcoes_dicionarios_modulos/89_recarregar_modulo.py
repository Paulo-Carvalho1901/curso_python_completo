import importlib

import aula90_para_importar_modulo

print(aula90_para_importar_modulo.variavel)

for i in range(10):
    importlib.reload(aula90_para_importar_modulo)
    print(i)

print('Fim')
