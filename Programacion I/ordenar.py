# lista = [6,7,8,5]

# for i in range(len(lista)):
#      print(lista[i])

#  Ordenamiento de burbujeo
# for i in range(len(lista)-1):
#      for j in range(i+1, len(lista)):
#           if lista[i] > lista[j]:
#                aux = lista[i]
#                lista[i] = lista[j]
#                lista[j]= aux

# print("")

# for i in range(len(lista)):
#      print(lista[i])

x = 6
print("El numero x es %d"%x)

for i in range(0,11):
     texto = "iteracion %i"%i
     print("El numero i es %d %s"%(i,texto))

# burbujeo eficiente
bandera_swap = True

while bandera_swap:
     bandera_swap = False
     for i in range(len(jugadores)-1):
          if jugadores[i]["nombre"] < jugadores[i+1]["nombre"]
          aux = jugadores[i]
          jugadores[i] = jugadores[i+1]
          jugadores[i+1] = aux
          bandera_swap = True

print("Ordenado")
for e_jugador in jugadores:
     print(e_jugador)
