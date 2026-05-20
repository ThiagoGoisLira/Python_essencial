
def votacao(ano):
    from datetime import date

    atual = date.today().year

    vot = atual - ano
    if vot <= 15:
        print(f'Com {vot} anos: NÃO VOTA')
    elif 16 >= vot < 18 :
        print(f'Com {vot} anos: VOTO OPCIONAL!')
    elif 65 > vot >= 18 :
        print(f'Com {vot} anos: VOTO OBRIGATORY')
    else:
        print(f'Com {vot} anos: VOTO OPCIONAL')

data = int(input('Em que ano você nasceu? '))
votacao(data)

