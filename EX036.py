print('='*30)
print('\033[35m     EMPRÉSTIMO BANCÁRIO \033[m')
print('='*30)

valor = float(input('Digite o valor da imóvel R$ '))
sal = float(input('Informe seu salário atual R$ '))
meses = int(input('Informe em quantos anos deseja parcelar: ')) * 12
parcelas = valor / meses

if parcelas > (sal * 30/100):
    print('\033[35m=\033[m' * 40)
    print('\033[31m           EMPRÉSTIMO NEGADO\033[m\n')
    print('Valor do empréstimo R$ {:.2f}'.format(valor))
    print('Quantidade de parcelas: {}'.format(meses))
    print('Valor das parcelas R$ {:.2f}'.format(parcelas))
    print('\033[35m=\033[m' * 40)
else:
    print('\033[35m=\033[m' * 40)
    print('\033[32m         EMPRÉSTIMO APROVADO!\033[m\n')
    print('Valor do empréstimo R$ {:.2f}'.format(valor))
    print('Quantidade de parcelas: {}'.format(meses))
    print('Valor das parcelas R$ {:.2f}'.format(parcelas))
    print('\033[35m=\033[m' * 40)

