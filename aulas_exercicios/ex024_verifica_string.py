#Verifica se a cidade que nasceu começa com santo
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')