from modulos.objetos import estados, dias
from time import sleep

for dia in dias:
    for dicio in estados:
        estado = list(dicio.keys())[0]
        centros = dicio[estado]
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
        print(f'''\033[36m{dia}\033[m - \033[35m{estado.estado.upper()}\033[m'''.center(52))
        print()
        sleep(1)

        for centro in centros:
            estado.transporte.enviar_itens(centro)
            centro.entrega.fazer_entrega()
            sleep(2)

print('<<< FIM DA SIMULAÇÃO >>>')
print()
