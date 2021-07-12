def run():

    menu = """

    Bienvenido al centro de compras de Laura.SAS ❤💰

    Para continuar con el proceso le solicitamos amablemente que dijite su edad correctamente

    ¿Que edad tienes?:  """

    opcion = int(input(menu))

    while opcion < 18:
        texto = "Debe ser mayor de edad para continuar con la operacion: "
        opcion = int(input(texto))

    nombre= (input("¿Cual es su nombre?: "))
    print("Bienvenido " + nombre)
   

if __name__== "__main__":
    run()