num_orden = []

for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > num_orden[-1]:
        num_orden.append(num)
    else:
        pos = 0
        while pos < len(num_orden):
            if num <= num_orden[pos]:
                num_orden.insert(pos, num)
                break
            pos += 1
print('='*30)
print(f'Lista ordenada sem o comando sort(): {num_orden}')
