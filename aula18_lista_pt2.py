pessoas = list ()
pessoas = [['pedro',25],['maria', 19],['thiago',32]]
print(pessoas[2][:])

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

povo = [['paulo',22],['victor', 33],['marcio',18]]
for p in povo:
    print(f'{p[0]} Tem {p[1]} Anos de idade')

opovo = list()
dados = list()
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    opovo.append(dados[:])
    dados.clear()
for p in opovo:
    if p[1] >= 18:
        print(f'{p[0]} e maior de idade')
    else:
        print(f'{p[0]} e menor de idade')