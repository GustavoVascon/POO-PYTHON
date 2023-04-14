#Classe Retangulo: Crie uma classe que modele um retangulo:
#a. Atributos: LadoA, LadoB(ou Comprimento e Largura, ou Base e Altura, a escolher)
#b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular área e calcular Perimetro
#c. Crie um programa que utilize esta classe. Ele deve pedir ao uário que informe as medidades de um
#local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e rodapés necessárias
#para o local

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self._lado_a = lado_a
        self._lado_b = lado_b

    def get_lado_a(self):
        return self._lado_a

    def set_lado_a(self, novo_lado_a):
        self._lado_a = novo_lado_a

    def get_lado_b(self):
        return self._lado_b

    def set_lado_b(self, novo_lado_b):
        self._lado_b = novo_lado_b

    def calcular_area(self):
        return self._lado_a * self._lado_b

    def calcular_perimetro(self):
        return 2 * (self._lado_a + self._lado_b)

print("Digite as medidas do local em metros:")
comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))

local = Retangulo(comprimento, largura)

novo_comprimento = float(input("Digite o novo comprimento: "))
local.set_lado_a(novo_comprimento)

nova_largura = float(input("Digite a nova largura: "))
local.set_lado_b(nova_largura)

comprimento_atual = local.get_lado_a()
largura_atual = local.get_lado_b()

area = local.calcular_area()
perimetro = local.calcular_perimetro()

print(f"O retângulo possui lados {comprimento_atual} e {largura_atual}.")
print(f"A área do retângulo é {area:.2f} metros quadrados e o perímetro é {perimetro:.2f} metros.")