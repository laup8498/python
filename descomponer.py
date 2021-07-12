def run():
  texto = "Ingrese un numero de 3 cifras"
  numero = int(input(texto))
  numero1 = numero % 10
  numero  = int(numero / 10)
  numero2 = numero % 10
  numero = int(numero / 10)
  numero3 = numero

  if numero1 % 2 == 0:
    print('El numero ' + str(numero1) +' es par')
  else:
    print('El numero ' + str(numero1) +' es impar')
  if numero1 % 2 == 0:
    print('El numero ' + str(numero2) +' es par')
  else:
    print('El numero ' + str(numero2) +' es impar')
  if numero1 % 2 == 0:
    print('El numero ' + str(numero3) +' es par')
  else:
    print('El numero ' + str(numero3) +' es impar')
  

if __name__== "__main__":
    run()