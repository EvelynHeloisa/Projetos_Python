
#def inicio():

tot_pol = totlin = totcol = 0

print('='*40)
print('{:^40}'.format('SWEET FLIGHT'))
print('='*40)

print('\n[1] Cadastrar o total de poltronas\n'
      '[2] Realizar reserva de poltronas\n'
      '[3] Visualizar poltronas disponíveis\n'
      '[4] Visualizar poltronas reservadas\n'
      '[5] Consultar passageiros pelo nome\n'
      '[6] Cancelar reserva\n'
      '[7] Relatório do Voo\n'
      '[8] Sair do sistema\n')

opcao = 0
while opcao <= 0 or opcao > 8:
    opcao = int(input('Escolha uma opção: '))

if opcao == 1:

    tamlin = 30
    tamcol = 10

    if tot_pol == 0:
        print('='*40)
        print('{:^40}'.format('CADASTRAR TOTAL DE POLTRONAS'))
        print('='*40)

        while True:
            totlin = int(input('\nInforme a quantidade de fileiras na aeronave: '))
            totcol = int(input('Informe a quantiade de poltronas em cada fileira: '))

            if totlin > tamlin or totcol > tamcol:
                print('\nAtenção! Número máximo de fileiras é [30]\n'
                      'Número máximo de poltronas por fileira é [10].')
            else:
                break

        tot_pol = totcol * totlin

        print(f'\nAeronave cadastrada com total de {tot_pol} poltronas...')

        # voltar para o menu iniciar

    else:
        print('Poltronas já cadastradas.')

        # Voltar para o ínicio

if opcao == 2:

    passageiros = {}
    print('='*40)
    print('{:^40}'.format('RESERVA DE POLTRONAS'))
    print('='*40)

    while True:
        while True:
            lin = int(input('Informe a fileira: '))
            col = int(input('Inforem a poltrona: '))

            if lin > totlin or col > totcol:
                print('Atenção! Fileira ou coluna não existente! ')
            else:
                break

        passageiros['nome'][lin][col] = str(input('Nome do passageiro: ')).upper().strip()
        passageiros['sexo'][lin][col] = str(input('Sexo: ')).upper().strip()[0]
        passageiros['idade'][lin][col] = int(input('Idade: '))

        print('Poltrona reserva com sucesso!')

        opc = ' '
        while opc not in 'NS':
            opc = str(input('Gostaria de cadastrar outro passageiro? [S/N]')).upper().strip()[0]
        if opc == 'N':
            break








