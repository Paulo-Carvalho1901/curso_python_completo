"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[0:5])
print(variavel[:5])
print(variavel[::-1]) # invertendo a string
print(variavel[-1:-10:-1])
print(len(variavel)) # contando a string
print(variavel[0:9:])
