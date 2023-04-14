#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

salarios = [0] * 10 

while True:
    vendas = float(input("Digite as vendas brutas da semana (-1 para sair): "))
    if vendas == -1:
        break
    salario = 200 + 0.09 * vendas
    if salario >= 1000:
        salarios[9] += 1
    else:
        salarios[int(salario // 100) - 1] += 1

for i in range(len(salarios)):
    if i == 9:
        print("Salários acima de $1000: ", end="")
    else:
        print(f"Salários entre ${200 + i * 100} e ${299 + i * 100}: ", end="")
    print(salarios[i])
