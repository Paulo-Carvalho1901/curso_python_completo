"""
Repetições
while (enqunto)
while dentro de outro while
"""

# setando variavel qtd_linha e colunas iniciando com 5
qtd_linhas = 5
qtd_colunas = 5

# setando variavel linha 
linha = 1

# condição do while
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('FIM!')
