#1) Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N. 

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

teste = fatorial(5)
print(teste)