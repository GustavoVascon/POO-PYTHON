#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

for i in range(10):
    num1 = int(input(f"Digite o {i+1}º número do primeiro vetor: "))
    vetor1.append(num1)

for i in range(10):
    num2 = int(input(f"Digite o {i+1}º número do segundo vetor: "))
    vetor2.append(num2)

for i in range(10):
    num3 = int(input(f"Digite o {i+1}º número do terceiro vetor: "))
    vetor3.append(num3)

for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print("Quarto vetor intercalado:", vetor4)
