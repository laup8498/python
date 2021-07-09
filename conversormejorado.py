def conversor(tipo_pesos, Valor_dolar):
    pesos = input("¿Cuantos pesos" + tipo_pesos + "tienes?: ")
    pesos = float(pesos)
    dolares = pesos/Valor_dolar
    dolares = round(dolares,4)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas de Laura ❤💰

¿Que moneda deseas convertir a dolares?

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor(" colombianos ",3875)
elif opcion == 2:
    conversor(" argentinos ",95.02)
elif opcion == 3:
    conversor(" mexicanos ",19.76)
else:
    print("ingresa una opción correcta por favor")