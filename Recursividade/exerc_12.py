#12) Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais 
#de 0 até N em ordem crescente. 

def imprime_crescente(n):
    if n == 0:
        return
    else:
        imprime_crescente(n-1)
        print(n)

teste = imprime_crescente(10)
print(teste)