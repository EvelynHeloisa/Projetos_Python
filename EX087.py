matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_segCol = 0
maior = 0

for l in range(1, 4):
    for c in range(1, 4):
        matriz[l - 1][c - 1] = int(input(f'Valor para a posição [{l}][{c}]: '))
        if matriz[l-1][c-1] % 2 == 0:
            soma_pares += matriz[l-1][c-1]
print('='*40)

for n in range(0, 3):
    print(matriz[n])
    soma_segCol += matriz[n][2]

    maior = matriz[1][n]
    if matriz[1][n] > maior:
         maior = matriz[1][n+1]

print('='*40)
print(f'Soma de todos os valores pares: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_segCol}')
print(f'O maior valor da segunda coluna é {max(matriz[1])}')
print('='*40)
