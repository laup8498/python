def run():
     
    menu = """

    Bienvenido a la calculadora de conversion de monedas . 

         Esta herramienta tiene como finalidad ayudar al usuario para que conozca el equivalente en dolares de tres monedas de LATAM.

    Para continuar con el proceso le solicitamos amablemente que dijite su nombre

    Nombre:  """


    nombre = str(input(menu))
    opcion = 1 

    while opcion != 0:
        print ("Bienvenido " + nombre + " al conversor de monedas de Laura ❤💰 ¿Que moneda deseas convertir a dolares?")

        menu1="""
        
        1 - Pesos colombianos
        2 - Pesos argentinos
        3 - Pesos mexicanos
        0 - Salir del programa

        Elige una opcion: """

        opcion = int(input(menu1))

        while opcion < 0 or opcion > 3:
            print("Ingresa una opcion correcta") 
            opcion = int(input(menu1)) 
        
        if opcion != 0:
            

            if opcion == 1:
                pesos = int(input("¿Cuantos pesos colombianos tienes?: "))
                pesos = float(pesos)
                Valor_dolar = 3875
                dolares = pesos/Valor_dolar
                dolares = round(dolares,2)
                dolares = str(dolares)
                print("tienes $" + dolares + " dolares")

            elif opcion == 2:
                pesos = int(input("¿Cuantos pesos argentinos tienes?: "))
                pesos = float(pesos)
                Valor_dolar = 95.02
                dolares = pesos/Valor_dolar
                dolares= round(dolares,2)
                dolares = str(dolares)
                print("tienes $" + dolares + " dolares")

            elif opcion == 3:
                pesos = int(input("¿Cuantos pesos mexicanos tienes?: "))
                pesos = float(pesos)
                Valor_dolar = 19.76
                dolares = pesos/Valor_dolar
                dolares= round(dolares,2)
                dolares = str(dolares)
                print("tienes $" + dolares + " dolares")
            else:
                print("ingresa una opción correcta por favor")

if __name__ == "__main__":
    run()