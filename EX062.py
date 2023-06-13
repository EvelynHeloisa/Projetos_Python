print('='*40)
print('{:^40}'.format('PROGRESSÃO ARITIMÉTICA(PA)'))
print('='*40)

a1 = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão: '))
an = a1
tm = 1
tmu = 0
mais = 10

print('\nOs 10 Primeiros Termos dessa PA são: \n')

while mais != 0:
    tmu += mais
    while tm <= tmu:
        print(an, " ", end="")
        an += raz
        tm += 1
    mais = int(input("\nDeseja mostrar mais quantos termos: "))
print('='*40)
print('Progressão encerrada com {} termos'.format(tmu))



