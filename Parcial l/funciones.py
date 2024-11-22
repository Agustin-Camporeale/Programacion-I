#Realizar una funcion que reciba:
# -una lista (de letras de 'a' a 'h')
# y un caracter
# y retorne un entero
#La funcion debe retornar la cantidad de veces que encuantra en la lista
#El caracter pasado por parametro
#El caracter que se pasa por parametro para buscar en la lista
#se le debe solicitar al usuario
#validar que sea una lista de la 'a' a la  'h'
#No se pueden utilizar funciones propias

def contar_caracteres(lista:list, caracter:str) -> int:
     contador = 0
     for letra in lista:
          if letra == caracter:
               contador += 1
     return contador

