from time import sleep


def contar(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contando de {i} até {f} de {p} em {p}')
    if i > f:
        p = -p
    for num in range(i, f, p):
        print(num, end=' ')
        sleep(0.5)
    print(f, end=' ')
    print('FIM!')
    print('=' * 40)


contar(1, 10, 1)
contar(10, 0, 2)

print('Agora é sua vez!')
while True:
    ini = int(input('INÍCIO: '))
    fim = int(input('FIM: '))
    pas = int(input('PASSO: '))
    contar(ini, fim, pas)

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? ')).upper().strip()[0]
    if opc == 'N':
        break
