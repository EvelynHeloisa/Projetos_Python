n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
med = (n1+n2)/2
print("A média é {:.2f}".format(med))

if med == 10:
    print("Aprovado com Distinção!")

elif med >= 7:
    print("Aprovado")

else:
    print("Reprovado!")

