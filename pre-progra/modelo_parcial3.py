''' Debemos realizar la carga de una compra de 5(cinco) productos de desinfección
de cada una debo obtener los siguientes datos:
-el nombre del producto 
-el tipo de producto (validar "ALCOHOL", "IAC" o "QUAT"),
-el precio (validar entre 100 y 300),
-la cantidad de unidades (no puede ser 0 o negativo y no debe superar las 1000 unidades),
-el tipo de inflamable("ignifugo", "combustible", "explosivo" ) 
-y la Marca.
Se debe Informar al usuario lo siguiente:
a) El promedio de cantidad por tipo de producto
b) El tipo de inflamable con más cantidad de unidades en total de la compra
c) Cuántas unidades de IAC con precios menos a 200 (inclusive) se compraron en total
d) La marca y tipo del más caro de los productos
'''
PRECIO_MINIMO = 100
PRECIO_MAXIMO = 300
CANTIDAD_MINIMA = 0
CANTIDAD_MAXIMA = 1000
contador = 0
#acumulador_cantidad = 0
acumulador_alcohol = 0
acumulador_iac = 0
acumulador_quat = 0
contador_alcohol = 0
contador_iac = 0
contador_quat = 0
promedio_cantidad_alcohol = 0
promedio_cantidad_iac = 0
promedio_cantidad_quat = 0
#maximo_inflamable = 0
acumulador_ignifugo = 0
acumulador_combustible = 0
acumulador_explosivo = 0
acumulador_iac_precio = 0

while contador < 5:
    nombre_producto = input("Ingrese nombre del producto: ")
    tipo_de_producto = (input("¿Que tipo de producto es? ALCOHOL, IAC  o QUAT: "))
    while tipo_de_producto!= "ALCHOL" and tipo_de_producto != "IAC" and tipo_de_producto != "QUAT":
        tipo_de_producto = input("Entrada invalida. ¿Que tipo de producto es? ALCOHOL, IAC  o QUAT: ")
    precio = float(input("Ingrese el precio (mas de 100 y menos de 300): "))
    while precio <= PRECIO_MINIMO or precio >= PRECIO_MAXIMO:
        precio = float(input("Precio no valido. Ingrese el precio (mas de 100 y menos de 300) "))
    cantidad = int(input("Ingrese cantidad comprada (mas de 0 y menos de 1000): "))
    while cantidad <= CANTIDAD_MINIMA or cantidad >= CANTIDAD_MAXIMA:
        cantidad = int(input("Cantidad no valida. Ingrese la cantidad comprada (mas de 0 y menos de 1000): "))
    tipo_inflamable = input("Igresese la caracteristica del producto: ignifugo, combustible o explosivo ")
    while tipo_inflamable != "ignifugo" and tipo_inflamable != "combustible" and tipo_inflamable != "explosivo":
        tipo_inflamable = input("Ingreso no valido. Igresese la caracteristica del producto: ignifugo, combustible o explosivo ")
    marca = input("Ingrese la marca del producto: ")
    
    contador += 1
    
    if tipo_de_producto == "ALCHOL":
        acumulador_alcohol += cantidad
        contador_alcohol += 1
    elif tipo_de_producto == "IAC":
        acumulador_iac += cantidad
        contador_iac += 1
        if precio <= 200:
            acumulador_iac_precio += cantidad
    else:
        acumulador_quat += cantidad
        contador_quat += 1
    
    if tipo_inflamable == "ignifugo":
        acumulador_ignifugo += cantidad
    elif tipo_inflamable == "combustible":
        acumulador_combustible += cantidad
    else:
        acumulador_explosivo += cantidad



promedio_cantidad_alcohol = acumulador_alcohol / contador_alcohol
promedio_cantidad_iac = acumulador_iac / contador_iac
promedio_cantidad_quat = acumulador_quat / contador_quat

if promedio_cantidad_alcohol != 0:
    print("El promedio de cantidad del ALCOHOL fue de:", promedio_cantidad_alcohol)
if promedio_cantidad_iac != 0:
    print("El promedio de cantidad del IAC fue de:", promedio_cantidad_iac)
if promedio_cantidad_quat != 0:
    print("El promedio de cantidad del QUAT fue de:", promedio_cantidad_quat)

if acumulador_ignifugo > acumulador_combustible and acumulador_ignifugo > acumulador_explosivo:
    print("El tipo de inflamable con más cantidad de unidades en total de la compra es el IGNIFUGO")
elif acumulador_combustible > acumulador_explosivo:
    print("El tipo de inflamable con más cantidad de unidades en total de la compra es el COMBUSTIBLE")
else:
    print("El tipo de inflamable con más cantidad de unidades en total de la compra es el EXPLOSIVO")

print("Se compraron", acumulador_iac_precio,"unidades de de IAC con precio menor a 200 (inclusive)")
