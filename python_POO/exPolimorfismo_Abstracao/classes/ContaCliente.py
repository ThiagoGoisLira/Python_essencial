from abc import ABC, abstractmethod

class ContaCliente(ABC):

    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):#Metodo construtor
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valor_investido = valor_investido
        self.taxa_rendimento = taxa_rendimento

    @abstractmethod
    def calcular_rendimentos(self):
        pass

    def extrato(self):
        print(f'O saldo atual da conta {self.numero} é {self.valor_investido:10.2f}')