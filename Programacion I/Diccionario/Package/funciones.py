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