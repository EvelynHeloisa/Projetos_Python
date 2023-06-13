print('='*40)
print('      SENO, COSSENO E TANGENTE')
print('='*40)

import math
angle = float(input('\nInsira o ângulo do circúlo: '))
# Converter o angulo para radians
seno = math.sin(math.radians(angle))
cosseno = math.cos((math.radians(angle)))
tangente = math.tan((math.radians(angle)))
print('Dado o ângulo de {}° '
      '\n Seu seno é {:.2f} '
      '\n Seu cosseno é {:.2f} '
      '\n E sua tangente é {:.2f}'. format(angle, seno, cosseno, tangente))