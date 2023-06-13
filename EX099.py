def maior(lis):
    print(f'Números: {lis}')
    maior = aux = 0
    for c in range(0, len(lis)):
        for i in range(0, len(lis)):
            if lis[c] < lis[i]:
                aux = lis[c]
                lis[c] = lis[i]
                lis[i] = aux

    maior = lis[len(lis)-1]
    print(f'Maior número: {maior}'
          f'\nTamanho da lista: {len(lis)} elementos')
    print('='*30)


list1 = [1, 4, 7, 3]
list2 = [2, 93, 56]
list3 = [82, 52, 72, 2, 6]
list4 = [5, 2]


maior(list1)
maior(list2)
maior(list3)
maior(list4)
