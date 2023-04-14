#Aprimore a classe do exercício anterior para adicionar o método aumentarSalário (percentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
#Exemplo de uso:
#harry=funcionario("Harry",25000)
#harry.aumentarSalario(10)

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario
    
    def aumentarSalario(self, percentualDeAumento):
        aumento = self.salario * (percentualDeAumento / 100)
        self.salario += aumento
        
harry = Funcionario("Harry", 25000)
print(harry.getNome()) 
print(harry.getSalario())  

harry.aumentarSalario(10)

print(harry.getSalario())  
