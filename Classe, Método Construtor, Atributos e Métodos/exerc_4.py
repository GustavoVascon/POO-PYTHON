#classe Pessoa: Crie uma classe que modele uma pessoa:
#a. Atributos: nome, idade, peso e altura
#b. Métodos: Envelhecer, engordar, emagrecer, crescer. 
#Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve
#crescer 0,5cm

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

pessoa = Pessoa("Maria", 18, 60, 1.65)

print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade} anos")
print(f"Peso: {pessoa.peso} kg")
print(f"Altura: {pessoa.altura:.2f} m\n")

pessoa.envelhecer()
pessoa.engordar(5)
pessoa.crescer(0.10)

print("Depois de um ano:")
print(f"Idade: {pessoa.idade} anos")
print(f"Peso: {pessoa.peso} kg")
print(f"Altura: {pessoa.altura:.2f} m")
