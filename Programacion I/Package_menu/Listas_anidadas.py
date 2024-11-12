from opciones_anidadas import *
from Package_Input.Input import get_in

gondola = [
          [[],[],[],[],[]],
          [[],[],[],[],[]],
          [[],[],[],[],[]]
]

# corchete violeta = fila , corchet azul = columna

gondola[0][1] = ["Botellas", 3, [1,2]]
gondola[0][3] = ["Frascos", 8, [1,4]]
gondola[1][2] = ["Fideos", 4, [2,3]]
gondola[2][3] = ["Leche", 6, [3,4]]

# for i in range(len(gondola)):
#      for j in range(len(gondola[i])):
#           print(gondola[i][j], end=" ")
#      print("")

def menu_almacen():
     continuar = "s"
     while continuar == "s":
          opcion = int(input("""
          1-Alta de productos (producto nuevo)
          2-Baja de productos (producto existente)
          3-Modificar productos (cantidad, ubicación)
          4-Listar productos
          5-Lista de productos ordenado por nombre
          6-Salir
          Ingrese una opción: """))
          while opcion < 1 or opcion > 6:
               opcion = int(input("ERROR, vuelva a ingresar una opcion(1 a 6): "))
          if opcion == 1:
               agregar_productos(gondola)
               continuar = str(input("¿Desea volver al menu?(s/n): ")).lower()
          elif opcion == 2:
               eliminar_productos(gondola)
               continuar = str(input("¿Desea volver al menu?(s/n): ")).lower()
          elif opcion == 3:
               modificar_productos(gondola)
               continuar = str(input("¿Desea volver al menu?(s/n): ")).lower()
          elif opcion == 4:
               listar_productos(gondola)
               continuar = str(input("¿Desea volver al menu?(s/n): ")).lower()
          elif opcion == 5:
               print("lista de productos ordenados por nombre:")
               continuar = str(input("¿Desea volver al menu?(s/n): ")).lower()
          elif opcion == 6:
               print("--- Saliendo ---")
               continuar = "n"

# menu_almacen()

def menu_ferreteria():
     estanteria = [
               [["to12", 65],["to16", 86],["to20",65],["to25",45]],
               [["to30", 68],["to35", 73],["to40", 85],["to35", 89]],
               [["ta4", 58],["ta5", 48],["ta6", 64],["ta7", 96]],
               [["ta8", 36],["ta10", 72],["ta12", 78],["ta14", 71]]
     ]
     lista_estanteria = []
     continuar = "s"
     while continuar == "s":
          print("Iniciando programa...")
          print("""
          1: Reponer mercaderia
          2: Vender mercaderia (seleccionar fila y columna) 
          3: Listar inventaria
          4: Salir
          """)
          opcion = int(input("Ingrese la opción: "))
          while opcion < 1 or opcion > 4:
               opcion = int(input("ERROR, vuelva a ingresar una opcion(1 a 4): "))
          if opcion == 1:
               reponer(lista_estanteria,estanteria)
               continuar = str(input("¿Desea volver al menu?(s/n): ")).lower()
          elif opcion == 2:
               fila = get_in("Ingrese fila: ", "ERORR, vuelva a ingersar:", 1, 2, 2)
               columna = get_in("Ingrese columna: ", "ERORR, vuelva a ingersar:", 1, 4, 2)
               cantidad = get_in("Ingrese cantidad: ", "ERORR, vuelva a ingersar:",0,100,2 )
               vender(lista_estanteria,fila,columna,cantidad)
               continuar = str(input("¿Desea volver al menu?(s/n): ")).lower()
          elif opcion == 3:
               listar(lista_estanteria)
               continuar = str(input("¿Desea volver al menu?(s/n): ")).lower()
          elif opcion == 4:
               print("--- Saliendo del programa ---")
               continuar = "n"

# menu_ferreteria()