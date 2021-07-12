# Ejercicio 1
# nombre = input("Digite su nombre: ")
# n = input("Digite un numero: ")
# veces = (nombre + "\n") * int(n)
# print (veces)

# Ejercicio 2 
# nombre = input("Digite su nombre completo: ")
# print(str.lower(nombre))
# print(str.upper (nombre))
# # print(str.capitalize(nombre))

# ejercicio 3
# nombre = str.upper(input("Escriba su sonmbre: "))
# nl = len(nombre)
# print("El nombre de usuario " + nombre + " tiene " + str(nl) + " letras")

# ejercicio 4
# tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
# print('El número de teléfono es ', tel[2:-2])

# # ejercicio 5
# frase = input("Escriba una frase: ")
# frase1 = frase.replace (' ', '')
# frase1 = frase.lower()
# frase_invertida = frase1[::-1]
# print(frase_invertida)

# ejercicio 6 
# frase = input("Escriba una frase: ")
# vocal = input("Escriba una vocal: ")
# frase = frase.replace(vocal,vocal.upper())
# print (frase)

# ejercicio 7
# correo = input("Digite su correo eelectronico: ")
# correo = correo[:correo.find("@")]
# print (correo + "@ceu.es")

# # ejercicio 8 
# preciop = input ("ingrese el precio de su producto con dos decimales: ")
# precio = preciop[:preciop.find('.')]
# decimales = preciop[preciop.find('.') + 1:]
# print("serian en total " + str(precio) + " dolares y " + str(decimales) + " centavos")

# # ejercicio 9 
# fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
# dia = fecha[:fecha.find('/')]
# mesaño = fecha[fecha.find('/')+1:]
# mes = mesaño[:mesaño.find('/')]
# año = mesaño[mesaño.find('/')+1:]
# print('Día', dia)
# print('Mes', mes)
# print('Año', año)

# # ejercicio 10 
# cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
# cesta = cesta.replace(',', '\n')
# print(cesta)

# ejercicio 11
producto = input("Ingrese el nombre del producto: ")
unidades = int(input("Ingrese las unidades: "))
cu = int(input("Ingrese su valor unitario: "))
preciot = unidades * cu
print(str(unidades) + " unidades x " + str(cu) + " $ = " + str(preciot) + " $ pesos")