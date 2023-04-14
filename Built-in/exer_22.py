#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
#Quantidade de mouses: 100

#Situação                        Quantidade              Percentual
#1- necessita da esfera                  40                     40%
#2- necessita de limpeza                 30                     30%
#3- necessita troca do cabo ou conector  15                     15%
#4- quebrado ou inutilizado              15                     15%

situacoes = {'necessita da esfera': 0, 'necessita de limpeza': 0, 'necessita troca do cabo ou conector': 0, 'quebrado ou inutilizado': 0}

while True:
    id_mouse = int(input('Digite o número de identificação do mouse (ou 0 para encerrar): '))
    
    if id_mouse == 0:
        break
    
    tipo_defeito = input('Digite o tipo de defeito (1 - necessita da esfera; 2 - necessita de limpeza; 3 - necessita troca do cabo ou conector; 4 - quebrado ou inutilizado): ')
    
    if tipo_defeito == '1':
        situacoes['necessita da esfera'] += 1
    elif tipo_defeito == '2':
        situacoes['necessita de limpeza'] += 1
    elif tipo_defeito == '3':
        situacoes['necessita troca do cabo ou conector'] += 1
    elif tipo_defeito == '4':
        situacoes['quebrado ou inutilizado'] += 1

total = sum(situacoes.values())

print(f'Quantidade de mouses: {total}\n')
print(f'Situação{" " * 30}Quantidade{" " * 21}Percentual')
print(f'1- necessita da esfera{" " * 15}{situacoes["necessita da esfera"]:<20}{situacoes["necessita da esfera"]/total*100:>10.2f}%')
print(f'2- necessita de limpeza{" " * 14}{situacoes["necessita de limpeza"]:<20}{situacoes["necessita de limpeza"]/total*100:>10.2f}%')
print(f'3- necessita troca do cabo ou conector{" " * 1}{situacoes["necessita troca do cabo ou conector"]:<20}{situacoes["necessita troca do cabo ou conector"]/total*100:>10.2f}%')
print(f'4- quebrado ou inutilizado{" " * 10}{situacoes["quebrado ou inutilizado"]:<20}{situacoes["quebrado ou inutilizado"]/total*100:>10.2f}%')
