from modulos.objetos import estados, dias, caminhao, van
from arquivos_json.save_and_load import (load_unidade_estoque,
                                        dump_unidade_estoque,
                                        load_centro_estoque,
                                        dump_centro_estoque,
                                        salvar_dia, carregar_dia,
                                        salvar_semana, carregar_semana)
days = dias[:]
from time import sleep
print('''\033[33m
<<< CTRL + C para interromper >>>\033[m
''')
while True:
    try:
        semana = carregar_semana()
        dias = carregar_dia()
        if dias == None:  # ou seja, se ainda não houve salvamento do dia
            dias = days
        dia = dias[0]
        for dicio in estados:
            estado = list(dicio.keys())[0]
            centros = dicio[estado]
            estado.itens = load_unidade_estoque(estado)
            print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
            print(f'''\033[34mSEMANA {semana}\033[m'''.center(40))
            print()
            print(f'''\033[36m{dia}\033[m - \033[35m{estado.estado.upper()}\033[m'''.center(52))
            print()
            sleep(1)
            for centro in centros:
                centro.itens = load_centro_estoque(centro)
                caminhao.enviar_itens(estado, centro)
                valor, devolucao = van.fazer_entrega(centro)  # Confere se haverá devolução. A chance de não haver é quase nula,
                if valor == 'devolver':                       # mas ainda existe. Se isso é possível, então um dia irá acontecer.
                    van.devolver_entrega(devolucao, centro)
                    caminhao.devolver_itens(devolucao, centro)
                if len(centro.itens) < 3000:
                    caminhao.abastecer_centro(estado, centro)
                if len(estado.itens) < 5000:
                    estado.abastecer_unidade()
                sleep(1)
        if dia == 'SÁBADO':
            semana += 1
            salvar_semana(semana)
        dias = [dias[1],
                dias[2],
                dias[3],
                dias[4],
                dias[5],
                dias[0]]
        salvar_dia(dias)  # o dia é salvo assim que se passa pro próximo
        for dicio in estados:
            estado = list(dicio.keys())[0]
            centros = dicio[estado]
            dump_unidade_estoque(estado)
            for centro in centros:
                dump_centro_estoque(centro)  # todo o inventário dos objetos é salvo assim que se passa pro próximo dia
    except KeyboardInterrupt:
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
        print('\033[36m<<< FIM DA SIMULAÇÃO >>>\033[m')
        print()
        break
