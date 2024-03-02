from objetos import *
from random import choice
from time import sleep

while True:
    try:
        rounds = int(input('Defina o número de rounds para simulação: '))
        break
    except ValueError:
        print('Valor inválido! Digite um número inteiro')
        continue

print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
for _ in range(rounds):
    estado = choice(estados)
    agente1 = list(estado.keys())[0]
    agente2 = choice(estado[agente1])
    agente1.transporte.enviar_itens(agente2)
    print('''
=====================================''')
    agente2.entrega.fazer_entrega()


    sleep(3)

print('FIM DA SIMULAÇÃO.')
