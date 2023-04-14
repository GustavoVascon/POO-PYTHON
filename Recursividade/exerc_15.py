#15) Faça uma função recursiva que receba um número inteiro 
#positivo par N e imprima todos os números pares de 0 até N em ordem decrescente. 

def imprimir_pares_decrescente(n):
    if n == 0:
        print(0)
    else:
        if n % 2 == 0:
            print(n)
        imprimir_pares_decrescente(n-2)

teste = imprimir_pares_decrescente(10)
print(teste)