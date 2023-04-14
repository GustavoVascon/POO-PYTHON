#16) A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 
#1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15 
#Faça uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.

def fatorial_duplo(n):
    if n == 1:
        return 1
    else:
        return n * fatorial_duplo(n-2)

teste = fatorial_duplo(5)
print(teste)