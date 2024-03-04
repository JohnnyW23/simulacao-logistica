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
    print("""
Programa resetado com sucesso!
""")
