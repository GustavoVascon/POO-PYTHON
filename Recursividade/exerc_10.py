#10) Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192. 

def contar_digitos(n, k):
    if n == 0:
        return 0
    elif n % 10 == k:
        return 1 + contar_digitos(n//10, k)
    else:
        return contar_digitos(n//10, k)

teste = contar_digitos(32, 3213)
print(teste)