#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = []

for i in range(10):
    char = input("Digite um caractere: ")
    vetor.append(char)

consoantes = [c for c in vetor if c not in 'aeiouAEIOU']

print("As consoantes são:", consoantes)
print("Foram lidas {} consoantes".format(len(consoantes)))
