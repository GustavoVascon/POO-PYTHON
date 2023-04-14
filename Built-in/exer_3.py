#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
    nota = float(input("Digite a {}ª nota: ".format(i+1)))
    notas.append(nota)

media = sum(notas) / len(notas)

print("As notas são:", notas)
print("A média é:", media)
