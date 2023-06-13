p_abre = p_fecha = 0

expre = str(input('Digite uma expressão: '))

for car in expre:
    if '(' in car:
        p_abre += 1
    elif ')' in car:
        p_fecha += 1

if p_abre != p_fecha:
    print('Sua expressão está errada!')
else:
    print('Sua expressão está válida!')
