def externa():
    x = 10

    def interna():
        nonlocal x # Refere-se à veriavel x da função externa
        x += 5
        print(f'x dentro da função interna: {x}')
        
    print(f'x antes da função interna: {x}')
    interna()
    print(f'x depois da função interna: {x}')


externa()
# Saída
# x antes da função interna: 10
# x dentro da função interna: 15
# x depois da função interna: 15
