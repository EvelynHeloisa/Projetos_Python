from datetime import date
print('='*40)
print('{:^40}'.format('CADASTRO DE TRBALHADOR'))
print('='*40)

cadastro = dict()

cadastro['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
cadastro['Idade'] = date.today().year - ano_nasc
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano Contratação'] = int(input('Ano de Contrtação: '))
    cadastro['Salário'] = float(input('Salário R$ '))
    ano_aposent = cadastro['Ano Contratação'] + 35
    cadastro['Aposentadoria'] = ano_aposent - ano_nasc

print('='*40)
for k, v in cadastro.items():
    print(f'{k}: {v}')
