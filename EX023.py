nome = str(input('Digite seu nome nome completo: ')).strip().title()
print('Prazer em conhecê-lo(a) {} !'.format(nome))
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n)-1]))



