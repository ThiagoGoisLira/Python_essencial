numeros =  list ()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado')
    response = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if response in 'Nn':
        break
numeros.sort()#Ordena numeros
print(numeros)