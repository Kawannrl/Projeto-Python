from database import Pizza

def main ():
    pizza = Pizza ()
    pizza.adicionar_pizza ("Portuguesa", "média", 35.00)
    pizza.listar_pizzas ()

if __name__ == "__main__":
    main ()