opcion = "s"
contador = 0
cant_empleados_m = 0
empleados_ia = 0
bandera_mayor = False
empleado_mayor = 0
nombre_empleado_mayor = ""
tecnologia_empledo_mayor = ""
while opcion == "s":
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad(mayor a 18): "))
    while edad < 18 or edad > 99:
        edad = int(input("Error. Vuelva a ingresar su edad(mayor a 18): "))
    genero = input("Ingrese su género(Masculino - Femenino - Otro): ").lower()
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input("Error. Vuelva a ingresar su género: ")
    tecnologia = input("Ingrese su voto(IA - RV/RA - IOT)")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("Error. Vuelva a ingresar su voto: ")
    contador += 1
    if edad > 24 and edad < 51:
        if genero == "masculino" and (tecnologia == "IOT" or tecnologia == "IA"):
            cant_empleados_m += 1
            
    if genero != "femenino" or (edad < 33 and edad > 40):
        if tecnologia != "IA":
            empleados_ia += 1

    if genero == "masculino" and (bandera_mayor == False or edad > empleado_mayor):
        nombre_empleado_mayor = nombre
        tecnologia_empledo_mayor = tecnologia
        bandera_mayor = True

    opcion = input("¿Desea ingresar mas datos?(s/n):").lower()
    while opcion != "s" and opcion != "n":
        opcion = input("Error. Vuelva a ingresar el dato(s/n): ")

porcentaje_empleados_ia = empleados_ia * 100 / contador
print("Cantidad de empleados de género masculino que votaron por IOT o IA,de entre 25 y 50 años inclusive:", cant_empleados_m)
print("Porcentaje de empleados que no votaron por IA(sin contar los femeninos y a los empleados de entre 33 y 40 años):", porcentaje_empleados_ia, "%")
print("Nombre del empleado masculino con mayor edad:", nombre_empleado_mayor, "voto por:", tecnologia_empledo_mayor)