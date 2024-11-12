# Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
# Debe retornar las veces que la letra está incluida en el texto.

def buscar_caracter(letra:str,texto:str)->int:
     contador = 0
     for caracter in texto.lower():
          if caracter == letra.lower():
               contador += 1
     return contador

# Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
# Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
# Si las posiciones no son válidas se debe informar.

def cadena(cadena:str, indice_1:int, indice_2:int) -> str:
     if indice_1 < 0 or indice_2 >= len(cadena) or indice_1 > indice_2: # Verificar si los índices son válidos
          return "Índices no válidos"
     return cadena[indice_1:indice_2+1] # retorna los caracteres desde indice1 hasta indice2 (inclusive)

print(cadena("abcdefgh",3,6))

# Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
# Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
# **IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
# <número de caracteres> - 1.

def char_at(cadena:str, numero:int):
     for i in range(len(cadena)+1):
          if i == numero:
               return cadena[numero-1]
     if i != numero:
          return False


print(char_at("hola",4))
