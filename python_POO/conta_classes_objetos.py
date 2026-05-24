#Classes e objetos
#Codigo da classe
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True #Saque realizado com sucesso

    def extrato(self):
        print(f'EXTRATO:\nNumero: {self.numero}\nnome: {self.nomeTitular}\ncpf:{self.cpf}\nsaldo: R${self.saldo}')

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ('Não existe saldo suficiente!')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ('Transferencia realizada com sucesso!')


#Codigo do objeto
c1 = Conta(1, 12344321, "Marcos", 9000) #Objeto
c1.depositar(500)

valSaque = 300
resultadoSaque = c1.sacar(valSaque)

if resultadoSaque:
    print(f'Saque de: R${valSaque} realizado com sucesso!')
else:
    print(f'Saldo insuficiente!')



conta1 = Conta(1, 12344321, "Thiago", 5000)#Objeto
conta2 = Conta(2, 99999999, "Marliu", 0)#Objeto

print('*****'*10)
print(conta1.transfereValor(conta2 , 300))
print('*****'*10)
c1.extrato()
print('-----'*10)
conta1.extrato()
print('-----'*10)
conta2.extrato()