def agregar_productos(productos:list):
     # Agrega productos a la gondola
     producto_nuevo = input("Ingrese el nombre del producto: ")
     cantidad = int(input("Ingrese la cantidad: "))
     fila = int(input("Ingrese la fila en donde estara el producto(1 a 3): "))
     while fila < 1 or fila > 3:
          fila = int(input("ERROR, vuelva a ingresar la fila(1 a 3) "))
     columna = int(input("Ingrese la columna en donde estara el producto(1 a 5): "))
     while columna < 1 or columna > 5:
          columna = int(input("ERROR, vuelva a ingresar la columna(1 a 5) "))
     producto = [producto_nuevo,cantidad,[fila,columna]]
     productos[fila - 1][columna - 1] = producto
     for i in range(len(productos)):
          print(productos[i])

def eliminar_productos(productos: list):
     # elimina productos de la gondola
     fila = int(input("Ingresa la fila del producto a quitar: "))
     while fila < 1 or fila > 3:
          fila = int(input("ERROR, vuelva a ingresar la fila(1 a 3) "))
     columna = int(input("Ingresa la columna del producto a quitar: "))
     while columna < 1 or columna > 5:
          columna = int(input("ERROR, vuelva a ingresar la columna(1 a 5) "))
     if len(productos[fila-1][columna-1]) != 0:
          productos[fila-1][columna-1] = []
          print("Producto eliminado correctamente")
     else:
          print(f"ERROR no se encuentran productos en Fila:{fila} / Columna:{columna}")
     if len(productos[fila-1][columna-1]) != 0:
          for i in range(len(productos)):
               print(productos[i])


def modificar_productos(productos: list):
     # modifica los datos de la gondola
     fila = int(input("Ingresa la fila del producto a modificar: "))
     while fila < 1 or fila > 3:
          fila = int(input("ERROR, vuelva a ingresar la fila(1 a 3) "))
     columna = int(input("Ingresa la columna del producto a modificar: "))
     while columna < 1 or columna > 5:
          columna = int(input("ERROR, vuelva a ingresar la columna(1 a 5) "))
     if len(productos[fila-1][columna-1]) != 0:
          print("1 - Modificar cantidad")
          print("2 - Modificar ubicación")
          opcion = int(input("Seleccione la opción: "))
          if opcion == 1:
               nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
               productos[fila-1][columna-1][1] = nueva_cantidad
          elif opcion == 2:
               nueva_fila = int(input("Ingrese la nueva fila del producto: "))
               nueva_columna = int(input("Ingrese la nueva columna del producto: "))
               productos[fila-1][columna-1][2] = [nueva_fila,nueva_columna]
          
     for i in range(len(productos)):
          print(productos[i])

def listar_productos(productos:list):
     # Muestra la lista de los productos que hay en la gondola
     print("\nLista de productos:")
     for i in range(len(productos)):
          if len(productos[0][i+1]) != 0:
               print(productos[0][i+1])
     for i in range(len(productos)):
          if len(productos[1][i+1]) != 0:
               print(productos[1][i+1])
     for i in range(len(productos)):
          if len(productos[2][i+1]) != 0:
               print(productos[2][i+1])

# Menú Ferreteria

def reponer(lista_estanteria,estanteria):
        lista_estanteria.append(estanteria)
        print("Estanteria repuesta")
        # return lista_estanteria
def vender(lista_estanteria,fila:int,columna:int,cantidad:int):
    if lista_estanteria == []:
        print("No hay articulos cargados")
    else:
        if lista_estanteria[0][fila][columna][1] > cantidad:
            lista_estanteria[0][fila][columna][1] -= cantidad
        else:
            print("No hay stock suficiente, no se puede realizar la venta")
def listar(lista_estanteria):
    if lista_estanteria == []:
        print("No hay articulos cargados")
    else:
        print("Productos:")
        for fila in lista_estanteria[0]:
            for columna in fila:
                print(f"{columna[0]}: {columna[1]} unidades")
