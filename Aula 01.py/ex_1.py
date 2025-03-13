numero: int = 10
numero2: int = 10.10

"""
if (numero > 10){
    System.out.println ("número maior que " + numero);
}
"""

numero = int (input("Digite um Número: "))

if numero > 10:
    print ("número", numero, " maior que 10")
elif numero < 10:
    print (f"número ", {numero}, " menor que 10")
else:
    print (f"número {numero} é 10")
    
print (f"numero2 = {numero2}")