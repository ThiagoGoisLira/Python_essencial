#listas compostas e analise de dados
principal = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])#Cria uma copiado do temporario
    temp.clear()#Apos armazera limpa a variavel temp
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar in 'Nn':
        break
print('-'*30)
print(f'Ao todo, voçê cadastrou: {len(principal)} pessoas.')
print(f'Os dados foram: {principal}')
print(f'O maior peso foi de: {maior} Kg. Peso de', end='')
for p in principal:
    if p[1] == maior:
        print(f' [{p[0]}]', end=' ')
print(f'O menor peso foi de: {menor} Kg. Peso de', end='')
for p in principal:
    if p[1] == menor:
        print(f' [{p[0]}] ', end='')
