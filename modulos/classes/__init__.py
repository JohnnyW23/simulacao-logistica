from time import sleep
from estoques.ut_estoque import estoque_ut
from estoques.cd_estoque import estoque_cd
itens_cd = []
itens_ut = []
for item in estoque_cd:
    itens_cd.append({item: True})
for item in estoque_ut:
    itens_ut.append({item: True})
estoque_ut = itens_ut
estoque_cd = itens_cd


class Caminhao():
    def __init__(self, unidade, estoque=1000):
        self.unidade = unidade
        self.estoque = estoque
        self.carga = []

    def enviar_itens(self, destino):
        from random import choice, randint
        envios = 0
        if len(destino.itens) < destino.estoque:
            if len(self.unidade.itens) > 0:
                for _ in range(randint(self.estoque - self.estoque // 5, self.estoque)):
                    item = choice(self.unidade.itens)
                    self.carga.append(item)
                    self.unidade.itens.remove(item)
                    envios += 1
                    if len(self.unidade.itens) == 0:
                        print(f'{self.unidade.local} sem mais itens restantes.')
                        break
                for _ in range(len(self.carga)):
                    destino.itens.append(self.carga[0])
                    self.carga.pop(0)
                    if len(destino.itens) == destino.estoque:
                        print(f'Estoque de {destino.local} totalmente abastecido.')
                        break
                print(f'''\033[36mENVIO DE MERCADORIAS\033[m

Mercadorias transferidas: \033[36m{envios}\033[m
{self.unidade.local} >>> {destino.local}''')
                if len(self.carga) > 0:
                    print(self.carga)
                    self.unidade.itens.extend(self.carga)
                    self.carga = []
                    print(f'Carga restante de {self.unidade.local} devolvida.')
                print(f'''
Estoque de {self.unidade.local}: {len(self.unidade.itens)}
Estoque de {destino.local}: {len(destino.itens)}''')
            else: print(f'Transferência não suportada: Não há itens no estoque de {self.unidade.local}!')
        else: print(f'Operação não suportada: Estoque de {destino.local} cheio!')
        sleep(1)

    def devolver_itens(self, devolucao):
        if len(self.unidade.estado.itens) < self.unidade.estado.estoque:
            for item in devolucao:
                    self.unidade.itens.remove(item)
                    item.values() == True
                    self.unidade.estado.itens.append(item)
                    if len(self.unidade.itens) == 0:
                        print(f'{self.unidade.local} sem mais itens para devolução.')
                        break
                    elif len(self.unidade.estado.itens) == self.unidade.estado.estoque:
                        print(f'Estoque de {self.estado.local} totalmente abastecido.')
                        break
            print(f'''Mercadorias devolvidas:
>>> {self.unidade.local} >>> {self.unidade.estado.local}''')
            if len(self.carga) > 0:
                print(self.carga)
                self.unidade.itens.extend(self.carga)
                self.carga = []
                print(f'Carga restante para devolução de {self.unidade.local} devolvida.')
            print(f'''
Estoque de {self.unidade.local}: {len(self.unidade.itens)}
Estoque de {self.unidade.estado.local}: {len(self.unidade.estado.itens)}''')
        else: print(f'Operação não suportada: Estoque de {self.unidade.estado.local} cheio!')
        sleep(1)


class Van():
    def __init__(self, centro, estoque=300):
        self.centro = centro
        self.estoque = estoque
        self.entrega = []
        self.devolver = []
    
    def fazer_entrega(self):
        from random import choice, randint
        for _ in range(randint(self.estoque - self.estoque // 5, self.estoque)):
            item = choice(self.centro.itens)
            self.entrega.append(item)
            self.centro.itens.remove(item)
            if len(self.centro.itens) == 0:
                break
        entregue = devolvido = 0
        tentativas = len(self.entrega)
        for _ in range(len(self.entrega)):
            endereco = Endereço(self.centro.bairro, self.centro.estado)
            chance = randint(1, 10)
            if chance == 1:
                self.entrega[0].values() == False
                self.devolver.append(self.entrega[0])
                self.entrega.pop(0)
                devolvido += 1
            else:
                self.entrega.pop(0)
                entregue += 1
        print(f'''\033[36mENTREGA EM DOMICÍLIOS\033[m

{tentativas} tentativas de entrega em:
{endereco.endereco}

Entregues: {entregue}
Devoluções: {devolvido}

=====================================''')
        sleep(1)
        if len(self.devolver) > 0:
            devolucao = self.devolver[:]
            self.devolver.clear()
            self.devolver_entrega(devolucao)
    
    def devolver_entrega(self, devolucao):
        if len(self.centro.itens) < self.centro.estoque:
            for item in devolucao:
                self.centro.itens.append(item)
                if len(self.centro.itens) == self.centro.estoque:
                    print(f'Estoque de {self.centro.local} totalmente abastecido.')
                    break
            print(f'''\033[36mDEVOLUÇÃO DE ITENS\033[m
''')
            self.centro.transporte.devolver_itens(devolucao)
        else: print(f'Operação não suportada: Estoque de {self.centro.local} cheio!')


class UnidadeDeTratamento():
    def __init__(self, estado):
        self.estado = estado
        self.local = f'\033[35mUT {estado}\033[m'
        self.estoque = 90000
        self.itens = estoque_ut[:]
        self.transporte = Caminhao(self)


class CentroDeDistribuicao():
    def __init__(self, bairro, estado):
        self.local = f'\033[33mCD {bairro}\033[m'
        self.bairro = bairro
        self.estado = estado
        self.estoque = 20000
        self.itens = estoque_cd[:]
        self.transporte = Caminhao(self)
        self.entrega = Van(self)


class Endereço():
    def __init__(self, bairro, estado):
        self.bairro = bairro
        self.estado = estado
        self.endereco = f'\033[32m{bairro} - {estado.estado}\033[m'
        self.recebimento = []
