# Realizar una funcion que reciba una lista(de num de 1 a 9)y un int y retorne un int.
# La funcion debe retornar la cantidad de veces que encuentra el numero pasado por parametro en la lista
# El int que se pasa por parametro para buscar en la lista se le debe solicitar al usuario[validar entre 1 y 9 inclusive]
# [NOTA] : No se pueden utilizar funciones propias

# def encontrar(lista:list, numero:int) -> int:
#      contador = 0
#      for i in range(len(lista)):
#           if lista[i] == numero:
#                contador += 1
#      return contador

# lista_test = [1,4,5,6,2,1,6,7,8,9,4]
# numero = int(input("Ingrese un numero a buscar en la lista del 1 al 9: "))
# while numero < 1 or numero > 9:
#      numero = int(input("ERROR, Vuelva a ingresar el numero(1 a 9): "))
# print(encontrar(lista_test,numero))

nombres = ["Ana","Luis","Juan","Sol","Roberto"]
mascotas = [["boby","michi"],"kuki","gati","pupy",["toto","coca"]]

print("Cliente:", nombres[4], "y su mascota:",mascotas[4][1])

# bandera = True
# for i in range(1,5):
#      numero = int(input("Ingrese un numero:"))
#      if bandera or numero > mayor:
#           mayor = numero

# print("El numero mayor ingresado es", mayor)

def mostrar(valor:int):
     print(valor)

lista = [10,20,30,40,50,60]
for i in range(len(lista)):
     mostrar(i)