from Package.funciones import *

def estudiantes_orden_as(estudiantes:list):
    clave = "apellido"
    estudiantes = ordenar(estudiantes, clave, 1)

    for i in range(len(estudiantes)):
        print("N° de legajo", estudiantes[i]["legajo"])
        print("Nombre del alumno:", estudiantes[i]["nombre"])
        print("Apellido del alumno:", estudiantes[i]["apellido"])
        print("Edad del alumno", estudiantes[i]["edad"])
        print("------------------------------------------------")

def promedio_notas(estudiantes:list):
    cant_estudiantes = 0
    suma = 0
    for i in range(len(estudiantes)):
        notas = estudiantes[i]["notas"]
        cant_estudiantes += 1
        for e_notas in notas:
            suma += e_notas
    promedio = suma / cant_estudiantes
    print("El promedio de nota de los estudiantes es", promedio)

def listar_estudiantes_ing(estudiantes:list):
    for i in range(len(estudiantes)):
        programa = estudiantes[i]["programa"]
        nombre_programa = programa["nombre"]
        if nombre_programa == "Ingenieria en Informatica":
            print("N° de legajo", estudiantes[i]["legajo"])
            print("Nombre del alumno:", estudiantes[i]["nombre"])
            print("Apellido del alumno:", estudiantes[i]["apellido"])
            print("Edad del alumno", estudiantes[i]["edad"])
            print("------------------------------------------------")
    
def promedio_edad(estudiantes:list):
    cant_estudiantes = 10
    suma = 0
    for i in range(len(estudiantes)):
        print("Nombre del alumno:", estudiantes[i]["nombre"])
        print("Apellido del alumno:", estudiantes[i]["apellido"])
        print(" ------------------------------------------------ ")
        edad = estudiantes[i]["edad"]
        suma += edad
    promedio = suma / cant_estudiantes
    print("El promedio de edad de los estudiantes es", promedio) 

def mayor_promedio(estudiantes:list):
    mayor = 0
    bandera = True
    pos = 0
    for i in range(len(estudiantes)):
        notas = alumnos[i]["notas"]
        notas_acumulador = 0
        for nota in notas:
            notas_acumulador += nota
        promedio = notas_acumulador / len(alumnos[i]["notas"])
        if promedio > mayor or bandera == False:
            mayor = promedio
            bandera = False
            posicion = i
    m_promedio = alumnos[posicion]
    print(f"El nombre y apellido del estudidante con mayor promedio es {m_promedio["nombre"]} {m_promedio["apellido"]}")

def int_club_informatica(estudiantes:list):
    estudiantes = obtener_grupo(estudiantes, "Club de Informatica")
    print("Integrantes del Club de informatica:")
    for i in range(len(estudiantes)):
        notas_acumulador = 0
        for nota in estudiantes[i]["notas"]:
            notas_acumulador += nota
        promedio = notas_acumulador / len(estudiantes[i]['notas'])
        print(f"{estudiantes[i]['nombre']} {estudiantes[i]['apellido']} con promedio de {promedio:.2f}")
    
def est_mas_jovenes(estudiantes:list):
    estudiantes_jovenes = buscar_jovenes(estudiantes)
    print(estudiantes_jovenes)
    for i in range(len(estudiantes_jovenes)):
        print("N° de legajo", estudiantes[i]["legajo"])
        print("Nombre del alumno:", estudiantes[i]["nombre"])
        print("Apellido del alumno:", estudiantes[i]["apellido"])
        print("El progrma que cursa:", estudiantes[i]["programa"]["nombre"])
                      
