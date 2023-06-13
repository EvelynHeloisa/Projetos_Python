print('='*40)
print('{:^40}'.format('CALCULADORA CONVERSÃO'))
print('{:^40}'.format('WONS COREANOS PARA REAIS'))
print('='*40)

won = float(input('Digite o valor em WON: '))
dolar = float(input('Digite o dolar hoje: '))
reais = won * dolar
print('Valor em R$ {:.2f}'.format(reais))