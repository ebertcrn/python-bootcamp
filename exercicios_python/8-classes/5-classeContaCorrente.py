class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
        print(self.nome_correntista)

    def deposito(self, valor_deposito):
        self.saldo += valor_deposito
        print(self.saldo)

    def saque(self, valor_saque):
        if valor_saque > self.saldo:
            print('Você não tem saldo suficiente.')
        else:
            self.saldo -= valor_saque
            print(self.saldo)

# teste da classe
cc1 = ContaCorrente(1, 'João')
cc1.alterarNome('Maria')
cc1.deposito(100)
cc1.saque(40)