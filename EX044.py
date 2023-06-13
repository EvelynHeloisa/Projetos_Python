# Minha versão - PRECISA SER MELHORADA

print('\033[35m=\033[m'*60)
print('{:^60}'.format('GERENCIAMENTO DE PAGAMENTOS'))
print('\033[35m=\033[m'*60)

produto = float(input('         |       VALOR DA COMPRA R$ '))
print('\n         |       SELECIONE O MÉTODO DE PAGAMENTO:'
      '\n         |       [1] A VISTA NO DINHEIRO/PIX 10% DESCONTO'
      '\n         |       [2] CARTÃO DE DÉBITO 5% DESCONTO'
      '\n         |       [3] CARTÃO DE CRÉDITO (Até 12 vezes)')
escolha = int(input('\n         OPÇÃO ESCOLHIDA: '))

desconto = produto - (produto * 0 / 100)
juros = produto + (produto * 0 /100)
if escolha == 1:
      desconto = produto - (produto * 10 / 100)
      print('\n         |       PREÇO ORIGINAL R$ {}'
            '\n         |       PREÇO APÓS DESCONTO de 10%:  R$ {:.2f}'.format(produto, desconto))
elif escolha == 2:
      desconto = produto - (produto * 5 / 100)
      print('\n         |       PREÇO ORIGINAL R$ {}'
            '\n         |       PREÇO APÓS DESCONTO de 5%: R$ {:.2f}'.format(produto, desconto))
elif escolha == 3:
      parcelas = int(input('\n         |       QUANTAS VEZES DESEJA PARCELAR? '))
      if parcelas == 1:
            juros = produto + (produto * 5 / 100)
      elif parcelas == 2:
            juros = produto + (produto * 0 /100)
      elif parcelas >= 3:
            juros = produto + (produto * 20 / 100)
      print('\n         |       PREÇO ORIGINAL R$ {}'
            '\n         |       PREÇO FINAL: {:.2f}'
            '\n         |       PARCELAS: {}'
            '\n         |       VALOR DE CADA PARECLA R$ {:.2f}'.format(produto, juros, parcelas, (juros/parcelas)))
else:
      print('\n         |       ATENÇÃO: Escolha uma opção válida.')


