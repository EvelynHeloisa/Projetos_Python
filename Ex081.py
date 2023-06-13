numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
numeros.sort(reverse=True)
print('='*30)
print(f'Você digitou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não faz parte da lista.')
