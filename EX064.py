print('='*40)
print('{:^40}'.format('DESCUBRA A REGRA DO JOGO!'))
print('='*40)

n = int(input('Digite um número aleatório: '))
soma = totn = 0

while n != 999:
    soma += n
    totn += 1
    n = int(input('Ainda não! tente novamente: '))

print('='*40)
print('             PARABÉNS!')
print('Números digitados : {}'.format(totn))
print('Soma dos números digitados : {}'.format(soma))
