#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
#"Qual o melhor Sistema Operacional para uso em servidores?"

#As possíveis respostas são:

#1- Windows Server
#2- Unix
#3- Linux
#4- Netware
#5- Mac OS
#6- Outro

votos = {'Windows Server': 0, 'Unix': 0, 'Linux': 0, 'Netware': 0, 'Mac OS': 0, 'Outro': 0}

while True:
    voto = int(input("Digite o número correspondente ao sistema operacional escolhido (0 para encerrar): "))
    
    if voto == 0:
        break
    
    if voto in votos:
        votos[list(votos.keys())[voto-1]] += 1
    else:
        print("Opção inválida, tente novamente.")

total_votos = sum(votos.values())
porcentagens = {k: v/total_votos*100 for k, v in votos.items()}

print(f"Total de votos: {total_votos}")
for k, v in votos.items():
    print(f"{k}: {v} votos ({porcentagens[k]:.2f}%)")
    
vencedor = max(votos, key=votos.get)
print(f"\nO sistema operacional mais votado foi o {vencedor} com {votos[vencedor]} votos.")
