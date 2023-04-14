#11) A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. Proponha um algoritmo recursivo 
#Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros. 

def multiplicacao(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    else:
        return n1 + multiplicacao(n1, n2-1)

teste = multiplicacao(3, 10)
print(teste)