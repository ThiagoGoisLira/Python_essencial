'''#Dicionarios indices para listas e tupas
pessoas = {'nome':'Thiago','sexo':'M','idade':32}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['peso'] = 72.5#Adicionando um novo item
for k, v in pessoas.items():
    print(f'{k} = {v}')
    print('-----'*10)
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''
brasil = []
estado1 = {'uf' : 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf' : 'São paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
'''
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v} ', end='')
    print()
'''
locadora = [
    {'titulo':'Star wars','ano':1977,'diretor':'George Lucas'},
    {'titulo':'Avengers','ano':2012,'diretor':'Joss Whedon'},
    {'titulo':'Matrix','ano':1999,'diretor':'Wachowski'}
]
print(locadora[0]['ano'])
print(locadora[2]['titulo'])