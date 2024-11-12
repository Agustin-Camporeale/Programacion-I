jugadores = [
     {"Nombre": "Ana", "Edad": 43, "puntos":[10,12,14]},
     {"nombre": "Juan", "edad": 32, "puntos":[12,10,11]},
     {"nombre": "Pedro", "edad": 28, "puntos":[9,15,11]},
     {"nombre": "Sol", "edad": 31, "puntos":[11,8,15]}
]

# Determina el nombre del los jugadores con menos de 10 puntos

# Ordenar de manera ascendete los nombres

# Buscar el de menor de edad y mostrar su nombre

# Acumular los puntos de cada jugador

def ord_generico(lista:list, clave:str, orden:int):
     """Ordena una lista de diccionario por la clave solicitada con el criterio de ord pasado por parametro
     Param : lista es la lista a ordenar
     Param : clave es la key del diccionario por la cual voy a ordenar
     Param : ascendente 1 / descendente -1
     """
     for i in range(len(lista)-1):
          for j in range(i, len(lista)):
               if orden == 1 and lista[i][clave] > lista[j][clave]:
                    intercambiar(lista,i,j)
               if orden == -1 and lista[i][clave] < lista[j][clave]:
                    intercambiar(lista,i,j)

def intercambiar(lista:list, pos1:int, pos2:int):
     aux = lista[pos1]
     lista[pos1] = lista[pos2]
     lista[pos2] = aux