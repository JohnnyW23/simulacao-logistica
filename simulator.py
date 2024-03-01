from log import UnidadeDeTratamento, CentroDeDistribuicao, Caminhao
from time import sleep
from random import choice

rj = UnidadeDeTratamento('Rio de Janeiro')
sp = CentroDeDistribuicao('São Paulo')
mg = CentroDeDistribuicao('Minas Gerais')
es = CentroDeDistribuicao('Espírito Santo')
caminhao = Caminhao()

print('=====================================')
while True:
    agentes = [sp, mg, es]
    
    agente1 = choice(agentes)
    agentes.remove(agente1)
    agente2 = choice(agentes)
    caminhao.transferir_item(agente1, agente2)
    print(agente1.itens)

    sleep(3)
