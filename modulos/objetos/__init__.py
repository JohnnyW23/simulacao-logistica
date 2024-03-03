from modulos.classes import (UnidadeDeTratamento,
                             CentroDeDistribuicao,
                             Caminhao,
                             Van)

riodejaneiro = UnidadeDeTratamento('Rio de Janeiro')
rj = riodejaneiro

copacabana = CentroDeDistribuicao('Copacabana', rj)
ipanema = CentroDeDistribuicao('Ipanema', rj)
lapa = CentroDeDistribuicao('Lapa', rj)
botafogo = CentroDeDistribuicao('Botafogo', rj)

saopaulo = UnidadeDeTratamento('São Paulo')
sp = saopaulo

osasco = CentroDeDistribuicao('Osasco', sp)
saojosedoscampos = CentroDeDistribuicao('São José dos Campos', sp)
taubate = CentroDeDistribuicao('Taubaté', sp)
alphaville = CentroDeDistribuicao('Alphaville', sp)

minasgerais = UnidadeDeTratamento('Minas Gerais')
mg = minasgerais

belohorizonte = CentroDeDistribuicao('Belo Horizonte', mg)
uberlandia = CentroDeDistribuicao('Uberlândia', mg)
contagem = CentroDeDistribuicao('Contagem', mg)
juizdefora = CentroDeDistribuicao('Juiz de Fora', mg)

espiritosanto = UnidadeDeTratamento('Espírito Santo')
es = espiritosanto

vitoria = CentroDeDistribuicao('Vitória', es)
vilavelha = CentroDeDistribuicao('Vila Velha', es)
cariacica = CentroDeDistribuicao('Cariacica', es)
serra = CentroDeDistribuicao('Serra', es)

Rj = {riodejaneiro: 
        [copacabana, ipanema, lapa, botafogo]
    }

Sp = {saopaulo:
        [osasco, saojosedoscampos, taubate, alphaville]
    }

Mg = {minasgerais:
        [belohorizonte, uberlandia, contagem, juizdefora]
    }

Es = {espiritosanto:
        [vitoria, vilavelha, cariacica, serra]
    }

estados = [Rj, Sp, Mg, Es]

dias = ['SEGUNDA-FEIRA',
        'TERÇA-FEIRA',
        'QUARTA-FEIRA',
        'QUINTA-FEIRA',
        'SEXTA-FEIRA',
        'SÁBADO']

caminhao = Caminhao()
van = Van()
