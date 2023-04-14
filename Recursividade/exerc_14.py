#14) Faça uma função recursiva que receba um número inteiro positivo par N e 
#imprima todos os números pares de 0 até N em ordem crescente. 

def imprimir_pares_crescente(n):
    if n == 0:
        print(0)
    else:
        imprimir_pares_crescente(n-2)
        if n % 2 == 0:
            print(n)

teste = imprimir_pares_crescente(10)
print(teste)
