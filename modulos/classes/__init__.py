from time import sleep

wrn = '\033[31m#\033[m'
# ^^^^ Só pra melhorar a estética do código quando uma mensagem de aviso ocorrer.

class Caminhao():
    def __init__(self, estoque=750, carga=[]):
        self.estoque = estoque
        self.carga = carga

    def enviar_itens(self, remetente, destino):
        from random import randint
        print('\033[34m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[m')
        print(f'''\033[36mENVIO DE MERCADORIAS\033[m''')
        envios = 0
        if len(destino.itens) < destino.estoque:  # Examina se o estoque do CD não estará cheio. Chance quase nula, mas possível.
            quantidade_itens = randint(self.estoque - self.estoque // 5, self.estoque) * randint(3, 5)
            caminhoes = quantidade_itens // 750 + 1
            for _ in range(quantidade_itens):
                self.carga.append(remetente.itens[0])  # Enchendo caminhões com itens da UT.
                remetente.itens.pop(0)
                envios += 1
                if len(remetente.itens) == 0:
                    print(f'''
{wrn} {remetente.local} sem mais itens restantes! {wrn}''')
                    break
            for _ in range(len(self.carga)):
                destino.itens.append(self.carga[0])  # Descarregando carga dos caminhões no CD.
                self.carga.pop(0)
                if len(destino.itens) == destino.estoque:
                    print(f'Estoque de {destino.local} totalmente abastecido.')
                    break
            print(f'''
Caminhões utilizados na operação: \033[33m{caminhoes}\033[m
Mercadorias transferidas: \033[36m{envios}\033[m
{remetente.local} >>> {destino.local}''')
            if len(self.carga) > 0:
                remetente.itens.extend(self.carga)
                self.carga = []
                print(f'Carga restante de {remetente.local} devolvida.')
            print(f'''
Estoque de {remetente.local}: {len(remetente.itens)}
Estoque de {destino.local}: {len(destino.itens)}''')
        else: print(f'''
{wrn} Operação não suportada:
Estoque de {destino.local} cheio! {wrn}''')
        sleep(1)

    def devolver_itens(self, remetente):
        copia = remetente.itens[:]
        for item in copia:
            for k, v in item.items():
                if v is False:
                    remetente.estado.itens.append({k: True})
                    if item in remetente.itens:
                        remetente.itens.remove(item)
                    if len(remetente.itens) == 0:
                        print(f'''
{remetente.local} sem mais itens para devolução.''')
                        break
                    elif len(remetente.estado.itens) == remetente.estado.estoque:
                        print(f'''
Estoque de {self.estado.local} totalmente abastecido.''')  # praticamente impossível de acontecer (cenário onde uma UT cheia
                        break                                  # 
        print(f'''
Mercadorias devolvidas:
>>> {remetente.local} >>> {remetente.estado.local}''')
        if len(self.carga) > 0:
            remetente.itens.extend(self.carga)
            self.carga = []
            print(f'''
Carga restante para devolução de {remetente.local} devolvida.''')
        print(f'''
Estoque de {remetente.local}: {len(remetente.itens)}
Estoque de {remetente.estado.local}: {len(remetente.estado.itens)}
''')
        sleep(1)

    def abastecer_centro(self, remetente, destino):
        from random import choice, randint
        print('''=====================================
\033[36mABASTECIMENTO DO CD\033[m''')
        envios = 0
        if len(remetente.itens) > 0:
            quantidade = randint(12000, 16000)
            caminhoes = quantidade // 750 + 1
            for _ in range(quantidade):
                item = choice(remetente.itens)
                self.carga.append(item)
                remetente.itens.remove(item)
                envios += 1
                if len(remetente.itens) == 0:
                    print(f'''
{wrn} {remetente.local} sem mais itens restantes! {wrn}''')
                    break
            for _ in range(len(self.carga)):
                destino.itens.append(self.carga[0])
                self.carga.pop(0)
            print(f'''
Caminhões utilizados na operação: \033[33m{caminhoes}\033[m
Mercadorias para abastecimento: \033[36m{envios}\033[m
{remetente.local} >>> {destino.local}''')
            if len(self.carga) > 0:
                remetente.itens.extend(self.carga)
                self.carga = []
                print(f'''\033[36m
Carga restante de {remetente.local} devolvida.\033[m''')
            print(f'''
Estoque de {remetente.local}: {len(remetente.itens)}
Estoque de {destino.local}: {len(destino.itens)}
''')
        else: print(f'''
{wrn} Transferência não suportada:
Não há itens no estoque de {remetente.local}! {wrn}
''')
        sleep(1)


class Van():
    def __init__(self, estoque=100, entrega=[], devolver=[], devolucao=[]):
        self.estoque = estoque
        self.entrega = entrega
        self.devolver = devolver
        self.devolucao = devolucao
    
    def fazer_entrega(self, remetente):
        from random import randint, shuffle
        quantidade_itens = randint(self.estoque - self.estoque // 5, self.estoque) * randint(30, 40)
        vans = quantidade_itens // 100 + 1
        for _ in range(quantidade_itens):
            self.entrega.append(remetente.itens[0])
            remetente.itens.pop(0)
            if len(remetente.itens) == 0:
                break
        entregue = devolvido = 0
        tentativas = len(self.entrega)
        endereco = Endereço(remetente.bairro, remetente.estado)
        for _ in range(len(self.entrega)):
            chance = randint(1, 10)
            if chance == 1:
                devolvido += 1
            else:
                entregue += 1
        shuffle(self.entrega)
        c = 0
        for _ in range(devolvido):
            self.devolver.append(self.entrega[c])
            c += 1
        self.entrega.clear()
        for item in self.devolver:
            for k, v in item.items():
                if v is True:
                    self.devolucao.append({k: False})
        print('''
=====================================''')
        print(f'''\033[36mENTREGA EM DOMICÍLIOS\033[m

Vans utilizadas na operação: \033[33m{vans}\033[m
{tentativas} tentativas de entrega em:
{endereco.endereco}

Entregas: {entregue}
Devoluções: {devolvido}
''')
        sleep(1)
        if len(self.devolucao) > 0:
            devolucao = self.devolucao[:]
            self.devolucao.clear()
            self.devolver.clear()
            valor = 'devolver'
            return valor, devolucao
    
    def devolver_entrega(self, devolucao, remetente):
        print('''=====================================''')
        print(f'\033[36mDEVOLUÇÃO DE ITENS\033[m')
        remetente.itens.extend(devolucao)
        if len(remetente.itens) == remetente.estoque:
            print(f'''
Estoque de {remetente.local} totalmente abastecido.''')  # praticamente impossível de acontecer.


class UnidadeDeTratamento():
    def __init__(self, estado):
        self.estado = estado
        self.local = f'\033[35mUT {estado}\033[m'
        self.estoque = 90000
        self.itens = []
    
    def abastecer_unidade(self):
        from gerador_de_itens import gerar_mercadoria
        from random import randint
        from time import sleep
        print('''=====================================
\033[36mABASTECIMENTO DA UT\033[m''')
        recebimento = 0
        abastecimento = randint(60000, 80000)
        for _ in range(abastecimento):
            mercadoria = gerar_mercadoria()
            self.itens.append(mercadoria)  # O item padrão denominado lá no início.
            recebimento += 1
        print(f'''
Mercadorias para abastecimento: \033[36m{recebimento}\033[m
>>> {self.local}

Estoque de {self.local}: {len(self.itens)}
''')
        sleep(1)


class CentroDeDistribuicao():
    def __init__(self, bairro, estado, estoque=20000):
        self.local = f'\033[33mCD {bairro}\033[m'
        self.bairro = bairro
        self.estado = estado
        self.estoque = estoque
        self.itens = []


class Endereço():
    def __init__(self, bairro, estado):
        self.bairro = bairro
        self.estado = estado
        self.endereco = f'\033[32m{bairro} - {estado.estado}\033[m'
        self.recebimento = []


def calcular_valor(unidade, centros):
    from time import sleep
    valor_unidade = 0
    for item in unidade.itens:
        valor_unidade += int(list(item.keys())[0])
    valor = f'\033[32mR$\033[m{valor_unidade:,}'.replace(',', '.')
    print(f'''
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
Valor do estoque de {unidade.local}:
                    {valor}''')
    for centro in centros:
        valor_centro = 0
        for item in centro.itens:
            valor_centro += int(list(item.keys())[0])
        valor = f'\033[32mR$\033[m{valor_centro:,}'.replace(',', '.')
        print(f'''Valor do estoque de {centro.local}:
                    {valor}''')
    print()
    sleep(3)
