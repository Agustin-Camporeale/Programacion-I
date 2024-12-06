import random

lista = [
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]}
]

def generar_numeros(lista:list, clave:str):
    for i in range(len(lista)):
        for j in range(1,8):
            numeros = random.randint(1,3)
            lista[i][clave].append(numeros)

def mostrar(dic:dict, clave:str):
    for i in range(len(lista)):
        print(dic[i][clave])

def candy_crush(lista:list):
    generar_numeros(lista,"piezas")
    nombre = input("Ingrese su usuario(mínimo de 5 caracteres, puede incluir numeros): ")
    while nombre.isdigit() or len(nombre) < 5:
        nombre = str(input("--- ERROR ---\nIngrese su usuario(mínimo de 5 caracteres): "))
    mostrar(lista,"piezas")
    fila = int(input("Ingrese la fila: "))
    while fila < 0 or fila > 3:
        fila = int(input("ERROR... Ingrese la fila(0 a 3): "))
    columna = int(input("Ingrese la columna: "))
    while columna < 0 or columna > 6:
        columna = int(input("ERROR... Ingrese la columna(0 a 6): "))
    contador = 0
    puntos = 0
    for i in range(len(lista)-1):
        if fila == 0 and lista[fila]["piezas"][columna] == lista[i]["piezas"][columna]: #Compara el primer numero de la columna con los 3 primeros
            contador += 1
        elif fila == 1 and (lista[fila]["piezas"][columna] == lista[i + 1]["piezas"][columna]) or (lista[fila]["piezas"][columna] == lista[i]["piezas"][columna]): #Compara el segundo numero de la columna con las filas de abajo y con los 3 primeros 
            contador += 1
        elif fila == 2 and (lista[fila]["piezas"][columna] == lista[i + 1]["piezas"][columna]) or (lista[fila]["piezas"][columna] == lista[i]["piezas"][columna]): #Compara el tercer numero de la columna con los ultimos 3 numeros y con los 3 primeros
            contador += 1
        elif fila == 3 and (lista[fila]["piezas"][columna] == lista[i + 1]["piezas"][columna]): #Compara el cuarto numero de la columna con los ultimos 3
            contador += 1 
    if contador == 3:
        print("HA GANADO 10 PUNTOS")
        puntos += 10
    else:
        print("SEGUI PARTICIPANDO")
    jugadores = [nombre,puntos]
    return jugadores

def crear_archivo(nombre:str, lista:list):
    nombre += ".csv"
    with open(nombre, "a") as archivo: 
        archivo.write(f"{lista} \n")

lista = candy_crush(lista)
crear_archivo("Score", lista)
