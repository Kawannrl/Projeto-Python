lista_impar = []
lista_par = []

for i in range(1, 11):
    numero = int (input (f"informe o {i} números: "))
    
    if numero %2 == 0:
        lista_par.append(numero)
    elif numero %2 == 1:
        lista_impar.append(numero)
    else:
        print ("Erro!!!")

print (lista_impar)
print (lista_par)