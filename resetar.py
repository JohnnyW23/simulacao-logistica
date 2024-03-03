def resetar_estoques(caminho):
    import os
    try:
        for arquivo in os.listdir(caminho):
            caminho_arquivo = os.path.join(caminho, arquivo)
            os.remove(caminho_arquivo)
        print("Estoques resetados com sucesso!")
    except Exception as e:
        print(f"Erro ao resetar estoques: {e}")


resetar_estoques('arquivos_json/estoques_json/cd')
resetar_estoques('arquivos_json/estoques_json/ut')