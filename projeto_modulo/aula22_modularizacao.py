'''
--> Adicione os modulos do arquivo Uteis
import uteis
uteis.fatorial(n)
'''
#Importações
from uteis import numeros
from uteis import strings

#Inicio do projeto
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
strings.imprimir(f'O fatorial de {num} é {fat}')