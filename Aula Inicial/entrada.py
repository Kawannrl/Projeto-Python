nome = input ("Digite o seu nome: ")
print ("Seu nome é: " + nome)

idade = int (input ("Digite sua idade: "))
print ("Sua idade é: " + str(idade))

if idade < 18:
    print (f"O {nome} é menor de idade")
elif idade == 18:
    print (f"O {nome} tem 18 anos")
else :
    if idade < 30:
        print (f"O {nome} é um jovel adulto!")
    elif idade < 60:
        print (f"O {nome} é um adulto!")
    else:
        print (f"O {nome} é um idoso!")

print ("Deu certi :)")