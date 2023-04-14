#Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe
#contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor
#que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito)
#que adicione juros à conta. Esquecrema um programa que construa uma poupança com um saldo de R$1000,00 e uma taxa de 
#juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante

class contaInvestimento:
    
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros
    
    def adicioneJuros(self):
        self.saldo += self.saldo * (self.taxa_juros/100)
        
    def getSaldo(self):
        return self.saldo

poupanca = contaInvestimento(1000, 10)

for i in range(5):
    poupanca.adicioneJuros()

print("Saldo resultante: R$%.2f" % poupanca.getSaldo())
