#Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#a. Atributos: Nome, Fome, Saúde e idade
#b. Metódos: Alterar Nome, Fome, Saúde e Idade;
#Retornar Nome, Fome, Saúde e Idade
#Obs: Existe uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
#este humor é uma condição entre os atributos Fome e Saúde, ou seja, um calculo, então
#não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada
#a qualquer momento

class Tamagushi:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

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

    def humor(self):
        return (self.fome + self.saude) / 2

meu_tamagushi = Tamagushi("Tama")

meu_tamagushi.alterar_fome(50)
meu_tamagushi.alterar_saude(75)

print("Nome:", meu_tamagushi.retornar_nome())
print("Fome:", meu_tamagushi.retornar_fome())
print("Saúde:", meu_tamagushi.retornar_saude())
print("Idade:", meu_tamagushi.retornar_idade())

print("Humor:", meu_tamagushi.humor())