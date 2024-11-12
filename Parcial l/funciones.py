def cargar_pacientes(lista):
     """Permite al usuario ingresar los datos de los pacientes"""
     cargar = "s"
     while cargar == "s":
          num_historia = int(input("Ingrese el número de historia clinica del paciente: "))
          nombre = str(input("Ingrese el nombre del paciente: "))
          edad = int(input("Ingrese la edad del paciente: "))
          diagnostico = str(input("Ingrese el diagnostico: "))
          cant_dias = int(input("Ingrese la cantidad de dias de internacion: "))
          datos = [num_historia, nombre, edad, diagnostico, cant_dias]
          for i in range(len(lista)):
               if lista[i] == []:
                    lista[i] = datos
                    break          
          cargar = str(input("¿Desea seguir cargando datos?(s/n)")).lower()

     for i in range(len(lista)):
          print(lista[i])

def mostrar_datos(lista):
     """Muestra la lista con los datos de los pacientes"""
     for i in range(len(lista)):
          if lista[i] == []:
               print("No se cargaron datos aún")
               break
          elif lista[i] != []:
               print(lista[i], i+1)
