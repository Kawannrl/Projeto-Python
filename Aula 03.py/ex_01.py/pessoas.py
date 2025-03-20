class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.__nome = nome
        self.__idade = idade
        self.__cidade = cidade

    #def get_nome (self):
    #    return self.__nome
    
    @property
    def nome (self):
        return self.__nome
    
    #def set_nome (self, novo_nome):
    #    self.__nome == novo_nome
    
    @nome.setter
    def nome (self, novo_nome):
        self.__nome = novo_nome
        
    #def get_idade (self):
    #    return self.__idade 
    
    @property
    def idade (self):
        return self.__idade
    
    #def set_idade (self, valor):
    #    self.__idade += valor
    
    @idade.setter
    def idade (self, valor):
        self.__idade += valor
        
    @property
    def cidade (self):
        return self.__cidade
    
    @cidade.setter
    def cidade (self, nova_cidade):
        self.__cidade = nova_cidade
        
    def apresentar (self):
        print (f"O meu nome é {self.__nome}")
        print (f"Moro em {self.__cidade}")
        print (f"Tenho {self.__idade} anos")