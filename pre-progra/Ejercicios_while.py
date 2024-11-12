# 1-Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
# numero = 0
# while numero < 10:
#     numero += 1
#     print(numero)

# 2-Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
# numero = 11
# while numero != 1:
#     numero -= 1
#     print(numero)

# 3-Mostrar la suma de los números desde el 1 hasta el 10.
# contador = 0
# suma = 0
# while contador < 10:
#     contador += 1
#     suma += contador
# print(suma)

# 4-Mostrar la suma de los números pares desde el 1 hasta el 10.
# contador = 0
# suma = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         suma += contador
# print(suma)

# 5-Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar por pantalla.
# contador = 0
# suma = 0
# while contador < 5:
#     contador += 1
#     numero = int(input(f"Ingrese el numero {contador}:"))
#     suma += numero
# promedio = suma / contador
# print(f"La suma de los numeros ingresados es:{suma} y el promedio es {promedio}")

# 6-Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
# opcion = ""
# numero_ingresados = 0
# while opcion != "no":
#     numero = int(input("Ingrese un numero: "))
#     numero_ingresados += 1
#     suma += numero
#     opcion = input("¿Agregar mas numeros?(si/no):").lower()
# promedio = suma / numero_ingresados
# print(f"La suma de los numeros ingresados es {suma} y el promedio es {promedio:.2f}")

# 7-Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

opcion = ""
numero_ingresados = 0
negativos = 0
bandera_positivos = False
bandera_negativos = False
mensaje = ""
suma = 0
while opcion != "no":
    numero = int(input("Ingrese un numero: "))
    numero_ingresados += 1
    if numero > 0:
        suma += numero
        bandera_positivos = True
    elif numero < 0:
        negativos *= numero
        bandera_negativos = False
    opcion = input("¿Agregar mas numeros?(si/no):").lower()
if bandera_positivos == True:
    mensaje += f"La suma de los positivos es: {suma} "
else:
    mensaje += f"No se ingresaron numeros positivos "
if bandera_negativos == True:
    mensaje += f"y el producto de los negativos es: {negativos}\n"
else:
    mensaje += f"no se ingresaron numeros negativos\n"
print(mensaje)

# 8-Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# contador = 0
# maximo = 0
# minimo = 0
# bandera_max = False
# bandera_min = False
# while contador < 10:
#     contador += 1
#     numero = int(input("Ingrese un numero: "))
#     if bandera_max == False or numero > maximo:
#         maximo = numero
#         bandera_max = True
#     elif bandera_min == False or numero < minimo:
#         minimo = numero
#         bandera_min = True
# print(f"El maximo es {maximo} y el minimo es {minimo}")

# 9-Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

# clave = "123"
# clave = input("Ingrese su clave: ")
# while clave != "123":
#     clave = input("Clave incorrecta vuelva a intentarlo: ")
# print("Bienvenido")

# 10-Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

# contraseña = input("Ingrese su contraseña: ")
# intentos = 0        
# while contraseña != "123" and intentos < 2:
#     intentos += 1
#     contraseña = input("Contraseña incorrecta... vuelva a intentarlo: ")
# if contraseña == "123":
#     print("Bienvenido")
# else:
#     print("Su cuenta ha sido bloqueada")

# 11-Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

# nota = int(input("Ingrese una nota(del 1 al 10): "))
# while nota > 10 or nota <= 0:
#     nota = int(input("Dato invalido... vuelva a ingresar una nota: "))
# print(f"Su nota es {nota}")

# 12-Solicitarle al usuario el ingreso de un color primario. Validar que el mismo sea Rojo, Verde o Azul.

# color = input("Ingrese un color primario: ").lower()
# while color != "rojo" and color != "verde" and color != "azul":
#     color = input("Solo colores primarios: ")
# print(f"El color que eligio es {color}")

'''
TP 5
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas). 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
    a) print de edad promedio de las personas ingresadas
    b) Estado civil mas ingresado
    c) El numero de legajo de la persona con menos edad
'''

