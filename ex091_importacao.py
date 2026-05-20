#Jogo de dados em python
from random import randint #Importando a biblioteca ramdom
from time import sleep #Importando a biblioteca time
from operator import itemgetter#Impora a biblioteca organização
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
ranking = list ()#trata o resultado como lista
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado...')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#
print('-'*40)
print('  --RANKING DOS JOGADORES--')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
