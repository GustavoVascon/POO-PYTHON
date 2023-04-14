#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    num1 = int(input(f"Digite o {i+1}º número do primeiro vetor: "))
    vetor1.append(num1)

for i in range(10):
    num2 = int(input(f"Digite o {i+1}º número do segundo vetor: "))
    vetor2.append(num2)

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("Terceiro vetor intercalado:", vetor3)
