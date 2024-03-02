def load_unidade_estoque(unidade):
    import json
    filename = f'UT_{(unidade.estado.title()).replace(' ', '')}.json'
    try:
        with open(filename) as f:
            unidade_estoque = json.load(f)
    except FileNotFoundError:
        dump_unidade_estoque(unidade) 
    else:
        return unidade_estoque

def dump_unidade_estoque(unidade):
    import json
    filename = f'UT_{(unidade.estado.title()).replace(' ', '')}.json'
    with open(filename, 'w') as f:
        json.dump(unidade.itens, f)
        load_unidade_estoque(unidade)


def load_centro_estoque(centro):
    import json
    filename = f'CD_{centro.bairro}.json'
    pass