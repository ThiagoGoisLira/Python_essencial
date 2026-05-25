#Crie um programa que faça o computar jogar com voçê
x = int(input('Escolha entre: 1 - Pedra, 2 - Papel, 3 - Tesoura'))
computador = 2 #Papel
if x == 1:
    print('O computador escolheu {}'.format(computador),'Voçê escolheu {}'.format(x),'Voçê PERDEU')
elif x == 2:
    print('O computador escolheu {}'.format(computador),'Voçê escolheu {}'.format(x),'EMPATE')
elif x == 3:
    print('O computador escolheu {}'.format(computador),'Voçê escolheu {}'.format(x),'Voçê GANHOU')