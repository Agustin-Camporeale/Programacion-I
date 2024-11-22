bandera = True
for i in range(1,5):
     numero = int(input("Ingrese un numero: "))
     if bandera or numero > mayor:
          mayor = numero
          bandera = False

print("El numero mayor ingresado fue:", mayor)

nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto"]
telefonos = [["123","234"],"345",["567","525"],"891",["876","543"]]
print("Cliente:", nombres[2], "telefono:", telefonos[2][1])

def mostrar(valor:int):
     print(valor)

lista = [10,20,30,40,50,60]
for i in lista:
     mostrar(i)
   