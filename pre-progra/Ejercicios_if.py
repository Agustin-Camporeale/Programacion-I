'''Ejercicio: instrucion_if_01
Enunciado:
Se deberá obtener una edad por input,
transformarlo en número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando la consola.'''

# edad = int(input("Ingrese una edad:"))
# if edad == 18:
#     print("Usted tiene 18 años")
# else:
#     print("Usted no tiene 18 años")

'''Ejercicio: instrucion_if_02
Enunciado:
Se deberá obtener la edad a través del input, transformarlo en número 
y calcular si es mayor de edad, si es mayor de 18 se mostrará el mensaje “MAYOR” utilizando la consola.'''

# edad = int(input("Ingrese una edad:"))
# if edad >= 18:
#     print("MAYOR")

'''Ejercicio: instrucion_if_03
Enunciado:
Se deberá obtener la edad a través del input, transformarlo en número 
y calcular si es o no mayor de edad, si es mayor de 18 se mostrará el mensaje “MAYOR” caso contrario “MENOR” en 
ambos casos utilizando la consola.'''

# edad = int(input("Ingrese una edad:"))
# if edad >= 18:
#     print("MAYOR")
# else:
#     print("MENOR")

'''Ejercicio: instrucion_if_04
Enunciado:
Se deberá obtener la edad a través del input, 
transformarlo en número y calcular si es adolescente (edad entre 13 y 17 años). 
Se deberá informar utilizando la consola.'''

# edad = int(input("Ingrese una edad:"))
# if edad >= 13 and edad <= 17:
#     print("Adolescente")

'''Ejercicio: instrucion_if_05
Enunciado:
Se deberá obtener la edad a través del input, 
transformarlo en número e informar si la persona "NO ES ADOLESCENTE" utilizando la consola.'''

# edad = int(input("Ingrese una edad:"))
# if edad < 13 or edad > 17:
#     print("No es adolescente")

'''Ejercicio: instrucion_if_06
Enunciado:
Se deberá obtener la edad a través del input, 
transformarlo en número y calcular si es mayor, niño/a(menor de 10) o pre-adolescente 
(edad entre 10 y 13 años) o adolescente (edad entre 13 y 17 años) de edad, 
se deberá informar utilizando la consola.'''

# edad = int(input("Ingrese una edad:"))
# if edad >= 18:
#     print("Mayor")
# elif edad >= 13 and edad <= 17:
#     print("Adolescente")
# elif edad >= 10:
#     print("Pre-Adolescente")
# elif edad < 10:
#     print("Niño")

''' Ejercicio: instrucion_if_07
Enunciado:
Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos
naturalizados desde los dieciocho (18) años están habilitados a votar. 
Se deberá informar si es o no posible que la persona concurra a votar 
en base a la información suministrada.'''

# edad = int(input("Ingrese su edad:"))
# tipo = input("Ingrese nativo o naturalizado:").lower()
# if edad >= 16 and tipo == "nativo":
#     print("Puede votar")
# elif edad >= 18 and tipo == "naturalizado":
#     print("Puede votar")
# else:
#     print("NO puede votar")

'''Ejercicio: instrucion_if_08
Enunciado:
Al ingresar una edad menor a 18 años y un estado civil distinto a "Soltero", NO HACER NADA,
pero si no es asi, y es soltero y no es menor, mostrar el siguiente mensaje: 'Es soltero y no
es menor.'''

# edad = int(input("Ingrese su edad:"))
# estado_civil = input("Ingrese su estado civil:").lower()
# if edad >= 18 and estado_civil == "soltero":
#     print("Es soltero y no es menor")

import random

'''Ejercicio: instrucion_if_09
Se deberá mostrar  un número
aleatorio entre el 1 y el 10 inclusive'''

# numero = random.randint(1,10)
# print(numero)

'''Ejercicio: instrucion_if_10
Enunciado:
Se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
    6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
    4 y 5           ---> Aprobado, la nota es ...
    1, 2 y 3        ---> Desaprobado, la nota es ...'''

# nota = random.randint(1,10)
# if nota > 5:
#     print(f"Promocion directa, la nota es {nota}")
# elif nota == 4 or nota == 5:
#     print(f"Aprobado, la nota es {nota}")
# elif nota < 4:
#     print(f"Desaprobado, la nota es {nota}")

'''Ejercicio:TP_04
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.'''

compra = int(input("¿Cuantas lamparas va a comprar?:"))
marca = input("¿De que marca llevara?(ArgentinaLuz / FelipeLamparas / Otras):").lower()
lamparas_precio = 800 * compra

if compra >= 6:
    lamparas_precio = lamparas_precio  * 0.5
elif compra == 5:
    if marca == "argentinaluz":
        lamparas_precio = lamparas_precio - (lamparas_precio  * 0.4)
    else:
        lamparas_precio = lamparas_precio - (lamparas_precio  * 0.3)
elif compra == 4:
    if marca == "argentinaluz" or marca == "felipelamparas":
        lamparas_precio = lamparas_precio - (lamparas_precio  * 0.25)
    else:
        lamparas_precio = lamparas_precio - (lamparas_precio * 0.2)
elif compra == 3:
    if marca == "argentinaluz":
        lamparas_precio = lamparas_precio - (lamparas_precio * 0.15)
    elif marca == "felipelamparas":
        lamparas_precio = lamparas_precio - (lamparas_precio * 0.1)
    else:
        lamparas_precio = lamparas_precio - (lamparas_precio * 0.05)

if lamparas_precio >= 4000:
    lamparas_precio = lamparas_precio - (lamparas_precio * 0.05)

print(f"El precio final(con descuento) es:${int(lamparas_precio)}")


