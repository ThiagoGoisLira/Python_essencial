from classes.ContaCliente import ContaCliente
from classes.Banco import Banco
from classes.ContaVIP import ContaVIP
from classes.ContaComun import ContaComun

banco1 = Banco( 999, 'Teste')

conta_comun1 = ContaComun(2, 0.01, 0.1, 2000, 0.05 )
conta_remunerada = ContaVIP(3, 0.01, 0.1, 2000, 0.05)

banco1.adiciona_conta(conta_comun1)
banco1.adiciona_conta(conta_remunerada)

banco1.calcular_rendimentos()
banco1.imprime_saldo()