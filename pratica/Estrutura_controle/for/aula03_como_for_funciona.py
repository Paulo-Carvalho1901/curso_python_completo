"""
Iterável -> str, range (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador 
"""

texto = 'Paulo'
for letra in texto:
    print(letra)
print()

# |--------------------------------------------------------------------|

texto = iter('Paulo') # __iter__()

print(next(texto)) # print(texto.__next__())
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print()
# Quando esgota os valores um erro é levantado
# |--------------------------------------------------------------------|


texto = 'Paulo' # iterável
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
