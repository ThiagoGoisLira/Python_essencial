#Variaveis compostas TUPLAS (Vetores), Tuplas são imutáveis
"""
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'

#caso nao precise da posição
for comida in lanche:
    print(comida)
#caso precise da posição
for cont in range (0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer: {comida} - {pos}')
print('Comi muito')
"""
"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))
"""
pessoa = ('Gustavo', 40, 'M')
print(pessoa)