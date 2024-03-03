from modulos.objetos import estados, dias, campogrande, caminhao, van
from arquivos_json.save_and_load import (load_unidade_estoque,
                                        dump_unidade_estoque,
                                        load_centro_estoque,
                                        dump_centro_estoque)

from time import sleep

print('''\033[33m
<<< CTRL + C para interromper >>>\033[m
''')

while True:
    try:
        for dia in dias:
            for dicio in estados:
                estado = list(dicio.keys())[0]
                centros = dicio[estado]
                estado.itens = load_unidade_estoque(estado)
                print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
                print(f'''\033[36m{dia}\033[m - \033[35m{estado.estado.upper()}\033[m'''.center(52))
                print()
                sleep(1)

                for centro in centros:
                    centro.itens = load_centro_estoque(centro)
                    caminhao.enviar_itens(estado, centro)
                    valor, devolucao = van.fazer_entrega(centro)
                    if valor == 'devolver':
                        van.devolver_entrega(devolucao, centro)
                        caminhao.devolver_itens(devolucao, centro)
                    if len(centro.itens) < 3000:
                        caminhao.abastecer_centro(estado, centro)
                    if len(estado.itens) < 5000:
                        estado.abastecer_unidade()
                    dump_centro_estoque(centro)
                    dump_unidade_estoque(estado)
                    sleep(2)
    except KeyboardInterrupt:
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
        print('\033[36m<<< FIM DA SIMULAÇÃO >>>\033[m')
        print()
        break
