def swap(lista:list, pos1:int, pos2:int):
    aux = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = aux

def ordenar(lista:list, clave:str, orden:int):
    for i in range(len(lista)-1):
            for j in range(i, len(lista)):
                if orden == 1 and lista[i][clave] > lista[j][clave]:
                    swap(lista,i,j)
                if orden == -1 and lista[i][clave] < lista[j][clave]:
                    swap(lista,i,j)
                if lista[i][clave] == lista[j][clave]:
                    clave = "nombre"
                    swap(lista,i,j)
    return lista

def obtener_grupo(datos:list, grupo:str) -> list:
    lista = []
    for i in range(len(datos)):
        if 'grupos' in datos[i]:
            for j in range(len(datos[i]["grupos"])):
                if datos[i]["grupos"][j]["nombre"] == grupo:
                    lista.append(datos[i])
    return lista

def buscar_jovenes(data:list) -> list:
    menores = [data[0]]
    edad_menor = data[0]["edad"]
    for i in range(len(data)):
        if data[i]["edad"] < edad_menor:
            menores = [data[i]]
            edad_menor = data[i]["edad"]
        elif data[i]["edad"] == edad_menor and i > 0:
            menores.append(data[i])
    return(menores)