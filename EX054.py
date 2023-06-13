print('============= MAIORIDADE (21 anos) =============\n')

ano = {}
idade = {}
from datetime import date
ano_atual = date.today().year
pessoa = 0
maior = 0
menor = 0

for pessoa in range(0, 7):
    ano[pessoa] = int(input('{}/7 Digite o ano de nascimento: '.format(pessoa)))
    idade = ano_atual - ano[pessoa]

    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('-'*30)
print('Existem {} maiores de 21 anos.'.format(maior))
print('Existem {} menores de 21 anos.'.format(menor))
