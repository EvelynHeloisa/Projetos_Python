print('ORDEM DE APRESENTAÇÃO DE TRABALHOS')

alunos = ['Ana', 'Beto', 'Carla', 'Daniel', 'Emily']
n = 1
print("\n COM O COMANDO [FOR]: ")
from random import shuffle
shuffle(alunos)
for item in alunos:
    print('{}° {}'.format(n, item))
    n = n+1

# OUTRA OPÇÃO
shuffle(alunos)
print('\n\n SEM O COMANDO [FOR]:'
      '\n A ordem será:')
print(alunos)