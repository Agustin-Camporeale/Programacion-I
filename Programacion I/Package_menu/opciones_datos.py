from listas_personas import *

def lista_mex(country,nombres,telefonos,mails,address,postalZip,region,edades):
     for i in range(len(country)):
          if country[i] == "Mexico":
               print(nombres[i],edades[i],country[i],telefonos[i],mails[i],address[i],postalZip[i],region[i])

def lista_bra(country,nombres,telefonos,mails):
     for i in range(len(country)):
          if country[i] == "Brazil":
               print(nombres[i],telefonos[i],mails[i])

def lista_menores(country,nombres,telefonos,mails,address,postalZip,region,edades):
     menor_edad = edades[0]
     for i in range(len(edades)):
          if edades[i] <= menor_edad:
               print(nombres[i],edades[i],country[i],telefonos[i],mails[i],address[i],postalZip[i],region[i])

def promedio_usuarios(edades):
     suma = 0
     for i in range(len(edades)):
          suma += edades[i]
     promedio = suma / len(edades)
     print(promedio)

def lista_bra_mayor(country,edades,nombres,telefonos,mails,address,postalZip,region):
     mayor_edad = edades[0]
     for i in range(len(edades)):
          if country[i] == "Brazil" and (edades[i] >= mayor_edad):
               print(nombres[i],edades[i],country[i],telefonos[i],mails[i],address[i],postalZip[i],region[i])


def lista_datos_mex_bra(country,edades,nombres,telefonos,mails,address,postalZip,region):
     for i in range(len(country)):
          if (country[i] == "Brazil" or country[i] == "Mexico") and postalZip[i] > 8000:
               print(nombres[i],edades[i],country[i],telefonos[i],mails[i],address[i],postalZip[i],region[i])

def lista_ita(nombres,mails,telefonos,country):
     for i in range(len(country)):
          if country[i] == "Italy" and edades[i] > 40:
               print(nombres[i],mails[i],telefonos[i])

def lista_mex_ordenados(country,nombres,telefonos,mails,address,postalZip,region,edades):
     for i in range(len(nombres)-1):
          for j in range(i+1, len(nombres)):
               if nombres[i] > nombres[j] and country[i] == "Mexico":
                    aux = nombres[j]
                    nombres[j] = nombres[i]
                    nombres[i] = aux
                    print(nombres[i],edades[i],country[i],telefonos[i],mails[i],address[i],postalZip[i],region[i])

def lista_ord_edad(country,nombres,telefonos,mails,address,postalZip,region,edades):
     for i in range(len(edades)-1):
          for j in range(i+1, len(edades)):
               if edades[i] > edades[j]:
                    aux = edades[j]
                    edades[j] = edades[i]
                    edades[i] = aux
               if edades[j] == edades[i]:
                    if nombres[i] > nombres[j]:
                         aux = nombres[j]
                         nombres[j] = nombres[i]
                         nombres[i] = aux
          print(nombres[i],edades[i],country[i],telefonos[i],mails[i],address[i],postalZip[i],region[i])

def lista_ord_mex_bra(country,nombres,telefonos,mails,address,postalZip,region,edades):
     posicion = []
     for i in range(len(country)):
          if country[i] == "Brazil" or country[i] == "Mexico" and int(postalZip[i]) > 8000:
               posicion.append(i)
               for j in range(len(posicion)):
                    for k in range(len(posicion)):
                         if nombres[posicion[j]] < nombres[posicion[k]]:
                              aux = nombres[j]
                              nombres[k] = nombres[j]
                              nombres[j] = aux
                         elif nombres[posicion[j]] == nombres[posicion[k]]:
                              if edades[posicion[j]] < edades[posicion[k]]:
                                   aux = edades[j]
                                   edades[k] = edades[j]
                                   edades[j] = aux
               print(nombres[i],edades[i],country[i],telefonos[i],mails[i],address[i],postalZip[i],region[i])

