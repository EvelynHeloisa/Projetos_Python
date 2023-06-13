from time import sleep


def maior (*num):
   cont = maior = 0
   for n in num:
       print(f'{n}', end=' ', flush=True)
       sleep(0.5)
       if cont == 0:
            maior = n
       else:
           if n > maior:
               maior =  n
       cont += 1
   print(f'\nValores informados {cont} ao todo.'
        f'\nO maior é {maior}')
   print('-'*30)


maior(8, 34, 81, 2, 90)
maior(12, 16, 26, 72)
maior(9, 3)
maior(90)
maior()