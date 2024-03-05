def load_unidade_estoque(unidade):
    from gerador_de_itens import gerar_itens
    import json
    filename = f'arquivos_json/estoques/ut/UT_{(unidade.estado.title()).replace(' ', '')}.json'
    try:
        with open(filename) as f:
            unidade_estoque = json.load(f)
    except FileNotFoundError:
        unidade.itens = gerar_itens(unidade, 40000)
        dump_unidade_estoque(unidade)
        with open(filename) as f:
            unidade_estoque = json.load(f)
    return unidade_estoque


def dump_unidade_estoque(unidade):
    import json
    filename = f'arquivos_json/estoques/ut/UT_{(unidade.estado.title()).replace(' ', '')}.json'
    with open(filename, 'w') as f:
        json.dump(unidade.itens, f)


def load_centro_estoque(centro):
    from gerador_de_itens import gerar_itens
    import json
    filename = f'arquivos_json/estoques/cd/CD_{(centro.bairro.title()).replace(' ', '')}.json'
    try:
        with open(filename) as f:
            centro_estoque = json.load(f)
    except FileNotFoundError:
        centro.itens = gerar_itens(centro, 10000)
        dump_centro_estoque(centro)
        with open(filename) as f:
            centro_estoque = json.load(f)
    return centro_estoque


def dump_centro_estoque(centro):
    import json
    filename = f'arquivos_json/estoques/cd/CD_{(centro.bairro.title()).replace(' ', '')}.json'
    with open(filename, 'w') as f:
        json.dump(centro.itens, f)


def carregar_dia(dias):
    import json
    try:
        with open('arquivos_json/status_tempo/dia_atual.json') as f:
            dias = json.load(f)
    except FileNotFoundError:
        salvar_dia(dias)
        with open('arquivos_json/status_tempo/dia_atual.json') as f:
            dias = json.load(f)
    return dias


def salvar_dia(dias):
    import json
    with open('arquivos_json/status_tempo/dia_atual.json', 'w') as f:
        json.dump(dias, f)


def carregar_semana(semana):
    import json
    try:
        with open('arquivos_json/status_tempo/semana_atual.json') as f:
            semana = json.load(f)
    except FileNotFoundError:
        salvar_semana(semana)
        with open('arquivos_json/status_tempo/semana_atual.json') as f:
            semana = json.load(f)
    return semana


def salvar_semana(semana):
    import json
    with open('arquivos_json/status_tempo/semana_atual.json', 'w') as f:
        json.dump(semana, f)
