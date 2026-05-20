#Programa que leia a idade e sexo de varias pessoas, a cada pessoa cadastradas o programa devera
#pergutar se o usuario quer ou nao continuar, no final mostre:
#Quantas pessoas tem mais de 18anos
#Quantos homens foram cadastrados
#Quantas mulheres tem menos de 20 Anos

maioridade = mulheres20 = homens = cont= 0

while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    print('---'*20)
    cont += 1
    if idade >= 18:
        maioridade += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    elif sexo == 'M':
        homens += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'''Maiores de 18 anos: {maioridade}
Quantidade de homens: {homens}
Quantidade de mulheres mais 20 anos: {mulheres20}
quantidade total de pessoas: {cont}''')