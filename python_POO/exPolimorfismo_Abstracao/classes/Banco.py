class Banco:
    def __init__(self, codigo, nome):#Semple que uma conta e criada ela e passada pra uma lista contas
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adiciona_conta(self, conta_cliente):#Metodo para adicioanr conta no banco
        self.contas.append(conta_cliente)

    def calcular_rendimentos(self):
        for c in self.contas:
            c.calcular_rendimentos()

    def imprime_saldo(self):
        for c in self.contas:
            c.extrato()