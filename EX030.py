print('='*40)
print('        CALCULANDO A AUMENTO')
print('='*40)

sal = float(input('\nInsira o seu salário atual R$ '))

if sal > 1250:
    aumento = (sal*10/100) + sal
    print('Após um aumento de 10%, seu salário será R$ {:.2f}'.format(aumento))
else:
    aumento = (sal*15/100) + sal
    print('Após um aumento de 15%, seu salário será R$ {:.2f}'.format(aumento))
