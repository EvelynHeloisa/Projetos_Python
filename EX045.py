print('\033[34m=\033[m'*40)
print('{:^40}'.format('PEDRA, PAPEL, TESOURA'))
print('\033[34m=\033[m'*40)

print('          FAÇA SUA JOGADA:'
      '\n           [1] PEDRA'
      '\n           [2] PAPEL'
      '\n           [3] TESOURA')

usu = int(input('\n          ESCOLHA: '))
if usu > 3:
      print('          Opção inválida!')
else:

      opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

      from random import randint

      comp = randint(1, 3)
      print('\033[34m=\033[m' * 40)
      print('\n          Sua jogada: {}'
            '\n          Jogada do computador: {}'.format(opcoes[usu-1], opcoes[comp-1]))

      if usu == 1 and comp == 3 or usu == 3 and comp == 2 or usu == 2 and comp == 1:
            print('\n          \033[7;32mVocê ganhou!!!!\033[m')
      elif comp == 1 and usu == 3 or comp == 3 and usu == 2 or comp == 2 and usu ==1:
             print('\n          \033[7;31mVocê perdeu...\033[m')
      else:
            print('\n          \033[33mEMPATOU!')
print('')
print('\033[34m=\033[m' * 40)