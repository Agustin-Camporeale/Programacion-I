from .validate import *

# 1- Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

def get_in(mensaje:str, mensaje_error: str, minimo: int,maximo:int, reintentos: int) -> int|None:
     while reintentos > 0:
          valor = int(input(mensaje))
          if validate_number(valor,minimo,maximo):
               return valor
          else:
               print(mensaje_error)
          reintentos -= 1
     if reintentos == 0:
          return None

# Ejemplo de uso de get_in

# resultado = get_in("Introduce un número entre 1 y 10: ", "Número inválido, intenta de nuevo.", 1, 10, 3)

# if resultado != None:
#     print(f"Número válido ingresado: {resultado}")
# else:
#     print("No se pudo obtener un número válido.")

def get_float(mensaje:str, mensaje_error: str, minimo: int,maximo:int, reintentos: int) -> int|None:
     while reintentos > 0:
          valor = float(input(mensaje))
          if validate_number(valor,minimo,maximo):
               return valor
          else:
               print(mensaje_error)
          reintentos -= 1
     if reintentos == 0:
          return None

# Ejemplo de uso de get_float

# resultado2 = get_float("Introduce un número entre 0.5 y 10.5: ", "Número inválido, intenta de nuevo.", 0.5, 10.5, 3)
# if resultado2 != None:
#     print(f"Número válido ingresado: {resultado2}")
# else:
#     print("No se pudo obtener un número válido.")

# 2-Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud
# de la cadena ingresada dado el parámetro recibido.

def get_string(longitud: int) -> str|None:
     cadena = str(input("Introduce una cedena de caracteres: "))
     if validate_length(cadena,longitud):
          return cadena
     else:
          print("Error. La cadena tiene demasiados caracteres.")
          return None

# Ejemplo de uso de get_string

# resultado3 = get_string(5)
# if resultado3 != None:
#      print(f"Cadena de caracteres valida: {resultado3}")
# else:
#      print("Cadena de caracteres invalida.")


