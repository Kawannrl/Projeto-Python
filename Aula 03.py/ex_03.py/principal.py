from contas import Conta

def mostrar_menu ():
    print ("1. Criar Conta Bancária")
    print ("2. Ver Saldo")
    print ("3. Fazer Depósito")
    print ("4. Fazer Saque")
    print ("5. Sair")
    
def criar_conta ():
    nome =  input ("Digite o seu nome: ")
    c1 = Conta (nome)
    print ("Conta aberta com sucesso!")

def escolher_opcao ():
    opcao = int (input ("Digite uma das opções: "))
    
    match opcao:
        case 1:
            criar-conta ()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            pass

def main ():
    mostrar_menu ()
    escolher_opcao ()
    #c1 = Conta ("Kawann")
    #c1.ver_saldo ()
    #valor = int (input ("Digite o valor à depositar: "))
    #c1.depositar (valor)
    #c1.ver_saldo ()
    #saque = int (input ("Digite o valor à sacar: "))
    #c1.sacar (saque)
    #c1.ver_saldo ()

if __name__ == "__main__":
    main ()