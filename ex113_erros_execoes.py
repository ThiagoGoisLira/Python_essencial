def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompido pelo usuario.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero real válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompido pelo usuario.\033[m')
            return 0
        else:
            return n

x = leiaInt('Digite um numero inteiro: ')
print(f'O valor digitado foi {x}')

y = leiaFloat('Digite um numero real: ')
print(f'O valor digitado foi {y}')