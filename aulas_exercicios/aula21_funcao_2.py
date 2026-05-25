'''
def contador(i, f, p):
    """
    -->Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: na tela
    Função criada por Thiago Gois
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM')

contador(2,10,2)
'''
'''
def somar(a,b,c=0):
    """
    -->Faz a soma de três valores e mostra na tela.
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    """
    s = a + b + c
    print(f'A soma vale: {s}')

somar(2,3)
'''