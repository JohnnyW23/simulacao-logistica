filename = '50000lines_itens.txt'
itens = []
with open(filename) as f:
    for linha in f:
        itens.append(linha.strip())

with open('10000_itens.txt', 'a') as f:
    f.write(str(itens[:10000]))