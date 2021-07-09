# def fact_1(n):
#     factorial_total = 1
#     while n >= 1:
#         factorial_total = factorial_total * n
#         n = n - 1 
#     return factorial_total  

numero = int(input("Ingrese un numero: "))
factorial = 1
while numero >= 1 :
    print (numero)
    factorial = factorial * numero
    numero = numero - 1

print ("Resultado " + str(factorial))
    