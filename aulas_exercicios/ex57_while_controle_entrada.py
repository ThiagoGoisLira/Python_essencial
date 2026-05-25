#Faça um programa que leia o sexo da pessoa que so aceite 'M' ou 'F' caso esteja errado peça novamente

#s = ""
#c = 0
#while c != 1:
#    s = input('Digite seu sexo (M/F): ')
#    if s == "m":
#        c = 1
#    elif s == "f":
#        c = 1
#print('Sexo {} registrado com sucesso!'.format(s))

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, Digite o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} Registrado com sucesso'.format(sexo))