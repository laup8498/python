def calcularNombreCompleto(nombre, apellido):
  return nombre + " " + apellido

def run():
  nombre = input("Digite su nombre: ")
  apellido = input("Digite su apellido: ")

  print("Hola " + calcularNombreCompleto(nombre, apellido))

if __name__ == "__main__":
  run()