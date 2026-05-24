from classes.Cliente import Cliente
from classes.Conta import Conta

#Testando o codigo
cliente1 = Cliente('123.651.120.-98', 'Jõao', 'Rua X')
cliente2 = Cliente('333.444.120.-65', 'Marta', 'Rua y')
cliente3 = Cliente('123.456.789-00', 'Manuel', 'Rua Z')
cliente4 = Cliente('087.234.532-99', 'Manuel', 'Rua W')

conta1 = Conta([cliente1, cliente2], 121, 120)
conta3 = Conta(cliente3, 333, 300)
conta4 = Conta(cliente4, 444, 400)

print('*****'*10)
conta1.depositar(1000)
conta1.sacar(200)
conta1.depositar(1000)
conta1.sacar(500)
conta1.extrato.gerar_extrato(conta1.numero)
conta1.gerar_saldo()
print('-----'*10)
conta3.depositar(1500)
conta3.gerar_saldo()
print('-----'*10)
conta4.depositar(1500)
conta4.sacar(200)
conta4.gerar_saldo()
print('#####'*10)

