import mysql.connector

class Pizza:
    
    def __init__(self):
        self.__conexao = mysql.connector.connect (
            host = 'localhost',
            user = 'kawann',
            password = '1234',
            database = 'pizzaria'
        )
        
        self.__cursor = self.__conexao.cursor ()
        self.criar_tabelas ()
    
    def criar_tabelas (self):
        query = ("""create table if not exists pizzas(
                id int auto_increment primary key,
                nome varchar(255) not null,
                tamanho varchar(255) not null default 'grande',
                preco decimal(10,2))""")
        self.__cursor.execute (query)
        self.__conexao.commit ()
    
    def adicionar_pizza (self, nome, tamanho, preco):
        self.__cursor.execute ('insert into pizzas (nome, tamanho, preco) values (%s,%s, %s)', (nome, tamanho, preco))
        self.__conexao.commit ()
        print ("Pizza adicionada com sucesso!")
        
    def listar_pizzas (self):
        self.__cursor.execute ('select * from pizzas')
        pizzas = self.__cursor.fetchall ()
        
        if not pizzas:
            print ("Pizzas não cadastradas")
        else:
            for pizza in pizzas:
                print (f"id: {pizza [0]}| Nome: {pizza [1]}| Tamanho: {pizza [2]}| Preço: {pizza [3]}")
        self.__conexao.commit ()