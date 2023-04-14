#Classe Bichinho Virtual++:Melhore o programa do bichinho virtual, 
#permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca 
#com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
 
class Tamagushi:
    def __init__(self, nome, fome=0, saude=100, idade=0, tedio=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_tedio(self):
        return self.tedio

    def humor(self):
        return (self.fome + self.saude - self.tedio) / 3

    def alimentar(self, quantidade):
        self.fome -= quantidade
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo):
        self.tedio -= tempo
        if self.tedio < 0:
            self.tedio = 0


meu_tamagushi = Tamagushi("Gust")

meu_tamagushi.alimentar(20)

meu_tamagushi.brincar(30)

meu_tamagushi = Tamagushi("Gust")

meu_tamagushi.alimentar(20)

meu_tamagushi.brincar(30)

print("Nome:", meu_tamagushi.retornar_nome())
print("Fome:", meu_tamagushi.retornar_fome())
print("Saúde:", meu_tamagushi.retornar_saude())
print("Tédio:", meu_tamagushi.retornar_tedio())
print("Humor:", meu_tamagushi.humor())

