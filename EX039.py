print('='*60)
print('                    ALISTAMENTO MILITAR')
print('='*60)

nome = input('Infome o seu nome completo: ').title()
ano_nasc = int(input('Informe seu ano de nascimento: '))
genero = input('Digite [M] para Masculino ou [F] para feminino: ').upper()[0:1]
print('='*60)

if genero == "F":
    nome = nome.split()
    print('{}, você não precisa fazer o alistamento militar obrigatório.'.format(nome[0]))
else:
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    print('NOME:', nome)

    if idade == 18:
        print('IDADE: {} anos \nVocê deve se alistar esse ano!'.format(idade))
    elif idade > 18:
        if idade - 18 == 1:
            print('IDADE: {}\nSeu alistamento foi ano passado({}).'.format(idade, ano_atual - 1))
        else:
            print('IDADE: {} anos \nJá passou {} anos do seu prazo de alistamento.'
                  '\nSeu alistamento foi em {}'.format(idade, idade - 18, ano_nasc + 18 ))
    elif idade < 18:
        if 18 - idade == 1:
            print('IDADE: {}\nSeu alistamento será ano que vem! Em {}'.format(idade, ano_atual + 1))
        else:
            print('IDADE: {} anos\nAinda falta {} anos  para você se alistar. '
                  '\nSerá em {}'.format(idade, 18 - idade, ano_nasc + 18))
    else:
        print('ATENÇÃO: Insira um ano válido.')