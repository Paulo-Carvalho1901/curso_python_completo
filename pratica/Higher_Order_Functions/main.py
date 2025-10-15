# A empresa do nosso melhor cliente vai nos visitar hoje
# e ele adora melancia!

frutas = ['melancia', 'banana', 'maça']

distancia_ir_feira = 2
def ir_a_feira(algo_a_fazer):
    x = 0
    while(x < distancia_ir_feira):
        x += 1

    return algo_a_fazer()


def varificar_se_tem(fruta):
    return 'Sim temos' if fruta in frutas else 'Não temos'


def check_preco():
    return 'Custa R$ 10,00 cada'



if __name__ == '__main__':
    print('Tem melancia?', ir_a_feira(lambda: varificar_se_tem('melancia')))
    print('preço ?', ir_a_feira(check_preco()))
