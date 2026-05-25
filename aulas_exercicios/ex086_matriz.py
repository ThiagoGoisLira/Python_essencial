matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):#Linhas 0 a 3
    for c in range(0,3):#Colunas 0 a 3
        matriz[l][c] = int(input(f'Digite um valor para posição[{l},{c}]: '))
print('----'*10)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
#print(f'Voce digitou os valores {matriz}')