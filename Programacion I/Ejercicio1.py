"""
Nombre: Agustín Camporeale
Div:213
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su sueldo para esa persona."""

nombre = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo: "))
aumento = sueldo + (sueldo * 0.10)
print(f"El aumento es de 10%, su sueldo ahora es de {aumento:.2f}")

"""Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), adolescente (entre 13 y 17 años) o niño (menor a 13 años)."""

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Mayor de edad")
elif edad >= 13:
    print("Adolescente")
else:
    print("Niño")

"""Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos. """

numeros_ingresados = 0
num_par = 0
num_impar = 0
num_min = 0
bandera_min = False
bandera_max = False
num_max = 0
suma_positivos = 0
producto_negativos = 1
while numeros_ingresados < 5:
    numero = int(input("ingrese un numero, distinto a cero: "))
    if numero % 2 == 0:
        num_par += 1
        if bandera_max == False or num_par > num_max:
            num_max = numero
            bandera_max = True
    else:
        num_impar += 1
    if bandera_min == False or numero < num_min:
        num_min = numero
        bandera_min = True
    if numero > 0:
        suma_positivos += numero
    elif numero < 0:
        producto_negativos = numero * numero

    numeros_ingresados += 1

print("La cantidad de numeros pares es:", num_par)
print("La cantidad de numeros impares es:", num_impar)
print("El menor numero ingresado fue:", num_min)
print("el mayor numero par ingresado fue:", num_max)
print("La suma de los positivos es:", suma_positivos)
print("El producto de los numeros negativos es:", producto_negativos)

"""Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO ser soltero.'"""

edad = int(input("Ingrese su edad: "))
estado_civil = input("Ingrese su estado civil: ").lower()
if edad < 18 and estado_civil != "soltero":
    print("Es muy pequeño para NO ser soltero")

"""Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 por cada estadía como base, se pide el ingreso de una estación del año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) para vacacionar para poder calcular el precio final: 
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un descuento del 10% Mar del Plata tiene un descuento del 20% 
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene un aumento del 10% Mar del Plata tiene un aumento del 20% 
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el precio sin descuento.
Validar el ingreso de datos."""

precio = 0
estacion = input("Ingrese la estacion del año: ").lower()
while estacion != "invierno" and estacion != "verano" and estacion != "otoño" and estacion != "primavera":
    estacion = input("Error. Vuelva a ingresa la estacion: ")
localidad = input("Ingrese el lugar a vacacionar(Bariloche/Cataratas/Mar del Plata/Córdoba): ").lower()
while  localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and localidad != "cordoba":
    localidad = input("Error. Vuelva a ingresar la localidad(Bariloche/Cataratas/Mar del Plata/Córdoba): ")

if estacion == "invierno" and localidad == "bariloche":
    precio = 15000 + (15000 * 0.20)
    print("El precio por ir a Bariloche en invierno es:", precio)
elif estacion == "invierno" and localidad == "cataratas" and localidad == "cordoba":
    precio = 15000 - (15000 * 0.10)
    print("El precio por ir a Cataratas o Cordoba en invierno es:", precio)
elif estacion == "invierno" and localidad == "mar del plata":
    precio = 15000 - (15000 * 0.20)
    print("El precio por ir a Mar del Plata en invierno es:", precio)

if estacion == "verano" and localidad == "bariloche":
    precio = 15000 - (15000 * 0.20)
    print("El precio por ir a Bariloche en verano es:", precio)
elif estacion == "verano" and localidad == "cataratas" and localidad == "cordoba":
    precio = 15000 + (15000 * 0.10)
    print("El precio por ir a Cataratas o Cordoba en verano es:", precio)
elif estacion == "verano" and localidad == "mar del plata":
    precio = 15000 + (15000 * 0.20)
    print("El precio por ir a Mar del Plata en verano es:", precio)

if (estacion == "otoño" or estacion == "primavera") and localidad == "bariloche":
    precio = 15000 + (15000 * 0.10)
    print("El precio por ir a Bariloche en otoño o primavera es:", precio)
elif (estacion == "otoño" or estacion == "primavera") and localidad == "cataratas":
    precio = 15000 + (15000 * 0.10)
    print("El precio por ir a Cataratas en verano es:", precio)
elif (estacion == "otoño" or estacion == "primavera") and localidad == "mar del plata":
    precio = 15000 + (15000 * 0.10)
    print("El precio por ir a Mar del Plata en otoño o primavera es:", precio)
elif (estacion == "otoño" or estacion == "primavera") and localidad == "cordoba":
    precio = 15000
    print("El precio por ir a Cordoba en otoño o primavera es:", precio)