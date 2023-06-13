num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))

if num.count(9) == 0:
    print('O número 9 não foi foi digitado nenhuma vez')
else:
    print(f'O número 9 apareceu {num.count(9)} vezes')

if 3 in num:
     print(f'O número 3 apareceu na {pos+1}° posição')
else:
    print(f'O número 3 não foi digitado')

for n in num:
    if num[n] % 2 == 0:
       print(f'Números pares digitados: {num[n]}')
else:
    print('Não foram digitados números pares.')

