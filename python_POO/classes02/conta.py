class Conta:

    __total_contas = 0

    @classmethod
    def get_total_contas(cls):
        return cls.__total_contas

    @staticmethod
    def nome_banco():
        return 'Banco THIAGO'
    def __init__(self, numero, saldo):#Construtor
        self.__numero = numero#__ transforma os atributos em privados
        self.__saldo = saldo
        type(self).__total_contas += 1

    @property #Permite acessar um atributo
    def saldo(self):
        return self.__saldo

    @saldo.setter #Permite manipular Set novos valores
    def saldo_set(self, valor): #Manipulação de saldo, com proteção
        if (valor < 0):
            print('Saldo INVALIDO!')
        else:
            self.__saldo = valor

    def sacar(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            return True

    def gerar_saldo(self):
        print(f'Conta: {self.__numero}\nSaldo: {self.__saldo:10.2f}')