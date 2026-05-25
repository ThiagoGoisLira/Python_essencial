from Cliente import Cliente
from Conta import Conta
from ContaEspecial import ContaEspecial
from ContaRemuneradaPoupanca import ContaRemuneradaPoupanca

#Testando o codigo
cliente1 = Cliente('123.651.120.-98', 'Jõao', 'Rua X')
cliente2 = Cliente('333.444.120.-65', 'Marta', 'Rua y')
cliente3 = Cliente('123.456.789-00', 'Manuel', 'Rua Z')
cliente4 = Cliente('087.234.532-99', 'Manuel', 'Rua W')



conta1 = Conta(cliente1, 11, 1000)
conta2 = Conta(cliente2, 22, 2000)
conta3 = ContaEspecial(cliente3, 31, 4000, 500)
conta4 = ContaRemuneradaPoupanca(cliente4, 44, 2000, 1.1)


conta1.depositar(300)
conta1.transfere_valor(conta2,500)

conta2.sacar(700)
conta3.sacar(400)

print('*****'*10)
conta1.extrato.gerar_extrato(conta1)
print('-----'*10)
conta2.gerar_saldo()
print('-----'*10)
conta3.extrato.gerar_extrato(conta3)
print('-----'*10)
conta4.gerar_saldo()
