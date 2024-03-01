from ut_estoque import estoque_ut
from cd_estoque import estoque_cd
itens_cd = []
itens_ut = []
for item in estoque_cd:
    itens_cd.append({item: True})
for item in estoque_ut:
    itens_ut.append({item: True})
estoque_ut = itens_ut
estoque_cd = itens_cd

class Caminhao():
    def __init__(self, estoque=50):
        self.estoque = estoque
        self.carga = []

    def transferir_item(self, remetente, destino):
        from random import choice
        if len(destino.itens) < destino.estoque:
            if len(remetente.itens) > 0:
                for _ in range(self.estoque):
                    item = choice(remetente.itens)
                    self.carga.append(item)
                    remetente.itens.remove(item)
                    if len(remetente.itens) == 0:
                        print(f'{remetente.local} sem mais itens restantes.')
                        break
                for _ in range(len(self.carga)):
                    destino.itens.append(self.carga[0])
                    self.carga.pop(0)
                    if len(destino.itens) == destino.estoque:
                        print(f'Estoque de {destino.local} totalmente abastecido.')
                        break
                print(f'Mercadorias transferidas de estoque em\n{remetente.local} para estoque em {destino.local}.')
                if len(self.carga) > 0:
                    print(self.carga)
                    remetente.itens.extend(self.carga)
                    self.carga = []
                    print(f'Carga restante de {remetente.local} devolvida.')
                print(f'''
Estoque de {remetente.local}: {len(remetente.itens)}
Estoque de {destino.local}: {len(destino.itens)}''')
            else: print(f'Transferência não suportada: Não há itens no estoque de {remetente.local}!')
        else: print(f'Operação não suportada: Estoque de {destino.local} cheio!')
        print('=====================================')


class Van():
    def __init__(self, estoque=10):
        self.estoque = estoque
        self.carga = []


class UnidadeDeTratamento():
    def __init__(self, local):
        self.local = f'\033[35m{local}\033[m'
        self.estoque = 5000
        self.itens = estoque_ut[:]
        self.transporte = Caminhao()


class CentroDeDistribuicao():
    def __init__(self, local):
        self.local = f'\033[33m{local}\033[m'
        self.estoque = 500
        self.itens = estoque_cd[:]


class Residencia():
    def __init__(self, bairro, estado):
        self.bairro = bairro
        self.estado = estado
        self.endereco = f'{bairro} - {estado}'
    