from modulos.objetos import estados, dias
from estoques.storages import (load_unidade_estoque,
                               dump_unidade_estoque,
                               load_centro_estoque,
                               dump_centro_estoque)
from time import sleep

print('''\033[33m
<<< CTRL + C para interromper >>>\033[m''')
while True:
    try:
        for dia in dias:
            for dicio in estados:
                estado = list(dicio.keys())[0]
                centros = dicio[estado]
                estado.itens = load_unidade_estoque(estado)
                print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
                print(f'''\033[36m{dia}\033[m - \033[35m{estado.estado.upper()}\033[m'''.center(52))
                print()
                sleep(1)

                for centro in centros:
                    centro.itens = load_centro_estoque(centro)
                    estado.transporte.enviar_itens(centro)
                    centro.entrega.fazer_entrega()
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
