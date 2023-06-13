from time import sleep
import emoji

print('\033[32m=\033[m'*50)
print('{:^50}'.format('{} CONTAGEM FOGOS DE ARTIFÍCIOS!!{}'.format('\033[35m', '\033[m')))
print('\033[32m=\033[m'*50)

enter = input('{:^50}'.format('Aperte [ENTER] para começar...'))

if enter == "":
    for seg in range(10, -1, -1):
        print('{:^50}'.format(seg, "!"))
        sleep(1)

print('\n{:^50}'.format('\033[7;33m !!!  !!! !!!  BUUUUM   !!! !!! !!!\033[m'))

for c in range(0, 23):
    print(emoji.emojize(':boom:', language='alias'), end="")

