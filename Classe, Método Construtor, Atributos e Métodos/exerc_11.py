#Classe Carro: Implemente uma classe chamada carro com as seguintes propriedades:
#a. Um veículo tem um certo consumo de combustível (medidos em km/litro) e uma certa quantidade
#de combustível no tanque.
#b. O consumo é especificado no construtor e o nível de combustível inicial é 0
#c. Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância
#reduzindo o nível de combustível no tanque de gasolina.
#d. Forneça um método obterGasolina(), que retorna o nível atual de combustível.
#e. Forneça um método adicionarGasolina(), para abastecer o tanque. Exemplo de uso:
#meuFusca = Carro(15) 
#meuFusca.adicionarGasolina(20)
#meuFusca.andar(100)
#meuFusca.obterGasolina()

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.gasolina = 0
        
    def andar(self, distancia):
        consumo_total = distancia/self.consumo
        if consumo_total <= self.gasolina:
            self.gasolina -= consumo_total
            print("O carro percorreu", distancia, "km.")
        else:
            print("Não há combustível suficiente para percorrer essa distância.")
            
    def obterGasolina(self):
        return self.gasolina
    
    def adicionarGasolina(self, quantidade):
        self.gasolina += quantidade

meuFusca = Carro(15) 
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
print(meuFusca.obterGasolina())
