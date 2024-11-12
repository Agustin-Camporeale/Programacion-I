from opciones_datos import *
from listas_personas import *

def menu():
     continuar = "s"
     while continuar == "s":
          opcion = int(input("""INICIANDO...
          1-Importar listas
          2-Listar los datos de los usuarios de México
          3-Listar los nombres, mail y teléfono de los usuarios de Brasil
          4-Listar los datos del/los usuario/s más joven/es
          5-Obtener un promedio de edad de los usuarios
          6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
          7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
          8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
          9-Listar los datos de los usuarios de México ordenados por nombre
          10-Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente
          11-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente\nSeleccione una opción: """))
          if opcion == 1:
               nombres_c = nombres
               country_c = country
               telefonos_c = telefonos
               mails_c = mails
               address_c = address
               postalZip_c = postalZip
               region_c = region
               edades_c = edades
               print("Listas importadas")
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 2:
               print("Los datos de los usuarios de mexico son:\n")
               lista_mex(country_c,nombres_c,telefonos_c,mails_c,address_c,postalZip_c,region_c,edades_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 3:
               print("Los nombres,mails y telefono de los usuarios de Brasil son:\n")
               lista_bra(country_c,nombres_c,telefonos_c,mails_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 4:
               print("Los datos de los usuarios más jovenes son:\n")
               lista_menores(country_c,nombres_c,telefonos_c,mails_c,address_c,postalZip_c,region_c,edades_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 5:
               print("El promedio de edad de los usuarios es:\n")
               promedio_usuarios(edades_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 6:
               print("Los datos de los usuarios de Brasil de mayor edad son:\n")
               lista_bra_mayor(country_c,edades_c,nombres_c,telefonos_c,mails_c,address_c,postalZip_c,region_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 7:
               print("Los datos de los usuarios de Brasil y Mexico cuyo codigo postal es mayor a 8000 son:\n")
               lista_datos_mex_bra(country_c,edades,nombres_c,telefonos_c,mails_c,address_c,postalZip_c,region_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 8:
               print("Los nombres,mails y telefono de los usuarios de Italia mayores a 40 son:\n")
               lista_ita(nombres_c,mails_c,telefonos_c,country_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 9:
               print("Los datos de los usuarios de mexico son(ordenados por nombre):\n")
               lista_mex_ordenados(country_c,nombres_c,telefonos_c,mails_c,address_c,postalZip_c,region_c,edades_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 10:
               print("Los datos de los usuarios más jovenes son(ordenados de menor a mayor):\n")
               lista_ord_edad(country_c,nombres_c,telefonos_c,mails_c,address_c,postalZip_c,region_c,edades_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          elif opcion == 11:
               print("Los datos de los usuarios de Brasil y Mexico cuyo codigo postal es mayor a 8000 son:\n")
               lista_ord_mex_bra(country_c,nombres_c,telefonos_c,mails_c,address_c,postalZip_c,region_c,edades_c)
               continuar = input("\n¿Desea continuar(S/N): ").lower()
          else:
               continue
          while opcion > 11 or opcion < 1:
               opcion = int(input("ERROR, vuelva a seleccionar una opción: "))

menu()
