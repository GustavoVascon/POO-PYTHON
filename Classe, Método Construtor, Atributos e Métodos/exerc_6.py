#Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz
#de informar o número do canal e aumentar ou diminuir o volume. 
#Certifique-se de que o número do canal e o nível do volume permanecem dentros de faixas válidas.

class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 10

    def mudar_canal(self, canal):
        if canal >= 1 and canal <= 100:
            self.canal = canal
        else:
            print("Canal inválido")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo atingido")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo atingido")

tv = TV()

print(f"Canal: {tv.canal}")
print(f"Volume: {tv.volume}\n")

tv.mudar_canal(10)
tv.aumentar_volume()
tv.diminuir_volume()

print("Depois das operações:")
print(f"Canal: {tv.canal}")
print(f"Volume: {tv.volume}")