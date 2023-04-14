#13) Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais 
#de 0 até N em ordem decrescente. 

def imprimir_naturais_decrescente(n):
    if n == 0:
        print(0)
    else:
        print(n)
        imprimir_naturais_decrescente(n-1)

teste = imprimir_naturais_decrescente(10)
print(teste)