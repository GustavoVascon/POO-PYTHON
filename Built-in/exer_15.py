#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

notas = []
nota = 0

while nota != -1:
    nota = float(input("Digite uma nota (-1 para encerrar): "))
    if nota != -1:
        notas.append(nota)

qtd_notas = len(notas)

print("Quantidade de notas lidas:", qtd_notas)

print("Notas informadas: ", end="")
for nota in notas:
    print(nota, end=" ")

print("\nNotas invertidas: ")
for nota in reversed(notas):
    print(nota)

soma = sum(notas)
print("Soma das notas: ", soma)

media = soma / qtd_notas
print("Média das notas: ", media)

qtd_acima_media = 0
for nota in notas:
    if nota > media:
        qtd_acima_media += 1
print("Quantidade de notas acima da média: ", qtd_acima_media)

qtd_abaixo_sete = 0
for nota in notas:
    if nota < 7:
        qtd_abaixo_sete += 1
print("Quantidade de notas abaixo de sete: ", qtd_abaixo_sete)

print("Programa encerrado.")
