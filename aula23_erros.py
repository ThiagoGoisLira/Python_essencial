'''
except Exception as erro:
    print(f'Infelizmente tivemos um problema: {erro.__class__}')
'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados')
except ZeroDivisionError:
    print('Não e possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
