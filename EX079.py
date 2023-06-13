num = list()
while True:
    num_usu = int(input('Digite um valor: '))
    if num_usu not in num:
        num.append(num_usu)
    else:
        print('Valor duplicado! Não add..')
    print('='*30)

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break

num.sort()
print('='*40)
print(f'Esses são os números digitados em ordem crescente: {num}')
