from time import sleep
from estoques.ut_estoque import estoque_ut
from estoques.cd_estoque import estoque_cd

abastecimento_ut = {'item': True}
wrn = '\033[31m#\033[m'


class Caminhao():
    def __init__(self, estoque=750, carga=[]):
        self.estoque = estoque
        self.carga = carga

    def enviar_itens(self, remetente, destino):
        from random import choice, randint
        print('\033[34m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[m')
        print(f'''\033[36mENVIO DE MERCADORIAS\033[m''')
        envios = 0
        if len(destino.itens) < destino.estoque:
            if len(remetente.itens) > 0:
                for _ in range(randint(self.estoque - self.estoque // 5, self.estoque) * 4):
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
                    if len(destino.itens) == destino.estoque:
                        print(f'Estoque de {destino.local} totalmente abastecido.')
                        break
                print(f'''
Mercadorias transferidas: \033[36m{envios}\033[m
{remetente.local} >>> {destino.local}''')
                if len(self.carga) > 0:
                    print(self.carga)
                    remetente.itens.extend(self.carga)
                    self.carga = []
                    print(f'Carga restante de {remetente.local} devolvida.')
                print(f'''
Estoque de {remetente.local}: {len(remetente.itens)}
Estoque de {destino.local}: {len(destino.itens)}''')
            else: print(f'''{wrn }Transferência não suportada:
Não há itens no estoque de {remetente.local}! {wrn}''')
        else: print(f'''
{wrn} Operação não suportada:
Estoque de {destino.local} cheio! {wrn}''')
        sleep(1)

    def devolver_itens(self, devolucao, remetente):
        for item in devolucao:
            remetente.itens.remove(item)
            item.values() == True
            remetente.estado.itens.append(item)
            if len(remetente.itens) == 0:
                print(f'''
{remetente.local} sem mais itens para devolução.''')
                break
            elif len(remetente.estado.itens) == remetente.estado.estoque:
                print(f'''
Estoque de {self.estado.local} totalmente abastecido.''')
                break
        print(f'''
Mercadorias devolvidas:
>>> {remetente.local} >>> {remetente.estado.local}''')
        if len(self.carga) > 0:
            print(self.carga)
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
        from random import choice
        print('''=====================================
\033[36mABASTECIMENTO DO CD\033[m''')
        envios = 0
        if len(remetente.itens) > 0:
            for _ in range(12000, 16000):
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
Mercadorias para abastecimento: \033[36m{envios}\033[m
{remetente.local} >>> {destino.local}''')
            if len(self.carga) > 0:
                print(self.carga)
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
    def __init__(self, estoque=100, entrega=[], devolver=[]):
        self.estoque = estoque
        self.entrega = entrega
        self.devolver = devolver
    
    def fazer_entrega(self, remetente):
        from random import choice, randint
        for _ in range(randint(self.estoque - self.estoque // 5, self.estoque) * 35):
            item = choice(remetente.itens)
            self.entrega.append(item)
            remetente.itens.remove(item)
            if len(remetente.itens) == 0:
                break
        entregue = devolvido = 0
        tentativas = len(self.entrega)
        for _ in range(len(self.entrega)):
            endereco = Endereço(remetente.bairro, remetente.estado)
            chance = randint(1, 10)
            if chance == 1:
                self.entrega[0].values() == False
                self.devolver.append(self.entrega[0])
                self.entrega.pop(0)
                devolvido += 1
            else:
                self.entrega.pop(0)
                entregue += 1
        print('''
=====================================''')
        print(f'''\033[36mENTREGA EM DOMICÍLIOS\033[m

{tentativas} tentativas de entrega em:
{endereco.endereco}

Entregues: {entregue}
Devoluções: {devolvido}
''')
        sleep(1)
        if len(self.devolver) > 0:
            devolucao = self.devolver[:]
            self.devolver.clear()
            valor = 'devolver'
            return valor, devolucao
    
    def devolver_entrega(self, devolucao, remetente):
        print('''=====================================''')
        print(f'\033[36mDEVOLUÇÃO DE ITENS\033[m')
        for item in devolucao:
            remetente.itens.append(item)
            if len(remetente.itens) == remetente.estoque:
                print(f'''
Estoque de {remetente.local} totalmente abastecido.''')
        return devolucao


class UnidadeDeTratamento():
    def __init__(self, estado):
        self.estado = estado
        self.local = f'\033[35mUT {estado}\033[m'
        self.estoque = 90000
        self.itens = estoque_ut[:]
    
    def abastecer_unidade(self):
        from random import randint
        from time import sleep
        print('''=====================================
\033[36mABASTECIMENTO DA UT\033[m''')
        recebimento = 0
        abastecimento1 = randint(30000, 40000)
        abastecimento2 = randint(30000, 40000)
        abastecimento3 = abastecimento1 + abastecimento2
        for _ in range(abastecimento3):
            self.itens.append(abastecimento_ut)
            recebimento += 1
        print(f'''
Mercadorias para abastecimento: \033[36m{recebimento}\033[m
>>> {self.local}

Estoque de {self.local}: {len(self.itens)}
''')
        sleep(1)


class CentroDeDistribuicao():
    def __init__(self, bairro, estado, estoque=20000, itens=estoque_cd[:]):
        self.local = f'\033[33mCD {bairro}\033[m'
        self.bairro = bairro
        self.estado = estado
        self.estoque = estoque
        self.itens = itens


class Endereço():
    def __init__(self, bairro, estado):
        self.bairro = bairro
        self.estado = estado
        self.endereco = f'\033[32m{bairro} - {estado.estado}\033[m'
        self.recebimento = []
