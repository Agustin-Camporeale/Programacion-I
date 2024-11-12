# Modelo de parcial 1:
'''
Nombre: Agustin
Apellido: Camporeale
DNI: 463501454

Una distribuidora de bebidas llena 10 comiones con sus productos y necesita guardar ciertos datos de cada una:

-Nombre del conductor
-Cantidad de litros de agua transportada($300 el litro)
-Cantidad de litros de gaseosa transportada ($600 el litro)
-Cantidad de litros de cerveza transportada ($800 el litro)
-Cantidad de litros de vino transportada ($1000 el litro)

1-Informar el promedio de litros totales por camion.
2-Debemos mostrar que tipo de bebida se transportó en mayor cantidad (cerveza, agua, gaseosa o vino).
3-Si la empresa supera la facturación de 700000 pesos deberá pagar un 15% de impuesto a las ganancias. Informar si lo paga y de ser así el monto del impuesto.
4-Informar el porcentaje de agua transportada y de gaseosa transportada en relación al total de litros transportados.
5-Informar el primer ingreso (camion) que transporte mas de 100 litros.
6-Nombre del conductor y cantidad de litros del camion que más transportó.
7-Nombre del conductor y cantidad de litros del camion que menos transportó.
'''

'''

Una distribuidora de bebidas llena 10 comiones con sus productos y necesita guardar ciertos datos de cada una:

-Nombre del conductor
-Cantidad de litros de agua transportada($300 el litro)
-Cantidad de litros de gaseosa transportada ($600 el litro)
-Cantidad de litros de cerveza transportada ($800 el litro)
-Cantidad de litros de vino transportada ($1000 el litro)

1-Informar el promedio de litros totales por camion.
2-Debemos mostrar que tipo de bebida se transportó en mayor cantidad (cerveza, agua, gaseosa o vino).
3-Si la empresa supera la facturación de 700000 pesos deberá pagar un 15% de impuesto a las ganancias. Informar si lo paga y de ser así el monto del impuesto.
4-Informar el porcentaje de agua transportada y de gaseosa transportada en relación al total de litros transportados.
5-Informar el primer ingreso (camion) que transporte mas de 100 litros.
6-Nombre del conductor y cantidad de litros del camion que más transportó.
7-Nombre del conductor y cantidad de litros del camion que menos transportó.
'''

cant_camiones = 0
litros_camion = 0
contador_agua = 0
contador_gaseosa = 0
contador_cerveza = 0
contador_vino = 0
mayor_bebida = ""
camion_transporte = 0
bandera_max = False
bandera_min = False
litros_max = 0
litros_camion_max = 0
nombre_max = ""
litros_min = 0
nombre_min = ""
primer_camion_100 = False

while cant_camiones < 10:
    nombre = input("Diganos su nombre: ")
    agua = float(input("Cuantos litros de agua lleva: "))
    while agua < 0:
        agua = float(input("ERROR. Los litros no pueden ser menor que 0. Cuantos litros de agua lleva: "))
    gaseosa = float(input("Cuantos litros de gaseosa lleva: "))
    while gaseosa < 0:
        gaseosa = float(input("ERROR. Los litros no pueden ser menor que 0. Cuantos litros de gaseosa lleva: "))
    cerveza = float(input("Cuantos litros de cerveza lleva: "))
    while cerveza < 0:
        cerveza = float(input("ERROR. Los litros no pueden ser menor que 0. Cuantos litros de cerveza lleva: "))
    vino = float(input("Cuantos litros de vino lleva: "))
    while vino < 0:
        vino = float(input("ERROR. Los litros no pueden ser menor que 0. Cuantos litros de vino lleva: "))

    litros_camion_max = agua + gaseosa + cerveza + vino

    if litros_camion_max > 100:
        if not primer_camion_100:
            nombre_camionero = nombre
            primer_camion_100 = True
            

    if bandera_max == False or litros_max < litros_camion_max:
        litros_max = litros_camion
        nombre_max = nombre
        bandera_max = True
    if bandera_min == False or litros_min > litros_camion_max:
        litros_min = litros_camion
        nombre_min = nombre
        bandera_min = True  
    litros_camion += agua + gaseosa + cerveza + vino


    cant_camiones += 1
    contador_agua += agua
    contador_gaseosa += gaseosa
    contador_cerveza += cerveza
    contador_vino += vino

if contador_agua > contador_gaseosa and contador_agua > contador_cerveza and contador_agua > contador_vino:
     mayor_bebida = "Agua"
elif contador_gaseosa > contador_cerveza and contador_gaseosa > contador_vino:
    mayor_bebida = "Gaseosa"
elif contador_cerveza > contador_vino:
    mayor_bebida = "Cerveza"
else:
    mayor_bebida = "vino"
total = litros_camion / cant_camiones




precio_agua = contador_agua * 300
precio_gaseosa = contador_gaseosa * 600
precio_cerveza = contador_cerveza * 800
precio_vino = contador_vino * 1000
precio = precio_agua + precio_gaseosa + precio_cerveza + precio_vino
if precio > 700.000:
    impuesto = precio * 0.15
    total_precio = impuesto + precio
    print(f"Usted debe pagar impuesto a las ganancias, su monto es ${precio}, el impuesto es {impuesto} y el total es ${total_precio}")
else:
    print(f"El total es {precio}")
porcentaje_agua = (contador_agua / litros_camion) * 100
porcentaje_gaseosa = (contador_gaseosa / litros_camion) * 100


print(f"El promedio de litros totales por camion es {total}")
print(f"La bebida que se transporto en mayor cantidad es {mayor_bebida}")
print(f"El porcentaje de agua en relacion al litros totales es {porcentaje_agua}")
print(f"El porcentaje de gaseosa en relacion al litros totales es {porcentaje_gaseosa}")
print(f"el camion que transporto los primeros 100 litros es: {nombre_camionero}")
print(f"El conductor con menos es {nombre_min} y la cantidad de litros es {litros_min}")
print(f"El conductor con mas es {nombre_max} y la cantidad de litros es {litros_max}")

