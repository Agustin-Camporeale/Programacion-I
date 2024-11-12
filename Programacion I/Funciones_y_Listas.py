""" Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los guarde en una lista y la retorne. El programa principal debe 
invocar a la función y mostrar por pantalla el retorno. """

def pedir_nombres():
     nombres_contador = 0
     lista_nombres = []
     while nombres_contador < 10:
          nombres = input("Ingrese los nombres: ")
          lista_nombres.append(nombres)
          nombres_contador += 1
     return lista_nombres

print(pedir_nombre())

""" Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida posición y número a guardar al usuario, lo guarde en una lista en la posición
solicitada aleatoriamente y la retorne. El programa principal debe invocar a la función y mostrar por pantalla el retorno """

import random
def numeros():
     lista = [0] * 10
     numero = int(input("Ingrese un número: "))
     pos = random.randint(0,9)
     lista[pos] = numero
     return lista

print(numeros())

""" Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango especificado, validar los números solicitados dentro de ese rango, guardar en una
lista y retornarla. El programa principal debe invocar a la función y mostrar por pantalla el retorno. """

def rango():
     minimo = 5
     maximo = 20
     contador = 0
     lista_numeros = []
     while contador < 10:
          numero = int(input("Ingrese un numero(entre 5 y 20): "))
          lista_numeros.append(numero)
          while numero < 5 or numero > 20:
               numero = int(input("Ese numero no se encuentra en el rango(5,20), vuelva a ingresar un numero: "))
          contador += 1
     return lista_numeros

print(rango())

"""Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números y un número especificado. 
La misma debe buscar el número especificado en la lista y retornar “True” si existe."""

def lista_num(lista_numeros:list, numero:int) -> bool:
     for numeros in lista_numeros:
          if numeros == numero:
               return True

lista_numeros = [4,5,15,17,35,27]
print(lista_num(lista_numeros,17))

"""Ejercicio 5: Dadas las siguientes listas:Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria",
"Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que reciba por parámetro la lista de edades, busque a las personas de menor edad (puede ser más de una) y las retorne. 
El programa principal deberá mostrar nombre y edad de los menores. """

def lista_x(lista_edades:list):
     menor_edad = lista_edades[0]
     for edad in lista_edades:
          if edad < menor_edad:
               menor_edad = edad
     indices_menores = []
     for i in range(len(lista_edades)):
          if lista_edades[i] == menor_edad:
               indices_menores.append(i)
     return indices_menores

Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
indices_menores = lista_x(edades)
print("Personas con la menor edad:")
for indice in indices_menores:
    print(f"{Nombres[indice]} tiene {edades[indice]} años")

"""Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo
listas_personas.py. Importar los nombres a una lista. Realizar una función que muestre los mismos. """

from listas_personas import nombres

for i in range(len(nombres)):
     print(nombres[i])

def mostrar(nombres: list):
     lista_nombres = []
     lista_nombres = nombres
     print(lista_nombres)

print(mostrar(nombres))

""" Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de compras on-line 
recientemente lanzado al mercado para ello necesita un programa que le permita acceder a los datos relevados.
Realizar una función con el siguiente Menú de Opciones:
1-Importar listas
2-Listar los datos de los usuarios de México
3-Listar los nombre, mail y teléfono de los usuarios de Brasil
4-Listar los datos del/los usuario/s más joven/es
5-Obtener un promedio de edad de los usuarios
6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años. """

def menu():
     input("""   INICIANDO...
     1-Importar listas
     2-Listar los datos de los usuarios de México
     3-Listar los nombre, mail y teléfono de los usuarios de Brasil
     4-Listar los datos del/los usuario/s más joven/es
     5-Obtener un promedio de edad de los usuarios
     6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
     7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
     8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
     Seleccione una opcion: """)

print(menu())