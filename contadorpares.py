def esPar(numero):
  if numero % 2 == 0:
    print('El numero ' + str(numero) +' es par')
  else:
    print('El numero ' + str(numero) +' es impar')

def run():
  esPar(45)
  texto = "Ingrese un numero de 3 cifras"
  numero = int(input(texto))
  numero1 = numero % 10
  numero  = int(numero / 10)
  numero2 = numero % 10
  numero = int(numero / 10)
  numero3 = numero
  
  esPar(numero1)
  esPar(numero2)
  esPar(numero3)

  print("Gracias por su atencion.")


if __name__ == "__main__":
  run()