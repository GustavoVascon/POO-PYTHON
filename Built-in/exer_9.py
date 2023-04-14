#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

soma_quadrados = sum(map(lambda x: x**2, vetor))
print("A soma dos quadrados dos elementos do vetor é:", soma_quadrados)
