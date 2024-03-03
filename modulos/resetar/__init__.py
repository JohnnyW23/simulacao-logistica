def resetar(caminho):
    import os
    try:
        for arquivo in os.listdir(caminho):
            caminho_arquivo = os.path.join(caminho, arquivo)
            os.remove(caminho_arquivo)
    except Exception as e:
        print(f"Erro ao resetar estoques: {e}")

def recomecar():
    import json
    resetar('arquivos_json/estoques_json/cd')
    resetar('arquivos_json/estoques_json/ut')
    resetar('arquivos_json/status_tempo')
    with open('arquivos_json/status_tempo/dia_atual.json', 'a') as f:
        f.write('')
    with open('arquivos_json/status_tempo/semana_atual.json', 'a') as f:
        json.dump(1, f)
    print("""
Programa resetado com sucesso!
""")
