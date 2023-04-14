#4) Faça uma função recursiva que permita somar os elementos de um vetor de inteiros. 

def soma_vetor(v, n):
    if n == 0:
        return 0
    else:
        return v[n-1] + soma_vetor(v, n-1)

v = [1, 2, 3, 4, 5]
n = len(v)
print(soma_vetor(v, n))
