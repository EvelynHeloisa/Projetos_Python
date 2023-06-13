print('='*40)
print('{:^40}'.format('SISTEMA DE CADASTRO'))
print('='*40)

nome = {}
sexo = {}
idade = {}
soma = 0
temp = 0
homem = {}
tem_nome = ''

for c in range(1, 6):
    print('\nCadastro {}/5'.format(c))
    nome[c] = input('NOME: ').title().strip()
    idade[c] = int(input('IDADE: '))
    sexo[c] = input('SEXO [M] OU [F]: ').upper()
    soma += idade[c]
    print('='*30)

media = soma / 5
print('A média de idade é {}'.format(media))

id_hom = {}
pont = 0
for c in range(1, 6):
    if sexo[c] == 'M':
        id_hom[pont] = idade[c]
        homem[pont] = nome[c]
        pont += 1


for i in range(0, len(id_hom)):
    for n in range(0, len(id_hom)):
        if id_hom[i] < id_hom[n]:
            temp = id_hom[i]
            id_hom[i] = id_hom[n]
            id_hom[n] = temp

            tem_nome = homem[i]
            homem[i] = homem[n]
            homem[n] = tem_nome


print('O homem mais velho se chama {} e tem {} anos.'.format(homem[len(homem)-1], id_hom[len(id_hom)-1]))

cont = 0

for a in range(1, 6):
    if sexo[a] == 'F':
        if idade[a] < 20:
          cont += 1

print('Existem {} mulheres menores de 20 anos.'.format(cont))
