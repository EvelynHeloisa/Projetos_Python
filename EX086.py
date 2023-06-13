matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(1, 4):
    for c in range(1, 4):
        matriz[l - 1][c - 1] = int(input(f'Valor para a posição [{l}][{c}]: '))

print('='*25)
for n in range(0, 3):
    print(matriz[n])

