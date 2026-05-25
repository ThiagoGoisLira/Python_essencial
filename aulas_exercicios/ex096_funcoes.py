def area(x,y):
    t = x * y
    return t

def imprimir (txt):
    print('-----' * 10)
    print(txt)
    print('-----'*10)

a = float(input('Comprimento: '))
b = float(input('Largura: '))

imprimir(f'{area(a,b)},Mts²')
