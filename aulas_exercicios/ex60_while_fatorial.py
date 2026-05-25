#Calcule o fatorial de um numero
from math import factorial
n = int(input('Digite um numero para calcular o seu factorial: '))
c = n
f = 1
print('Calculando {}: '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
#f = factorial(n)
#print('O fatorial de {} e {}.'.format(n,f))