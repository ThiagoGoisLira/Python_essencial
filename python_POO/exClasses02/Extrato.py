class Extrato:
    def __init__(self):
        self.transacoes = []

    def gerar_extrato(self, conta):
        print(f'Extrato da Conta: {conta}')
        for transacoes in self.transacoes:
            print(f'{transacoes[0]:15s} {transacoes[1]:10.2f} {transacoes[2].strftime("%d/%m/%y")}')
#[0 - TIPO - VALOR 2 - Data]