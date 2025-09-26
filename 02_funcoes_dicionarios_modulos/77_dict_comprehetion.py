# Dictionary comprehention e Set comprehention

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'Categario': 'Escritorio'
}

# for chave, valor in produto.items():
#     print(chave, valor)


# dict comprehenrion
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in 
    produto.items()
}
print(dc)