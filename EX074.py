from random import randint

num_aleatorios = (randint(1, 10), randint(1, 10),
                  randint(1, 10), randint(1, 10),
                  randint(1, 10))
print(f'Numeros aleatórios: {num_aleatorios}')

print(f'Maior valor: {max(num_aleatorios)}')
print(f'Menor valor: {min(num_aleatorios)}')