#Leia o nome e média de um aluno, guarde tbm a situação em um dicionario
#No final mostre o conteudo da estrutura da tela

aluno = dict () #Cria discionario
aluno['nome'] = str(input('Nome: '))#Adiciona o id nome e preenche
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))#Adiciona o id media e preenche
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-----'*10)
for k, v in aluno.items():#Os Id como k keys, v values
    print(f'{k} é Igual: {v}')