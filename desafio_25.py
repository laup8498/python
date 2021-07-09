def run(): 
# Verifica un string compuesto de numeros. Devuelve True si es, de lo contrario False.
# Este desafio consta de utilizar break y continue dado que ellos
# rompen los ciclos, adicional si puedes seria chevere que utilices
# for, while e if

    menu = """

    Bienvenido a la calculadora interactiva HELPCHILDS. 

         Esta herramienta tiene como finalidad fortalecer el aprendizaje
         de niños de 0 a 5 años en su proceso educativo.

    Para continuar con el proceso le solicitamos amablemente que dijite su nombre

    Nombre:  """


    nombre = str(input(menu))
    opcion = 1 


    while opcion != 0:
      print (" Bienvenid@ " + nombre + " ¿Que operacion deseas realizar?")
      menu1 = """
      1 - Sumar
      2 - Restar
      3 - Dividir
      0 - Salir del programa
    

      Elige una opcion: """

      opcion = int(input(menu1))
      

      while opcion < 0 or opcion > 3:
          print("Ingresa una opcion correcta") 
          opcion = int(input(menu1)) 
          
      if opcion != 0:
        numero1 = int(input("Por favor, escribe el primer numero: "))
        numero2 = int(input("Por favor, escribe el segundo numero: "))
        
            
        if opcion == 1:
            suma = numero1 + numero2
            suma = str(suma)
            print (" el resultado es: " + suma)
        elif opcion == 2:
            while numero1 < numero2:
                print("No se puede realizar la operacion,dado que el numero 2 es mayor al numero 1 y el resultado seria negativo")  
                numero1 = int(input("Por favor, escribe el primer numero: "))
                numero2 = int(input("Por favor, escribe el segundo numero: "))
            resta = numero1 - numero2
            resta = str(resta)
            print (" el resultado es: " + resta)
                 
        elif opcion == 3: 
            while numero2 == 0:
                print("No se puede realizar la operacion,dado que el numero 2 es 0")  
                numero2 = int(input("Por favor, escribe el segundo numero: "))
            dividir = numero1 / numero2
            dividir = str(dividir)
            print (" el resultado es: " + dividir)
    
if __name__ == "__main__":
    run()        




