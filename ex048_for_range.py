#Faça um programa que calcule a soma entre todos os numeros  impares que sao multiplos de 3 e
#que se encontram no intervalor de 1 ate 500
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        #print(c)
        soma += c
        contador += 1
print('Soma de todos os numeros e: {}, total de {} repetições'.format(soma,contador))