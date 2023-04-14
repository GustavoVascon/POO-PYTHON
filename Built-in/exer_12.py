#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []
altura_total = 0
media_altura = 0
cont_alunos = 0

for i in range(30):
    idade = int(input(f"Digite a idade do {i+1}º aluno: "))
    altura = float(input(f"Digite a altura do {i+1}º aluno (em metros): "))
    idades.append(idade)
    alturas.append(altura)
    altura_total += altura

media_altura = altura_total / len(alturas)

for i in range(30):
    if idades[i] > 13 and alturas[i] < media_altura:
        cont_alunos += 1

print(f"Há {cont_alunos} alunos com mais de 13 anos e altura inferior à média de altura dos alunos.")
