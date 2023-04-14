#Classe Quadrado: Crie uma classe que modele um quadrado:

#a. Atributos: Tamanho do lado
#b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado 
    
    def MudarValorLado(self, mudar_valor_do_lado):
        self.tamanho_lado = mudar_valor_do_lado

    def RetornarValorLado(self):
        return self.tamanho_lado

    def CalcularArea(self):
        return self.tamanho_lado **2

quadrado = Quadrado(14)

quadrado.MudarValorLado(218)

print(quadrado.RetornarValorLado())

