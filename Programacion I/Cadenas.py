# Ejercicio 1: Desarrollar una función que Invierte el orden de los caracteres en una cadena.

def invertir_cadena(cadena):
     for i in range(len(cadena)):
          cadena_inv = cadena[::-1]
     return cadena_inv

print(invertir_cadena("Hola mundo"))

# Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena.

def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

# cadena = input("Introduce una cadena de texto: ")
# cant_palabras = contar_palabras(cadena)
# print(f"Cantidad de palabras en la cadena: {cant_palabras}")

# Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra en una cadena.

def reemplazar(cadena, palabra1, palabra2):
    # Usar el método replace() para reemplazar la palabra
    cadena_mod = cadena.replace(palabra1, palabra2)
    return cadena_mod

# Programa principal
# cadena = input("Introduce una cadena de texto: ")
# palabra1 = input("Introduce la palabra que deseas reemplazar: ")
# palabra2 = input("Introduce la nueva palabra: ")
# cadena_mod = reemplazar(cadena, palabra1, palabra2)
# print("Cadena modificada:", cadena_mod)

# Ejercicio 4: Desarrollar una función que convierta los elementos de lista_peli en una cadena y muestre: 

def lista_convertir(lista:list):
     separador = ", "
     for peliculas in lista:
          cadena = separador.join(peliculas)
          print("Se recomienda ver", cadena)

lista_peli = [
     ["Matrix", "El Padrino", "Titanic"],
     ["Forrest Gump", "Pulp Fiction", "Gladiador"],
     ["Blade Runner", "El Rey León", "Volver al Futuro"],
     ["La La Land", "El Gran Lebowski", "Blade Runner"],
     ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
     ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
     ["Titanic", "Star Wars", "El Señor de los Anillos"],
     ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
     ["Forrest Gump", "The Godfather", "Goodfellas"],
     ["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]

# lista_convertir(lista_peli)

# Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena.

def cad_capitalizar(cad:str):
     cad = cad.capitalize()
     return cad

# print(cad_capitalizar("bienvenidos"))

# Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo

def es_palindromo(cadena:str):
     if cadena[::-1] == cadena[0:]:
          print("La cadena de caracteres es un Palíndromo")
     else:
          print("La cadena de caracteres NO es un Palíndromo")

es_palindromo("ana")

# Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número (1 o -1). 
# Se debe retornar el string ordenado de manera ascendente (si recibió 1 por parámetros) o descendente (si recibió -1)

def ordenar(cad:str, num:int):
     for i in range(len(cad)-1):
          for j in range(i, len(cad)):
               if num == 1 and cad[i] > cad[j]:
                    intercambiar(cad,i,j)
               if num == -1 and cad[i] < cad[j]:
                    intercambiar(cad,i,j)
     return cad

def intercambiar(lista:list, pos1:int, pos2:int):
     aux = lista[pos1]
     lista[pos1] = lista[pos2]
     lista[pos2] = aux

elementos = ["me","gusta","las","peliculas","de","accion"]
print(ordenar(elementos,1))