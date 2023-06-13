print('='*45)
print('{:^45}'.format('BOLETIM ALUNOS 2023'))
print('='*45)

notas = []
aux = []
media = 0

while True:
    aux.append(str(input('Nome do aluno: ')))
    aux.append(float(input('1° Nota: ')))
    aux.append(float(input('2° Nota: ')))
    media = (aux[1] + aux[2]) / 2
    aux.append(media)
    notas.append(aux[:])
    aux.clear()

    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

print('='*45)
print(f'{"Cód.":<4} {"NOME":>6}{"MÉDIA":>12}')
for i in range(0, len(notas)):
    print(f'{i:<4}{notas[i][0]:>8}{notas[i][3]:12.2f}')

aluno = 0
while aluno != 999:
    print('=' * 45)
    aluno = int(input('Mostrar nota de qual aluno: (999 interrompe)'))

    for i in range(0, len(notas)):
        if aluno == i:
            print(f'Notas de {notas[i][0]} são: {notas[i][1:3]}\n')
