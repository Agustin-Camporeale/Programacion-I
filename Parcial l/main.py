from funciones import *

def main():
     pacientes = [[],
          [],
          [],
          [],
          [],
     ]
     continuar = "s"
     while continuar == "s":
          opcion = int(input("""Sistema de Gestión de clínica
          1. Cargar pacientes
          2. Mostrar todos los pacientes
          3. Buscar pacientes pot numero de historia clinica
          4. Ordenar paciente por numero de historia clinica
          5. Mostrar paciente con mas dias de internacion
          6. Mostrar pacientes con menos dias de internacion
          7. Cantidad de paciente con mas de 5 dias de internacion
          8. Promedio de dias de internacion de todos los pacientes
          9. Salir   
          Ingrese una opcion: """))
          if opcion == 1:
               cargar_pacientes(pacientes)
               continuar = "s"
          elif opcion == 2:
               mostrar_datos(pacientes)
               continuar = "s"
          elif opcion == 9:
               continuar = "n"

main()


