#3) Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321 

def inverte(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10 ** (len(str(n))-1) + inverte(n // 10)

teste = inverte(123)
print(teste)