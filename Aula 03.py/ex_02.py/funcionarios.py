class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        
    def exibir_informacoes (self):
        print (f"Funcionário: {self.__nome}")
        print (f"Cargo: {self.__cargo}")
        print (f"Salário: R$ {self.__salario:.2f}")
        print ("\n")
    
    def aplicar_aumento (self, porcentagem):
        self.__salario *= (1 + porcentagem/100)
        
    def mudar_cargo (self, novo_cargo):
        self.__cargo = novo_cargo
        
    @property
    def salario (self):
        return self.__salario
    
    @salario.setter
    def salario (self, aumento_salario):
        self.__salario += aumento_salario
    
    @property
    def cargo (self):
        return self.__cargo
    
    @cargo.setter
    def cargo (self, novo_cargo):
        self.__cargo = novo_cargo