#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []
contador = 0

for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input("Digite a {}ª nota do {}º aluno: ".format(j+1, i+1)))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)
    if media >= 7.0:
        contador += 1

print("As médias dos alunos são:", medias)
print("O número de alunos com média maior ou igual a 7.0 é:", contador)
