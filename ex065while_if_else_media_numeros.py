#Medias entre os numeros
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma / quant
print('Você digitou {}, ea media e:{}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('FIM')