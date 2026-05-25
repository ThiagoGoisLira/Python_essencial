maxVel = 80
vel = int(input('Qual a velocidade do carro? '))
if vel > maxVel:
    atual = vel - maxVel
    print('Velociade atual:',vel,'kM/h Excedeu:',atual,'kM/h, Ira pagar:',atual * 7, 'R$')
else:
    print('Velocidade do carro:',vel,'km/h PARABENS!')