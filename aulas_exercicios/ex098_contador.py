from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-' * 30)
    print(f'Contagem de {1} até {f} de {p} em {p}')
    sleep(2)


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-----' * 10)

print('Agora personalize a contagem!')
print('-' * 30)
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)