from modulos.objetos import estados, dias
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
                print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
                print(f'''\033[36m{dia}\033[m - \033[35m{estado.estado.upper()}\033[m'''.center(52))
                print()
                sleep(1)

                for centro in centros:
                    estado.transporte.enviar_itens(centro)
                    centro.entrega.fazer_entrega()
                    if len(centro.itens) < 3000:
                        estado.transporte.abastecer_centro(centro)
                    if len(estado.itens) < 5000:
                        estado.abastecer_unidade()
                    sleep(2)
    except KeyboardInterrupt:
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
        print('\033[36m<<< FIM DA SIMULAÇÃO >>>\033[m')
        print()
        break