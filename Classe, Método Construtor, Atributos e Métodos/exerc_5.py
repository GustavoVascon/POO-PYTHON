#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir
#os seguintes atributos: Atributos da conta, nome do correntisra e saldo. Os métodos são os seguintes:
#alterar nome, depósito e saque; No construtor, saldi é opcional, com valor default zero e os demais atributos
# são obrigatórios

class ContaCorrente:
    def __init__(self, nome_correntista, saldo=0):
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

conta = ContaCorrente("João", 1000)

print(f"Nome do correntista: {conta.nome_correntista}")
print(f"Saldo: R$ {conta.saldo:.2f}\n")

conta.alterar_nome("Maria")
conta.deposito(500)
conta.saque(2000)

print("Depois das operações:")
print(f"Nome do correntista: {conta.nome_correntista}")
print(f"Saldo: R$ {conta.saldo:.2f}")
