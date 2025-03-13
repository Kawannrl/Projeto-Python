#for i in range (1, 11):
#    print (i)
    
lista = [1, 2, 3.10, "texto", True]
lista.append (100)

for i in lista:
    print (i)
    
dicinario = {
    "nome": "Kawann",
    "idade": "18",
}

dicionario_2 = dict (nome = "Kawann", idade = "18")

for i in dicinario.keys ():
    print (i, " = ", dicinario (i))
    
for i in dicinario.values ():
    print (i)
    
lista_1 = []
lista_2 = []

for chave, valor in dicinario.items():
    lista_1.append (chave)
    lista_1.append (valor)
    
print (lista_1)
print (lista_2)