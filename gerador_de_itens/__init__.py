def gerar_itens(objeto, num):
    from random import randint
    for _ in range(num):
        item = {randint(19, 3500): True}
        objeto.itens.append(item)
    return objeto.itens


def gerar_mercadoria():
    from random import randint
    mercadoria = {randint(19, 3500): True}
    return mercadoria