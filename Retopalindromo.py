def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    
    if palabra == palabra_invertida:
        return True
    else:
        return False 

def validar_texto(palabra_nueva):
    while len(palabra_nueva) < 7:
        palabra_nueva =  input(" El texto debe tener 8 caracteres o mas: ")
    return palabra_nueva  
          
    

def run(): 
    palabra = input('escribe una palabra: ')
    palabra = validar_texto(palabra)
    es_palindromo = palindromo(palabra)
      
    if es_palindromo == True:
       print('es palindromo')
       print (palabra[:3])
           
    else: 
        print('no es palindromo')
        print (palabra[2:])
 


if __name__ == '__main__':
  run()