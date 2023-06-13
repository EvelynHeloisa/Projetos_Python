print('='*30)
print('      MÉDIAS DO BIMESTRE')
print('='*30)

aluno = str(input('\nNome do aluno: ')).upper()
nota1 = float(input('1° Nota: '))
nota2 = float(input('2° Nota: '))
media = (nota1 + nota2) / 2

print('='*40)

if media < 5.0:
    print('\nALUNO(A): \033[34m{}\033[m FOI REPROVADO(A) \nMÉDIA: {:.2f}'.format(aluno, media))
elif media >= 5.0 and media < 6.9:
    print('\nALUNO(A) \033[34m{}\033[m ESTÁ EM RECUPERAÇÃO \nMÉDIA: {:.2f}'.format(aluno, media))
else:
    print('\nALUNO(A): \033[34m{}\033[m FOI APROVADO(A)!!! \nMÉDIA: {:.2f}'.format(aluno, media))

