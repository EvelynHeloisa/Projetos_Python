aluno = {}

aluno['Nome'] = str(input('Nome do aluno: ')).title().strip()
aluno['Média'] = float(input('Média: '))

if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado(a)'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Em recuperação'
else:
    aluno['Situação'] = 'Reprovado(a)'

print('-'*30)
for k, v in aluno.items():
    print(f'{k}: {v}')
