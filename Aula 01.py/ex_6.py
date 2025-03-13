opcao = int (input("Escolha umas das opções: "))

match opcao:
    case 1:
        numero = int (input("Digite um número inteiro: "))
        
        if numero %2 == 0:
            print (f"O número {numero} é par")
        else:
            print (f"O número {numero} é ímpar")
    case 2:
        numero1 = int (input("Digite um primeiro número inteiro: "))
        numero2 = int (input("Digite um segundo número inteiro: "))
        
        if numero1 > numero2:
            print (f"O número {numero1} é maior que o número {numero2}")
        elif numero1 == numero2:
            print (f"Os números {numero1} e {numero2} saõ iguais")
        else:
             print (f"O número {numero2} é maior que o número {numero1}")
    case 3:
        soma = 0
        
        numero1 = int (input("Digite um primeiro número inteiro: "))
        numero2 = int (input("Digite um segundo número inteiro: "))
        numero3 = int (input("Digite um terseiro número inteiro: "))
        
        soma = numero1 + numero2 + numero3
        
        print (f"A soma dos números {numero1}, {numero2} e {numero3} é: {soma}")
    case 4:
        print ("Você está encerrando o sistema!")
        print ("Sistema encerrando...")
    case _:
        print ("Opção inválida!")