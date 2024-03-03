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


def salvar_status(dia, estado, centro):
    import json

    dados_dia = {
        "dia_atual": dia,
    }
    dados_estado_serializado = {
        "classe": "UnidadeDeTratamento",
        "atributos": {
            "estado": estado.estado,
            "local": estado.local,
            "estoque": estado.estoque,
            "itens": estado.itens,
    }
    }
    dados_centro_serializado = {
        "class": "CentroDeDistribuicao",
        "atributos": {
        "local": centro.local,
        "bairro": centro.bairro,
        "estado": {
            "class": "UnidadeDeTratamento",
            "atributos": {
                "estado": estado.estado,
                "local": estado.local,
                "estoque": estado.estoque,
                "itens": estado.itens
        },
        "estoque": centro.estoque,
        "itens": centro.itens,
    }
    }
    }
    with open('arquivos_json/status_simulacao/dia_atual.json', 'w') as f:
        json.dump(dados_dia, f)
    with open('arquivos_json/status_simulacao/estado_atual.json', 'w') as f:
        json.dump(dados_estado_serializado, f)
    with open('arquivos_json/status_simulacao/centro_atual.json', 'w') as f:
        json.dump(dados_centro_serializado, f)

def carregar_status_dia():
    import json
    try:
        with open('arquivos_json/status_simulacao/dia_atual.json') as f:
            dados = json.load(f)
            return dados["dia_atual"]       
    except json.decoder.JSONDecodeError:
        return None

def carregar_status_estado():
    import json
    try:
        with open('arquivos_json/status_simulacao/estado_atual.json') as unidade_serializada:
            dados = json.load(unidade_serializada)
            classe = globals()[dados["class"]]
            unidade_atual = classe(**dados["atributos"])
            return unidade_atual  
    except json.decoder.JSONDecodeError:
        return None

def carregar_status_centro():
    import json
    try:
        with open('arquivos_json/status_simulacao/centro_atual.json') as centro_serializado:
            dados = json.load(centro_serializado)
            classe = globals()[dados["class"]]
            centro_atual = classe(**dados["atributos"])
            return centro_atual
    except json.decoder.JSONDecodeError:
        return None
    