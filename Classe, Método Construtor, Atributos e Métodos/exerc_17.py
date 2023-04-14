#Crie uma Fazenda de Bichinhos instanciando 
#vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, 
#mas ao invés de exigir que o usuário tome conta de um único bichinho, exija que ele tome conta dafazenda inteira. 
#Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos 
#(alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). 
#Para tornar o programa mais interessante, dê para cada bichinho um nível inicial aleatório de fome e tédio.

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.saude = 50
        self.idade = 1
        self.humor = "feliz"

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_humor(self):
        return self.humor

    def alimentar(self, quantidade):
        self.fome -= quantidade
        if self.fome < 0:
            self.fome = 0
        self.saude += quantidade / 2
        if self.saude > 100:
            self.saude = 100
        self.humor = "feliz"

    def brincar(self, tempo):
        self.fome += tempo
        if self.fome > 100:
            self.fome = 100
        self.saude -= tempo / 2
        if self.saude < 0:
            self.saude = 0
        self.idade += tempo / 60
        if self.idade > 10:
            self.idade = 10
        self.humor = "feliz"

    def ouvir(self):
        self.humor = "feliz"

class Fazenda:
    def __init__(self):
        self.bichinhos = []

    def adicionar_bichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentar_todos(self, quantidade):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade)

    def brincar_todos(self, tempo):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo)

    def ouvir_todos(self):
        for bichinho in self.bichinhos:
            bichinho.ouvir()

    def mostrar_bichinhos(self):
        for bichinho in self.bichinhos:
            print("Nome:", bichinho.retornar_nome())
            print("Fome:", bichinho.retornar_fome())
            print("Saúde:", bichinho.retornar_saude())
            print("Idade:", bichinho.retornar_idade())
            print("Humor:", bichinho.retornar_humor())
            print()


bichinho1 = Bichinho("Fido")
bichinho2 = Bichinho("Bob")
bichinho3 = Bichinho("Rex")

fazenda = Fazenda()
fazenda.adicionar_bichinho(bichinho1)
fazenda.adicionar_bichinho(bichinho2)
fazenda.adicionar_bichinho(bichinho3)

# Menu de opções para o usuário
opcao = ""
while opcao != "4":
    print("1 - Alimentar todos os bichinhos")
    print("2 - Brincar com todos os bichinhos")
    print("3 - Ouvir todos os bichinhos")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        quantidade = int(input("Quantidade de comida: "))
        fazenda.alimentar_todos(quantidade)
        print("Bichinhos alimentados!")

    elif opcao == "2":
        tempo = int(input("Tempo de brincadeira (em minutos): "))
        fazenda.brincar_todos(tempo)
        print("Bichinhos brincando!")

    elif opcao == "3":
        fazenda.ouvir_todos()
        print("Bichinhos ouvidos!")

    elif opcao == "4":
        print("Saindo...")

    else:
        print("Opção inválida. Tente novamente.")

fazenda.mostrar_bichinhos()
