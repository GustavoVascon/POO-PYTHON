#Classe Bola: Crie uma classe que modele uma bola:
#a. Atributos: Cor, circunferência, material
#b. Métodos: trocarCor e mostraCor

class Bola: #Declarando uma classe
    def __init__(self, cor, circunferencia, material ): #Construtor "__init__" e os atributos cor, circuf...
        self.cor = cor #self, faz referência ao self do construtor, self.cor, este é uma variável e o = cor faz referência a cor do método
        self.circunferencia = circunferencia
        self.material = material
    
    def trocar_cor(self, cor): #Método trocar cor
        self.cor = cor 

    def mostrar_cor(self): #Método mostrar cor 
        return self.cor

bola = Bola("verde", 19, "couro") #Variável bola que chama a classe Bola e passa valores para os atributos (cor, circunferencia, material)

print(bola.mostrar_cor())

bola.trocar_cor("azul")

print(bola.mostrar_cor())

