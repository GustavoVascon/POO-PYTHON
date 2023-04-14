#Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome(um string) e 
#um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos
#para devolver nome e salário. Escreva um pequeno programa que teste sua classe

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario

# Exemplo de uso
funcionario1 = Funcionario("João", 2500.00)
print("Nome:", funcionario1.getNome())
print("Salário:", funcionario1.getSalario())
