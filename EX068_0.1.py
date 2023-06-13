print('='*40)
print('{:^40}'.format("JOGO PAR OU ÍMPAR"))

usu = vitorias = tot = comp = 0

from random import randint

while True:
    print('='*40)
    usu = int(input('Digite um número: '))
    comp = randint(0, 10)
    tot = usu + comp
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]

    print('='*40)
    print(f'Seu jogo: {usu} \nJogo computador: {comp} \nTotal: {tot}', end=' ')
    print('PAR' if tot % 2 == 0 else 'ÍMPAR')
    print('='*40)

    if par_impar == "P":
        if tot % 2 == 0:
            print('VOCÊ GANHOU!')
            vitorias += 1
        else:
            print('GAME OVER!!')
            break
    else:
        if tot % 2 != 0:
            print('VOCÊ GANHOU!')
            vitorias += 1
        else:
            print('GAME OVER!!')
            break

print(f'Total de vitórias: {vitorias}')

