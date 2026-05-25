frase = 'Curso em video python'
print('-' * 25)
print (frase[9:21:3]) #Imprime aparte do endereço 9 ate 21(final) puladndo de 3 em 3
print('-' * 25)
print('Com. LEN: ',len(frase)) #Mostra a quatidade de endereços da string
print('-' * 25)
print('Com. COUNT: ',frase.count('o',0,13)) #Conta quantas veses aparece a letra O, zero 0,13 delimita o inicio eo final da contagem
print('-' * 25)
print('Com. FIND: ',frase.find('deo'))#Indica a posição encontrada o 'deo' na frase
print('-' * 25)
print('Com. FIND: ',frase.find('Android'))#Indica que essa sequencia nao exites ele alerta -1 na saida
print('-' * 25)
print('Com. IN: ','curso' in frase)#Verifica se existe curso na variavel true ou false
print('-' * 25)
print('Com. REPLACE: ',frase.replace('Python', 'Android'))#Mudar palavra python por android
print('-' * 25)
print('Com. UPPER: ',frase.upper())#Metodo para deixar letras em maiusculo
print('-' * 25)
print('Com. LOWER: ',frase.lower())#Metodo para deixar letras em minusculo
print('-' * 25)
print('Com. CAPITALIZE: ',frase.capitalize())#Muda toda a string tudo para minusculo pondo apenas a primeira letra em maiusculo
print('-' * 25)
print('Com. TITLE: ',frase.title())#Analisa quantas palavras tem e poem as inicias delas em

print('*' * 25)

newfrase = '   Aprenda Python  '
print('.' * 25)
print('Com. STRIP: ',newfrase.strip())#Remove os espaços no inicio e no final
print('.' * 25)
print('Com. RSTRIP: ',newfrase.rstrip())#Remove os espaços apenas do lado direito
print('.' * 25)
print('Com. LSTRIP: ',newfrase.lstrip())#Remove os espaços apenas do lado esquerdo

print('*' * 25)

print('Com. SLINT: ',frase.split())#Dividir a string onde tem os espaços criando uma lista
print('+' * 25)
print('Com. JOIN: ','-'.join(frase))