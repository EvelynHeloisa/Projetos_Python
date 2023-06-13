print('='*60)
print('            CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('')
print('                  CATEGORIAS DE ATLETAS')
print('='*60)

print('Até 9 anos: MIRIM'
      '\nAté 14 anos: INFANTIL'
      '\nAté 19 anos: JÚNIOR'
      '\nAté 25 anos: SÊNIOR'
      '\nAcima de 25 anos: MASTER')
print('='*60)

from datetime import date
atleta = input('\nNome do atleta: ')
nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
print('='*60)
print('Atleta: {}\nIdade:{}'.format(atleta, idade))

if idade <= 9:
      print('Classificação: MIRIM')
elif idade <= 14:
      print('Classificação: INFANTIL')
elif idade <= 19:
      print('Classificação: JÚNIOR')
elif idade <= 25:
      print('Classificação: SÊNIOR')
elif idade > 25:
      print('Classificação: MASTER')
else:
      print('ATENÇÃO: Insira um ano válido.')