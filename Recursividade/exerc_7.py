#7) Crie um programa em python que receba um vetor de números reais com 100 elementos. Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor. 

import random

def inverte_vetor(v, i, j):
    if i < j:
        v[i], v[j] = v[j], v[i]
        inverte_vetor(v, i + 1, j - 1)

vetor = [random.uniform(0, 100) for _ in range(100)]
print("Vetor original:", vetor)
inverte_vetor(vetor, 0, 99)
print("Vetor invertido:", vetor)
