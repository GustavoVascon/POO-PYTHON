#Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores 
#exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, 
#não listada no menu, for informada na escolha do usuário. Dica: 
#acrescente um método especialstr() à classe Bichinho.

class Tamagushi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.saude = 50
        self.idade = 0
        self.tedio = 50

    def __str__(self):
        return f"Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}\nTédio: {self.tedio}"

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def alimentar(self, quantidade):
        self.fome -= quantidade
        if self.fome < 0:
            self.fome = 0
        self.saude += 10
        if self.saude > 100:
            self.saude = 100

    def brincar(self, minutos):
        self.tedio -= minutos
        if self.tedio < 0:
            self.tedio = 0
        self.saude += 5
        if self.saude > 100:
            self.saude = 100

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
        humor = (self.fome + self.saude) / 2
        if humor <= 25:
            return "Triste"
        elif humor <= 50:
            return "Normal"
        elif humor <= 75:
            return "Feliz"
        else:
            return "Muito feliz"

meu_tamagushi = Tamagushi("Tama")

meu_tamagushi.alimentar(20)

meu_tamagushi.brincar(30)

if input("Digite a senha para ver os valores exatos do objeto: ") == "senha":
    print(meu_tamagushi)
else:
    print("Nome:", meu_tamagushi.retornar_nome())
    print("Fome:", meu_tamagushi.retornar_fome())
    print("Saúde:", meu_tamagushi.retornar_saude())
    print("Idade:", meu_tamagushi.retornar_idade())
    print("Humor:", meu_tamagushi.retornar_humor())
