x =int(input("Digite um numero inteiro: "))
y = int(input("Digite outro numero inteiro: "))
z = int(input("Digite outro numero inteiro: "))

if x > y and x > z:
    print('Maior numero', x)
if y > x and y > z:
    print('Maior numero', y)
if z > x and z > y:
    print('Maior numero', z)
if x == y or x == z or y == z:
    print('Alguns numero são iguais')
