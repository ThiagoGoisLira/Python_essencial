#num = [2, 5, 9, 1]
#num[2] = 3 #modifica valor
#num.append(7)#adiciona valor
#num.sort()#poem numero em ordem
#num.sort(reverse=True)#poem em ordem inversa
#num.insert(2,2)#isere um valor
#num.pop(2)#Elimina o valor fina "1"
#num.remove(2)#Elimina o primeiro elemento 2
#print(num)
#print(f'Essa lista tem {len(num)} elementos.')

#valores = list()
#for cont in range(0, 5):
#    valores.append(int(input('Digite um valor: ')))

#for c , v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')

#print('FIM')

a = [2,3,4,7]
b = a[:]#Cria uma copia de a em b
b[2] = 8
print(f'Lista a:{a}')
print(f'Lista b:{b}')