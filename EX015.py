# Sorteando numeros aleatórios

alunos = ["Ana", "Beto", "Carla", "Daniel"]

import random
print("Usando random.randint:")
sorteado = random.randint(0,3)
print("O aluno sorteado foi: {}".format(alunos[sorteado]))

# OUTRA FORMA

print("\nUsando random.choice:")
sorteado = random.choice(alunos)
print("O aluno sorteado foi: {}".format(sorteado))
