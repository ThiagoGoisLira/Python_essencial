#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão
n = int(input('Digite um numero para converter: '))
print('''Escolha uma das bases para converter:
[ 1 ] Converte para binario
[ 2 ] Converte para octal
[ 3 ] Converte para hexadecimal''')
opcao = int(input('Opção: '))

if opcao == 1:
    print('{} Converte para binario: {}'.format(n,bin(n)[2:]))
elif opcao == 2:
    print('{} Converte para octal: {}'.format(n,oct(n)[2:]))
elif opcao == 3:
    print('{} Converte para hexadecimal: {}'.format(n,hex(n)[2]))
else:
    print('Opcao invalida')