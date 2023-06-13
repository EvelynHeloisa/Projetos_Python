def cal_area(c, l):
    area = c * l
    print(f'Área total: {area:.2f}m²')


print('='*30)
print('CALCULANDO TERRENOS')
print('='*30)

com = float(input('Digite o comprimento(m): '))
lar = float(input('Digite a largura(m): '))
cal_area(com, lar)

