from estudiantes import *
from Diccionarios_op import *

def menu():
     continuar = "s"
     while continuar == "s":
          opcion = int(input("""INICIANDO...
          1-Listar los alumnos por orden ascendente de apellido, si se repite,ordenar por nombre. Mostrar legajo, nombre, apellido y edad
          2-Obtener el promedio de notas para cada estudiante
          3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica”
          4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y apellido
          5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido
          6-Listar nombre y apellido de los alumnos que forman el grupo “Club de Informática” con sus respectivos promedios
          7-Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes.
          Seleccione una opcion: """))
          if opcion == 1:
               alumnos_orden_as(estudiantes)
               continuar = str(input("¿Desea volver al menú?(s/n): ")).lower()
               while continuar != "s" and continuar != "n":
                    continuar = str(input("Opcion incorrecta, vuelva a intentarlo: "))
          elif opcion == 2:
               promedio_notas(estudiantes)
               continuar = str(input("¿Desea volver al menú?(s/n): ")).lower()
               while continuar != "s" and continuar != "n":
                    continuar = str(input("Opcion incorrecta, vuelva a intentarlo: "))
          elif opcion == 3:
               listar_alumnos_ing(estudiantes)
               continuar = str(input("¿Desea volver al menú?(s/n): ")).lower()
               while continuar != "s" and continuar != "n":
                    continuar = str(input("Opcion incorrecta, vuelva a intentarlo: "))
          elif opcion == 4:
               promedio_edad(estudiantes)
               continuar = str(input("¿Desea volver al menú?(s/n): ")).lower()
               while continuar != "s" and continuar != "n":
                    continuar = str(input("Opcion incorrecta, vuelva a intentarlo: "))
          elif opcion == 5:
               mayor_promedio(estudiantes)
               continuar = str(input("¿Desea volver al menú?(s/n): ")).lower()
               while continuar != "s" and continuar != "n":
                    continuar = str(input("Opcion incorrecta, vuelva a intentarlo: "))
          elif opcion == 6:
               

menu()