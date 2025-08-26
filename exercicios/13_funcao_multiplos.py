# Exercicio
# Crie funções que duplique, triplique, e quadruplique
# o número recebido com paramtros

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplica(numero):
#     return numero * 4

# Criando uma função multiplicador
def criar_multiplicador(multiplicador):
    # dentro dessa função criando outra função multiplicar
    def multiplicar(numero):
        # retornando numero * multiplicador
        return numero * multiplicador
    # retornando multiplicar
    return multiplicar
    
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
