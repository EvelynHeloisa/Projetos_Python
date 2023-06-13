print('='*40)
print('{:^40}'.format('CALCULADORA'))
print('='*40)

v1 = int(input('PRIMEIRO VALOR: '))
v2 = int(input('SEGINDO VALOR: '))
opcao = 0

from time import sleep

while opcao != 5:
      print('=' * 40)
      print('\n{:^40}'.format('ESCOLHA UMA OPÇÃO'))
      print('\n[1] SOMAR'
            '\n[2] MULTIPLICAR'
            '\n[3] MAIOR'
            '\n[4] NOVOS NÚMEROS'
            '\n[5] SAIR')

      opcao = int(input('\nDigite opção: '))
      print('=' * 40)

      if opcao == 1:
            soma = v1 + v2
            print('='*40)
            print('{:^40}'.format('SOMA'))
            print('\nA soma de {} mais {} é {}'.format(v1, v2, soma))

      elif opcao == 2:
            multi = v1 * v2
            print('{:^40}'.format('MULTIPLICAÇÃO'))
            print('\nA multiplicação de {} com {} é {}'.format(v1, v2, multi))

      elif opcao == 3:
            maior = 0
            if v1 > v2:
                  maior = v1
            else:
                  maior = v2
            print('\n{:^40}'.format('O maior valor é {}'.format(maior)))

      elif opcao == 4:
            print('{:^40}'.format('NOVOS NÚMEROS'))
            v1 = int(input('\nPRIMEIRO VALOR: '))
            v2 = int(input('SEGUNDO VALOR: '))
      elif opcao == 5:
            print('Saindo do programa', end='')
            sleep(1)
            print('.', end='')
            sleep(1)
            print('.', end='')
            sleep(1)
            print('.')
            print('\n================= FIM ==================')

      else:
            print('   Opção inválida! Tente novamente.')

