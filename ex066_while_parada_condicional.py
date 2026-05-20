#Crie um programa que leia varios numeros inteiros, o programa so para quando o usuario disgitar 999
#no final mostre quantos numeros foram digitados ea soma entre eles. (desconsidere o 999)
soma = 0
contador = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'A soma entre os valores e {soma}, foram digitados {contador} numeros')