"""
É comum usar laços de repetição aninhados (while dentro de while) 
para repetir alguma coisa dentro de uma repetição existente.

Para tabelas, temos linhas e colunas; para cada linha, posso ter n colunas. Por exemplo: 
para uma tabela de 5 linhas e 5 colunas, isso significa que eu tenho 5 
repetições de coluna dentro de cada repetição de linha.

"""

linhas = 2
colunas = 2
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1