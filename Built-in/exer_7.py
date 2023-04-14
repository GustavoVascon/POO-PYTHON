#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = []

for i in range(5):
    num = int(input("Digite um número inteiro: "))
    vetor.append(num)

soma = sum(vetor)
multiplicacao = 1
for n in vetor:
    multiplicacao *= n

print("O vetor é:", vetor)
print("A soma dos elementos é:", soma)
print("A multiplicação dos elementos é:", multiplicacao)
