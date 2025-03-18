import os

ingredientes = []

def titulo ():
    print ("""
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░███░░░░░░░░░░░░░░████░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░░░░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░████░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███████░░▄▀░░█████░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░█░░▄▀░░████████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░█████░░▄▀░░░░░░▄▀░░████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███████░░▄▀░░█████░░▄▀░░░░░░▄▀░░████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████████░░▄▀░░█████░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░█░░▄▀░░████████████░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████
█████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░████░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█████░░░░░░█████░░░░░░██░░░░░░████░░░░░░░░░░░░███░░░░░░░░░░░░░░████░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████""")
    
def exibir_menu ():
    print ("\n")
    print ("1. Adicionar ingrediente")
    print ("2. Exibir ingrediente")
    print ("3. Remover Ingrediente")
    print ("4. Sair")
    print ("\n")
    
def voltar_menu_inicial ():
    input ("Aperte o ENTER para voltar ao menu principal")
    principal ()

def adicionar_ingrediente ():
    os.system  ("cls")
    while True:
        ingrediente = input ("Digite o ingrediente: ")
        ingredientes.append (ingrediente)
        print ("Ingrediente salvo com Sucesso!")
        resposta = input ("Gostaria de adicionar outro ingrediente? (s/n)")
        
        if resposta.lower () == "n":
            break
    voltar_menu_inicial ()
    
def exibir_ingrediente ():
    os.system ("cls")
    print ("\n")
    print ("Os ingredientes são:")
    print ("\n")
    for ingrediente in ingredientes:
        print (ingrediente)
    print ("\n")
    voltar_menu_inicial ()
    

def remover_ingrediente ():
    encontrou_ingrediente = False
    os.system  ("cls")
    print ("Os ingredientes cadastros são: ")
    print ("\n")
    
    for ingrediente in ingredientes:
        print (ingrediente)
    print ("\n")    
    while True:
        remover = input ("Qual ingrediente gostaria de remover?")
        for ingrediente in ingredientes:
            if ingrediente == remover:
                ingredientes.remove (ingrediente)
                print ("Ingrediente removido com sucesso!")
                encontrou_ingrediente = True
        if encontrou_ingrediente == False:
            print ("Ingrediente não presente na receita")
        resposta = input ("Gostaria de remover outro Ingrediente (s/n)")
        if resposta.lower () == "n":
            break
    voltar_menu_inicial ()
    
def sair ():
    os.system ("cls")
    print ("Saindo...")
    exit ()
    
def escolher_menu ():
    escolha = int (input ("Escolha uma opção: "))
    
    match escolha:
        case 1:
            adicionar_ingrediente ()
        case 2:
            exibir_ingrediente ()
        case 3:
            remover_ingrediente ()
        case 4:
            sair ()
        case _:
            pass
    
def principal ():
    os.system ("cls")
    titulo ()
    exibir_menu ()
    escolher_menu ()
    
if __name__ == "__main__":
    principal ()
    