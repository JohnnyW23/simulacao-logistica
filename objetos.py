from log import UnidadeDeTratamento, CentroDeDistribuicao

riodejaneiro = UnidadeDeTratamento('Rio de Janeiro')
rj = riodejaneiro

santacruz = CentroDeDistribuicao('Santa Cruz', rj)
campogrande = CentroDeDistribuicao('Campo Grande', rj)
bangu = CentroDeDistribuicao('Bangu', rj)
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
        [santacruz, campogrande, bangu, botafogo]
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
