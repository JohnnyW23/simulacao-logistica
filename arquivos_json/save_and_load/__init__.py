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

def salvar_dia(dias):
    import json
    with open('arquivos_json/status_tempo/dia_atual.json', 'w') as f:
        json.dump(dias, f)

def carregar_dia():
    import json
    try:
        with open('arquivos_json/status_tempo/dia_atual.json') as f:
            dados = json.load(f)
            return dados
    except json.decoder.JSONDecodeError:
        return None

def salvar_semana(semana):
    import json
    with open('arquivos_json/status_tempo/semana_atual.json', 'w') as f:
        json.dump(semana, f)

def carregar_semana():
    import json
    with open('arquivos_json/status_tempo/semana_atual.json') as f:
        dados = json.load(f)
        return dados