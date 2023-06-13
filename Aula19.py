pessoas = {'nome': 'Evelyn', 'sexo': 'F', 'idade': 21}

print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())

passageiro = dict()
aeronave = list()

for c in range(0, 3):
    passageiro['Nome'] = str(input('Nome do Passageiro: ')).strip().title()
    passageiro['Sexo'] = ' '
    while passageiro['Sexo'] not in 'FM':
        passageiro['Sexo'] = str(input('Sexo: ')).upper().strip()[0]

    passageiro['Idade'] = int(input('Idade: '))
    aeronave.append(passageiro.copy())
    print('-'*20)

for pol in aeronave:
    for k, v in pol.items():
        print(f'{k}: {v}')
    print('-'*20)
