print('='*40)
print('\033[34m      CONVERSOR DE BASES NUMÉRICAS\033[m')
print('='*40)

num = int(input('Digite um número inteiro: '))
print('')
print('\033[34m=\033[m'*40)
print('Escolha uma opção para a conversão: \n')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Conveter para HEXADECIMAL')
print('\033[34m=\033[m'*40)


opcao = int(input("Digite a opção escolhida: "))

if opcao == 1:
   binary = bin(num)
   print('\033[34m=\033[m' * 40)
   print('NÚMERO EM DECIMAL: {} \nNÚMERO BINÁRIO: {}'.format(num, binary[2:]))
elif opcao == 2:
    octal = oct(num)
    print('\033[34m=\033[m' * 40)
    print('NÚMERO EM DECiMAL: {} \nOCTAL: {}'.format(num, octal[2:]))
elif opcao == 3:
    hexa = hex(num)
    print('\033[34m=\033[m' * 40)
    print('NÚMERO EM DECIMAL: {} \nHEXADECIMAL: {}'.format(num, hexa[2:]))
else:
    print("ESCOLHA UMA OPÇÃO VÁLIDA!")
