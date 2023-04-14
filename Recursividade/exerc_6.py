#6) Crie um programa em python, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule k^n .
#Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir o 
#resultado da chamada da função. 

def potencia(k, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return potencia(k, n//2) * potencia(k, n//2)
    else:
        return k * potencia(k, n-1)

teste = potencia(3,2)
print(teste)