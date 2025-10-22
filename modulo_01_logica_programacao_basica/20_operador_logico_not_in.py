# Operador in e not in
# Strings são iteraveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
nome = 'Otávio'
# print(nome[2])
# print(nome[-4])

# Operador in (está em nome?) expressão
print('vio' in nome)
print('á' in nome)
print('z' in nome)
print(10 * '-')
# Operador not in (não esta no nome?) expressão
print('vio' not in nome)
print('á' not in nome)
print('z' not in nome)

full_name = input('Enter your name: ')
find = input('Enter what wishe find: ')

if find in full_name:
    print(f"{find} It's in {full_name}")
else:
    print(f"{find} is not in {full_name}")
    