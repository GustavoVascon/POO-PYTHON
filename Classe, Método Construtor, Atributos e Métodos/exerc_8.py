#Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos
#nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
#Faça um programa ou teste interativamente com que um macaco coma o outro.
#É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
    def comer(self, alimento):
        self.bucho.append(alimento)
    
    def verBucho(self):
        print(f"{self.nome} tem no bucho: {', '.join(self.bucho)}")
    
    def digerir(self):
        self.bucho = []
        print(f"{self.nome} digeriu tudo.")

macaco1 = Macaco("Macaco1")
macaco2 = Macaco("Macaco2")

macaco1.comer(macaco2.nome)
macaco1.verBucho() 
macaco1.digerir()