from funciones import *

def main():
    continuar = "s"
    leer = False
    while continuar == "s":
        print("")
        opcion = int(input("""    1. Leer archivo (con el inventario de productos)
    2. Buscar un producto (en el inventario)
    3. Ordenar el inventario (por precio o cantidad)
    4. Listar inventario (mostrar productos)
    5. Actualizar el inventario (cuando un producto se vende (disminuir su cantidad))
    6. Escribir un archivo (con el inventario actualizado)
    7. Salir
    \nSeleccione una opción: """))
        if opcion == 1:
            inventario = leer_archivo("inventario")
            print("\nArchivo leído con exito.")
            leer = True
        if opcion == 2 and leer == True:
            buscar_producto(inventario,"almedras")
        if opcion == 3 and leer == True:
            ordenar_inventario(inventario, "cantidad")
        if opcion == 4 and leer == True:
            listar_inventario(inventario)            
        if opcion == 5 and leer == True:
            actualizar_cantidad(inventario,"atun en lata", 100)
        if opcion == 6 and leer == True:
            escribir_archivo(inventario, "ventas")
        if opcion == 7:
            continuar = "n"
            leer = True
            print("Fin del programa.")
        if leer == False:
            print("\nNo se ha leido el archivo, Volviendo al menú...")
        while opcion > 7 or opcion < 1:
            opcion = int(input("Rango invalido, Vuelva a seleccionar una opción: "))
               
main()