'''
Código usado para gerar uma lista com determinada quantidade de itens pros objetos.
'''
itens = []
for _ in range(7000):
    itens.append({'item': True})

with open('gerador_de_itens/7000_itens.txt', 'a') as f:
    f.write(str(itens))