#Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#a. Possua uma classe chamada bombaCombustivel, com no mínimo esses atributos?
#i. tipoCombustivel
#ii. valorLitro
#iii. quantidadeCombustivel
#b. Possua no mínimo esse métodos
#i. abastecerPorValor() - método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocado no veículo
#ii. abastecerPorLitro() - método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente
#iii. alterarValor() - altera o valor do litro de combustível
#iv. alterarCombustivel() - altera o valor do litro do combustível
#v. alterarQuantidadeCombustivel() - altera o tipo de combustível
#Obs: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustivel total na bomba

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
        
    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            print('Não há combustível suficiente na bomba.')
        else:
            print(f'Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.')
            self.quantidade_combustivel -= litros_abastecidos
        
    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valor_litro
        if litros > self.quantidade_combustivel:
            print('Não há combustível suficiente na bomba.')
        else:
            print(f'O valor a ser pago é de R${valor_a_pagar:.2f}.')
            self.quantidade_combustivel -= litros
            
    def alterarValor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro
        
    def alterarCombustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
        
    def alterarQuantidadeCombustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel

bomba = BombaCombustivel('gasolina', 5.50, 1000)

bomba.abastecerPorValor(50) 
bomba.abastecerPorLitro(10) 

bomba.alterarValor(5.80)
bomba.alterarCombustivel('etanol')
bomba.alterarQuantidadeCombustivel(500)

bomba.abastecerPorValor(50)