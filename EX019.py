# LER UM NUMERO DE 0 A 9999 E MOSTRE CADA UM DOS DIGITOS SEPARADOS
# (UNIDADE, DEZENA, CENTENA  E MILHAR)

print("="*40)
numero = int(input("Digite um número de 0 a 9999: "))
print("="*40)

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Unidade:", u)
print("Dezena:", d)
print("Cenetena:", c)
print("Milhar:", m)



