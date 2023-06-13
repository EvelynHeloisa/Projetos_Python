
# Pintando uma parede, considerando que a cada 2m² usa-se 1 litro de tinta

altura = float(input("Altura da parede(m): "))
largura = float(input("Largura da parede(m): "))

area = altura*largura
print("A área a ser pintada é de {:.2f}m²".format(area))

tinta = area/2
print("Será usado {:.2f} litros de tinta".format(tinta))
