# Tuplas são imutáveis
sobremesas = ('Pudim', 'Bolo', 'Pizza', 'Sorvete') # não precisa colocar ()
#print(sobremesas[0])

#for c in sobremesas:
#    print(f'Eu vou comer {c}')

#for c in range(0, len(sobremesas)):
#    print(f'Doces disponíveis: {sobremesas[c]}')

#for pos, c in enumerate(sobremesas):
#    print(f'Eu vou comer {c} {pos}')

#print(sorted(sobremesas)) # Ordenado

idadesA = (12, 34, 52, 29)
idadesB = (18, 25, 46, 37)
idadesC = idadesA + idadesB
print(idadesC)
print((idadesC.count(12))) #Quantas vezes aquele elemento aparece na tupla

print(idadesB.index(46)) # Em que posição está aquele elemento

pessoa = ('Evelyn', 21, 'F', 1.56)
del(pessoa) # Apagar a tupla