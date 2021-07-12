menu = """
Bienvenido al conversor de monedas de Laura ❤💰

¿Que moneda deseas convertir a dolares?

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    Valor_dolar = 3875
    dolares = pesos/Valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("¿Cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    Valor_dolar = 95.02
    dolares = pesos/Valor_dolar
    dolares= round(dolares,2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("¿Cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    Valor_dolar = 19.76
    dolares = pesos/Valor_dolar
    dolares= round(dolares,2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
else:
    print("ingresa una opción correcta por favor")


