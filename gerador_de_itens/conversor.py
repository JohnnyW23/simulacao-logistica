filename = 'gerador_de_itens/50000lines_itens.txt'
itens = []
with open(filename) as f:
    for linha in f:
        itens.append({'item': True})

with open('gerador_de_itens/40000_itens.txt', 'a') as f:
    f.write(str(itens[:40000]))