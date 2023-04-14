#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []

for i in range(20):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

par = [n for n in numeros if n % 2 == 0]
impar = [n for n in numeros if n % 2 != 0]

print("O vetor completo é:", numeros)
print("O vetor de pares é:", par)
print("O vetor de ímpares é:", impar)
