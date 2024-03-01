filename = '5000_itens.txt'

all = []

with open(filename, 'r') as f:
    for line in f:
        all.append(line.strip())

with open('4000_itens.txt', 'a') as f:
    f.write(str(all[:3999]))