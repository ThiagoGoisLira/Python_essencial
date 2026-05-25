#Jogo de advinhar o numero que o computador esta pensando
from random import randint
computador = randint(0, 10)
num = 0
palpite = 0
print('''Sou o computador acabei de pensar em um numero entre 0 e 10,
Será quem você consegue adivinhar?''')
print('-=-'*20)
while computador != num:
    print('...'*20)
    num = int(input('Em que numero eu pensei? '))
    palpite += 1
print('ACERTOU NUMERO: {}, Acetou com {} tentativas'.format(computador,palpite))
