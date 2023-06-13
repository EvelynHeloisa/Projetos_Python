# Função

import math

def raizQuadrada(x):
    raiz = float(math.sqrt(x));
    print("A raiz quadrada de {} é {:.2f}".format(x, raiz))

valor = int(input("Digite um número: "))
raizQuadrada(valor)
print("fim...")
