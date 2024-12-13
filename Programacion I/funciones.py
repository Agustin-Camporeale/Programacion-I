def leer_archivo(nombre:str):
    """Lee archivos; recibe por parametros el nombre del archivo, lo lee y retorna una lista anidada"""
    nombre += ".csv"
    inventario = []
    with open(nombre, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            producto = [valores[0],float(valores[1]),valores[2]]
            inventario.append(producto)
    return inventario

def buscar_producto(inventario:list, nombre_producto:str):
    """Busca; recibe por parametro el nombre del producto y busca si existe en el inventario"""
    existe = False
    for i in range(len(inventario)):
        if inventario[i][0].lower() == nombre_producto.lower():
            pos = i
            existe = True
    if existe:
        print(f"El producto {nombre_producto} esta en el inventario. Hay {inventario[pos][2]} y su precio es de ${inventario[pos][1]}")
    else:
        print("Producto no encontrado.")

def ordenar_inventario(inventario:list, criterio:str):
    """Ordena; recibe por parametro un str q determina si lo ordena por precio o cantidad"""
    for i in range(len(inventario)-1): 
        for j in range(i + 1, len(inventario)):
            if criterio.lower() == "precio" and inventario[i][1] > inventario[j][1]:
                swap(inventario,i,j)    
            if criterio.lower() == "cantidad" and inventario[i][2] > inventario[j][2]:
                swap(inventario,i,j)   
    return inventario

def listar_inventario(inventario:list):
    """Muestra los elementos en forma de matriz"""
    print(f"{'Nombre':<40}{'Precio':<10}{'Cantidad':<10}")
    for productos in inventario:
        print(f"{productos[0]:<40}${productos[1]:<10.2f}{productos[2]:<15}")

def actualizar_cantidad(inventario:list, nombre_producto:str, cant_vendida:int):
    """Recibe por parametro un str(archivo) y actualiza la cantidad de un producto despues de una venta"""
    existe = False
    for i in range(len(inventario)):
        if inventario[i][0].lower() == nombre_producto.lower():
            pos = i
            cantidad = int(inventario[pos][2])
            existe = True
            if cantidad >= cant_vendida:
                inventario[i][2] = cantidad - cant_vendida
                print(f"Se vendieron {cant_vendida} unidades. Cantidad actualizada para '{nombre_producto}': {cantidad} unidades restantes.")
            else:
                print("Stock insufiente, no es posible vender.")
    if existe == False:
        print("Producto no encontrado.")
    
def escribir_archivo(inventario:list, archivo_nuevo:str):
    """Escribe en un nuevo archivos con los datos actualizados"""
    archivo_nuevo += ".csv"
    with open(archivo_nuevo, "w") as archivo:
        for productos in inventario:
            archivo.write(f"{productos[0]},{productos[1]},{productos[2]}\n")
    print(f"Inventario guardado en '{archivo_nuevo}'.")

def mappear_precios(inventario:list):
    """Incrementa los precios de todos los productos en un 10%"""
    for productos in inventario:
        productos[1] *= 1.10
    print("Precios incrementados en un 10%.")

# Funcion extra
def swap(lista:list, pos1:int, pos2:int):
    aux = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = aux
