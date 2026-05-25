games = ('Dont starve','God of war', 'God of war raganrok','Resident evil 4','Resident evil 2',
         'Read dead 2','Tomb raider','Devil may cry','Terraria','Skyrim','The witch','The forest',
         'The last of us','Need for speed','Gta V','Guitar hero','Batman','Hitman','Call of duty',
         'Motoqueiro fantasma')
print('-----'*20)
print(f'Lista de games: {games}')
print('-----'*20)
print(f'Os 5 primeiros são: {games[:5]}')
print('-----'*20)
print(f'Os 4 ultimos são: {games[-4:]}')
print('-----'*20)
print(f'Em ordem alfabetica: {sorted(games)}')
print('-----'*20)
print(f'A posição do Terraria: {games.index("Terraria")+1}ª')
