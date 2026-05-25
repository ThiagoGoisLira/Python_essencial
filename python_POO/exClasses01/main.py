from conta import Conta

c1 = Conta(1, 1000)#Acesso a Class Conta e criar os objetors
c2 = Conta(2, 200)
c3 = Conta(3, 0)

c1.saldo_set = 1500#Atributos Objetos
#print(f'Conta -{c1.__numero}- com saldo R${c1.__saldo}')
#print(f'Conta -{c2.__numero}- com saldo R${c2.__saldo}')

print(f'Até agora temos: {Conta.get_total_contas()}, conta(s) criadas(s)')#Atributos de Classes
print(f'Obrigado por ser cliente do {Conta.nome_banco()}')
#c1.gerar_saldo()
#c2.gerar_saldo()
print(c1.saldo)
print(c2.saldo)
