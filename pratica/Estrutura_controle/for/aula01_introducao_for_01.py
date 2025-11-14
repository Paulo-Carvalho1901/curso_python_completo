# Iterando com while

"""
Geralmente a estrutura while se utiliza com
iterações que não sabemos sua parada (quando éla termina)
"""

texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i])

    i += 1
