from exClasses02.ContaCliente import ContaCliente

class ContaComun(ContaCliente):

    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    def calcular_rendimentos(self):
        remuneracao = self.valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        self.valor_investido += remuneracao - valorIOF