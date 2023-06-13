def voto(ano_nas):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nas
    print(f'Sua idade: {idade} anos | Voto:', end=' ')
    if idade < 16:
        print('NEGADO')
    elif 16 <= idade < 18 or idade > 65:
        print('OPCIONAL')
    else:
        print('OBRIGATÓRIO')


print('='*40)
ano = int(input('Digite seu ano de nascimento: '))
voto(ano)
