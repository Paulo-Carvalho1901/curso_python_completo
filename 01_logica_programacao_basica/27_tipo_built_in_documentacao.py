"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'paulo Carvalho'
outra_variavel = f'{string[:3]}ABC {string[4:]}'
print(string)
# string[3] = 'ABC'
print(outra_variavel)

print(string.capitalize())
print(string.zfill(50))
