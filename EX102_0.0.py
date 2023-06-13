def fatorial(n=1, show=False):
    f = 1
    if show:
        for c in range(n, 0, -1):
            f *= c
            #print(f'{f:<3} x {c:^3} = {c}')  HELP MEEEEE!!!!!!!!
    else:
        print(f'O fatorial de {n} é {f}')


print('='*30)
print('CALCULANDO FATORIAL')

num = int(input('Digite um número: '))
resp = ' '
show = False

while resp not in 'SN':
    resp = str(input('Deseja mostrar o cálculo? [S/N] ')).upper().strip()[0]
    if resp == 'S':
        show = True

fatorial(num, show)
