print('='*40)
print('{:^40}'.format('PROGRESSÃO ARITIMÉTICA(PA)'))
print('='*40)

a1 = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão: '))
an = a1
tm = 1

print('\nOs 10 Primeiros Termos dessa PA são: ')
print(a1, end=' ')

while tm < 10:
    an += raz
    tm += 1
    print(an, end=' ')
