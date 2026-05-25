#Faça um programa que jogue par ou impar com o computador, o jogo so sera interrompido quando
#jogador PERDE mostrando o total de vitorias consecutivas no final

from random import randint
cont = 0
total = 0
while True:
    computador = randint(0, 11)
    n =int(input('Digite entre 1 e 10: '))
    escolhido = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    #if n == 00:
    #    break

    total = computador + n

    if escolhido == 'P':
        if total % 2 == 0:
            print(f"VENCEU, computador escolheu: {computador}")
            cont += 1
        else:
            print("Voçê PERDEU")
            break
    elif escolhido == 'I':
        if total % 2 != 0:
            print(f"VENCEU, computador escolheu: {computador}")
            cont += 1
        else:
            print("Voçê PERDEU")
            break

print(f'Voçê venceu {cont} vezes')