# suma_edad = 0
# contador = 0
# seguir = "si"
# bandera_menor = False
# legajo_min = 0
# edad_menor = 0
# contador_soltero = 0
# contador_divorciado = 0
# contador_casado = 0
# contador_viudo = 0
# while seguir == "si":
#     apellido = input("Ingrese su apellido: ")
#     edad = int(input("Ingrese su edad: "))
#     while edad < 18 or edad > 90:
#         edad = int(input("Dato invalido. Vuelva a ingresar su edad: "))
#     estado_civil = input("Ingrese su estado civil[Soltero/a, Casado/a, Divorciado/a, Viudo/a]: ").lower()
#     while estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "divorciado" and estado_civil != "viudo":
#         estado_civil = input("Dato invalido. Vuelva a ingresar su estado civil: ")        
#     legajo = int(input("Ingrese su número de Legajo(entre 1000 y 9999): "))
#     while legajo > 9999 or legajo < 999:
#         legajo = int(input("Numero de legajo invalido. Vuelva a ingresarlo: "))
#     contador += 1
#     suma_edad += edad
#     if bandera_menor == False or edad_menor > edad:
#         edad_menor = edad
#         legajo_min = legajo
#         bandera_menor = True
#     if estado_civil == "soltero":
#         contador_soltero += 1
#     elif estado_civil == "casado":
#         contador_casado += 1
#     elif estado_civil == "divorciado":
#         contador_divorciado += 1
#     elif estado_civil == "viudo":
#         contador_viudo += 1     
#     seguir = input("¿Desea agregar mas dato?:(si/no):").lower()
# estado_mas_ing = ""    
# promedio = suma_edad / contador
# print(f"La edad promedio de las persona ingresadas es:{promedio:.2f}")
# if contador_viudo > contador_casado and contador_viudo > contador_soltero and contador_viudo > contador_divorciado:
#     estado_mas_ing = "Viudo"
# elif contador_casado > contador_soltero and contador_casado > contador_divorciado:
#     estado_mas_ing = "Casado"
# elif contador_soltero > contador_divorciado:
#     estado_mas_ing = "Soltero"
# else:
#     estado_mas_ing = "Divorciado"

# print(f"El estado civil mas ingresado es {estado_mas_ing}")
# print(f"El numero de legajo de la persona con menos edad es:{legajo_min}")

'''TP 6
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por input y los resultados por consola (print)
'''

# candidatos = 0
# total_votos = 0
# votos_mayor = 0
# votos_menor = 0
# bandera_mayor = False
# bandera_menor = False
# prom_edad = 0
# seguir = "si"
# while seguir == "si":
#     nombre = input("Ingrese su nombre: ")
#     edad = int(input("Ingrese su edad(mayor a 25): "))
#     while edad < 25:
#         edad = int(input("Dato invalido. Ingrese su edad(mayor a 25): "))
#     votos = int(input("Ingrese la cantidad de votos: "))
#     while votos <= 0:
#         votos = int(input("Dato invalido, Ingrese nuevamente(mayor a 0):"))
#     total_votos += votos
#     prom_edad += edad
#     candidatos += 1
#     if bandera_mayor == False or votos_mayor > votos:
#         votos_mayor = votos
#         nombre_mayor = nombre
#         bandera_mayor = True
#     if bandera_menor == False or votos_menor < votos:
#         votos_menor = votos
#         nombre_menor = nombre
#         edad_menor = edad
#         bandera_menor = True
#     seguir = input("¿Desea continuar? si/no: ").lower()
# promedio = prom_edad / candidatos
# print(f"\n El nombre del candidato con más votos es:{nombre_mayor}"
#       f"\n El nombre y la edad de el candidato con menos votos es:{nombre_menor} {edad_menor} años"
#       f"\n El promedio de edades de los candidatos es:{promedio}"
#       f"\n El total de votos emitidos es:{total_votos}")

"""
Nombre: Agustin Camporeale

Integrador Estructuras Repetitivas

Permitir que el usuario ingrese todos los números que desee. Los mismos deben estar comprendidos entre -10000 y 10000, y deben ser distintos de 0. Determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.
"""
# suma_negativos = 0
# suma_positivos = 0
# cant_num_negativos = 0
# cant_num_positivos = 0
# contador = 0
# numero_mas = 0
# seguir = "si"
# prom_num_positivos = 0
# prom_num_negativos = 0
# while seguir == "si":
#     numero = int(input("Ingrese un numero: "))
#     while numero < -10000 and numero > 10000 and numero == 0:
#         numero = int(input("Ingrese un numero(entre -10000 y 10000, y no puede ser 0):"))
#     contador += 1
#     if numero < 0:
#         cant_num_negativos+= 1
#         suma_negativos += numero
#     elif numero > 0:
#         suma_positivos += numero
#         cant_num_positivos += 1
#         if numero > numero_mas:
#             numero_mas = numero
#     seguir = input("¿Desea continuar?(si/no):").lower()

# if cant_num_positivos != 0:
#     prom_num_positivos = suma_positivos / cant_num_positivos 
#     print(f"La suma total de los numeros positivos es:{suma_positivos}")
#     print(f"El promedio de los numeros positivos es:%{prom_num_positivos:.2f}")
#     print(f"El numero positivo ingresado mas grande es:{numero_mas}")
#     print(f"El porcentaje de numeros negativos ingresados es:%{prom_num_negativos:.2f}")
# if cant_num_negativos != 0:
#     prom_num_negativos = cant_num_negativos / contador * 100
#     print(f"La cantidad de numero negativos ingresado fue:{cant_num_negativos}")
#     print(f"La suma total de los numeros negativos es:{suma_negativos}")
#     print(f"La cantidad de numero negativos ingresado fue:{cant_num_negativos}")
#     print(f"El porcentaje de numeros negativos ingresados es:%{prom_num_negativos:.2f}")
    
