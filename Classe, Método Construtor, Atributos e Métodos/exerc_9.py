#Classe Ponto e Retangulo: Faça um programa completo utiliazndo funções e classes que:
#a. Possua uma classe chama Ponto, com atributos x e y
#b. Possua uma classe chamada Retangulo, com os atributos largura e altura
#c. Possua uma função para imprimir os valores da classe Ponto
#d. Possua uma função para encontrar o centro de um retângulo
#e. Você deve criar alguns objetos da classe retângulo 
#f. Cada objeto deve ter vêrtice de partida, por exemplo, o vértice inferior esquerdo do 
#retângulo, que deve ser um objeto da classe Ponto
#g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo
#ponto que indique os valores x e y para o centro do objeto.
#h. O valor do centro do objeto deve ser mostrado na tela
#i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial
        
    def centro(self):
        x = self.ponto_inicial.x + self.largura/2
        y = self.ponto_inicial.y + self.altura/2
        return Ponto(x, y)
    
def imprimir_ponto(ponto):
    print(f"({ponto.x}, {ponto.y})")
    
def imprimir_centro(retangulo):
    centro = retangulo.centro()
    print("O centro do retângulo é:")
    imprimir_ponto(centro)
    
ponto1 = Ponto(0, 0)
retangulo1 = Retangulo(5, 3, ponto1)

ponto2 = Ponto(2, 2)
retangulo2 = Retangulo(4, 6, ponto2)

print("Ponto 1:", ponto1)
print("Retângulo 1:")
imprimir_centro(retangulo1)

print("Ponto 2:", ponto2)
print("Retângulo 2:")
imprimir_centro(retangulo2)

opcao = 0
while opcao != 3:
    print("MENU")
    print("1 - Alterar valores do retângulo 1")
    print("2 - Alterar valores do retângulo 2")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        x = int(input("Digite o valor de x do ponto inicial: "))
        y = int(input("Digite o valor de y do ponto inicial: "))
        ponto1 = Ponto(x, y)
        largura = int(input("Digite a largura do retângulo: "))
        altura = int(input("Digite a altura do retângulo: "))
        retangulo1 = Retangulo(largura, altura, ponto1)
        print("Retângulo 1 atualizado:")
        imprimir_centro(retangulo1)
        
    elif opcao == 2:
        x = int(input("Digite o valor de x do ponto inicial: "))
        y = int(input("Digite o valor de y do ponto inicial: "))
        ponto2 = Ponto(x, y)
        largura = int(input("Digite a largura do retângulo: "))
        altura = int(input("Digite a altura do retângulo: "))
        retangulo2 = Retangulo(largura, altura, ponto2)
        print("Retângulo 2 atualizado:")
        imprimir_centro(retangulo2)
        
    elif opcao == 3:
        print("Saindo...")
        
    else:
        print("Opção inválida!")
