"""Ejercicio 1:Dadas las siguientes listas:"""
nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenar_datos1(lista_nombres:list, lista_edades:list):
     for i in range(len(lista_nombres)-1):
          for j in range(i+1, len(lista_nombres)):
               if lista_nombres[j] < lista_nombres[i]:
                    aux = lista_nombres[j]
                    lista_nombres[j] = lista_nombres[i]
                    lista_nombres[i] = aux
                    aux = lista_edades[j]
                    lista_edades[j] = lista_edades[i]
                    lista_edades[i] = aux

# ordenar_datos1(nombres,edades)
# for i in range(len(nombres)):
#     print(f"{nombres[i]}  y su edad es  {edades[i]")

"""Ejercicio 2:Dadas las siguientes listas:"""
nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias","Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos","Base de Datos", "Ergonomia", "Naturaleza"]
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_datos2(lista_nombres:list,lista_puntos:list):
     for i in range(len(lista_nombres)-1):
          for j in range(i+1, len(lista_nombres)):
               if lista_nombres[j] < lista_nombres[i]:
                    aux = lista_nombres[j]
                    lista_nombres[j] = lista_nombres[i]
                    lista_nombres[i] = aux
               if lista_nombres[j] == lista_nombres[i]:
                    if lista_puntos[j] > lista_puntos[i]:
                         aux = lista_puntos[j]
                         lista_puntos[j] = lista_puntos[i]
                         lista_puntos[i] = aux

# ordenar_datos2(nombres,puntos)
# for i in range(len(nombres)):
#     print(f"Nombre:{nombres[i]}   Puntos:{puntos[i]}")

"""Ejercicio 3: Dadas las siguientes listas:"""
estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_datos3(lista_estudiantes:list, lista_apellidos:list, lista_notas:list):
     for i in range(len(lista_estudiantes)-1):
          for j in range(i+1, len(lista_estudiantes)):
               if lista_estudiantes[j] < lista_estudiantes[i]:
                    aux = lista_estudiantes[j]
                    lista_estudiantes[j] = lista_estudiantes[i]
                    lista_estudiantes[i] = aux
                    aux = lista_apellidos[j]
                    lista_apellidos[j] = lista_apellidos[i]
                    lista_apellidos[i] = aux
                    aux = lista_notas[j]
                    lista_notas[j] = lista_notas[i]
                    lista_notas[i] = aux
               if lista_estudiantes[j] == lista_estudiantes[i]:
                    if lista_apellidos[j] < lista_apellidos[i]:
                         aux = lista_estudiantes[j]
                         lista_estudiantes[j] = lista_estudiantes[i]
                         lista_estudiantes[i] = aux
                         aux = lista_apellidos[j]
                         lista_apellidos[j] = lista_apellidos[i]
                         lista_apellidos[i] = aux
                         aux = lista_notas[j]
                         lista_notas[j] = lista_notas[i]
                         lista_notas[i] = aux
               if lista_apellidos[j] == lista_apellidos[i]:
                    if lista_notas[j] > lista_notas[i]:
                         aux = lista_estudiantes[j]
                         lista_estudiantes[j] = lista_estudiantes[i]
                         lista_estudiantes[i] = aux
                         aux = lista_apellidos[j]
                         lista_apellidos[j] = lista_apellidos[i]
                         lista_apellidos[i] = aux
                         aux = lista_notas[j]
                         lista_notas[j] = lista_notas[i]
                         lista_notas[i] = aux

# ordenar_datos3(apellidos, estudiantes, nota)
# for i in range(len(apellidos)):
#     print(f'Apellido:{apellidos[i]}    Nombre:{estudiantes[i]}    Nota:{nota[i]:} ')

"""Ejercicio 4:Una startup desea analizar las estadísticas de los usuarios de su sitio de
compras on-line recientemente lanzado al mercado para ello necesita un programa
que le permita acceder a los datos relevados."""
