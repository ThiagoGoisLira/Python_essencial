#O programa de ler um numero pelo teclado entre 0 e 20 e mostralo por extenso
numero = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
print('Você digitou:',numero[n])