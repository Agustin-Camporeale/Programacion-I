from Package.funciones import *

def alumnos_orden_as(alumnos:list):
    clave = "apellido"
    alumnos = ordenar(alumnos, clave, 1)

    for i in range(len(alumnos)):
        print("N° de legajo", alumnos[i]["legajo"])
        print("Nombre del alumno:", alumnos[i]["nombre"])
        print("Apellido del alumno:", alumnos[i]["apellido"])
        print("Edad del alumno", alumnos[i]["edad"])
        print("------------------------------------------------")

def promedio_notas(alumnos:list):
    cant_alumnos = 10
    suma = 0
    for i in range(len(alumnos)):
        notas = alumnos[i]["notas"]
        for e_notas in notas:
            suma += e_notas
    promedio = suma / cant_alumnos
    print("El promedio de nota de los estudiantes es", promedio)

def listar_alumnos_ing(alumnos:list):
    for i in range(len(alumnos)):
        programa = alumnos[i]["programa"]
        nombre_programa = programa["nombre"]
        if nombre_programa == "Ingenieria en Informatica":
            print("N° de legajo", alumnos[i]["legajo"])
            print("Nombre del alumno:", alumnos[i]["nombre"])
            print("Apellido del alumno:", alumnos[i]["apellido"])
            print("Edad del alumno", alumnos[i]["edad"])
            print("------------------------------------------------")
    
def promedio_edad(alumnos:list):
    cant_alumnos = 10
    suma = 0
    for i in range(len(alumnos)):
        print("Nombre del alumno:", alumnos[i]["nombre"])
        print("Apellido del alumno:", alumnos[i]["apellido"])
        print(" ------------------------------------------------ ")
        edad = alumnos[i]["edad"]
        suma += edad
    promedio = suma / cant_alumnos
    print("El promedio de edad de los estudiantes es", promedio) 

def mayor_promedio(alumnos:list):
    mayor = 0
    bandera = True
    pos = 0
    for i in range(len(alumnos)):
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
    



                      
