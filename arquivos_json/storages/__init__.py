def load_unidade_estoque(unidade):
    import json
    filename = f'arquivos_json/estoques_json/ut/UT_{(unidade.estado.title()).replace(' ', '')}.json'
    try:
        with open(filename) as f:
            unidade_estoque = json.load(f)
    except FileNotFoundError:
        dump_unidade_estoque(unidade)
        with open(filename) as f:
            unidade_estoque = json.load(f)
    return unidade_estoque

def dump_unidade_estoque(unidade):
    import json
    filename = f'arquivos_json/estoques_json/ut/UT_{(unidade.estado.title()).replace(' ', '')}.json'
    with open(filename, 'w') as f:
        json.dump(unidade.itens, f)


def load_centro_estoque(centro):
    import json
    filename = f'arquivos_json/estoques_json/cd/CD_{(centro.bairro.title()).replace(' ', '')}.json'
    try:
        with open(filename) as f:
            centro_estoque = json.load(f)
    except FileNotFoundError:
        dump_centro_estoque(centro)
        with open(filename) as f:
            centro_estoque = json.load(f)
    return centro_estoque

def dump_centro_estoque(centro):
    import json
    filename = f'arquivos_json/estoques_json/cd/CD_{(centro.bairro.title()).replace(' ', '')}.json'
    with open(filename, 'w') as f:
        json.dump(centro.itens, f)
