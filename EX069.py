print('='*40)
print('{:^40}'.format('CADASTRO DE PESSOAS'))

cont_18 = cont_M = cont_F20 = 0

while True:
    sexo = ' '
    opcao = ' '
    print('=' * 40)
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        cont_18 += 1

    while sexo not in 'FM':
        sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()[0]
        if sexo == 'M':
           cont_M += 1

        else:
            if idade < 20:
                cont_F20 += 1

    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break


print('='*40)
print('{:^40}'.format('RELATÓRIO FINAL\n'))

print(f'Pessoas com mais de 18 anos: {cont_18}')
print(f'Total de homens cadastrados: {cont_M}')
print(f'Mulheres com menos de 20 anos: {cont_F20}')
