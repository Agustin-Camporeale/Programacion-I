import math

'''Ejercicio: entrada_salida_03
Enunciado:
Se deberá obtener un dato utilizando el input 
y luego mostrar por consola "El dato es: " concatenado con el dato que ingreso el usuario.'''

# dato = input("Ingrese un dato: ")
# print("El dato es:", dato)

'''Ejercicio: entrada_salida_04
Enunciado:
Se deberá obtener una edad utilizando el input 
y luego mostrar un mensaje acorde con la edad ingresada.'''

# edad = input("ingrese su edad: ")
# print("Su edad es: ", edad, "años")

'''Ejercicio: entrada_salida_05
Enunciado:
Se deberá obtener tanto el nombre como la edad a traves de 2 inputs y luego
mostrarlo concatenados utilizando la consola. 
Ej: "Usted se llama José y su edad es 66 años"'''

# nombre = input("Ingrese su nombre:")
# edad = str(input("Ingrese su edad:"))
# print("usted se llama " + nombre + " y su edad es " + edad + " años")

'''Ejercicio: entrada_salida_06
Enunciado:
Se deberán obtener 2 valores numericos, realizar la suma y luego
mostrar el resultado de la operación utilizando la consola. 
Ej: "El resultado de la sumas es: 755" '''

# numero = int(input("ingrese un numero:"))
# numero2 = int(input("ingrese otro numero:"))
# suma = numero + numero2
# print("El resultado de la suma es: ", suma)

'''Ejercicio: entrada_salida_07
Enunciado:
Se deberan pedir dos numeros por input y realizar cuatro operaciones (suma,
resta, division y multiplicacion).Mostrar los 4 resultados por consola.
Ej: "El resultado de la …… es: 755"  '''
# numero1 = int(input("ingrese un numero:"))
# numero2 = int(input("ingrese otro numero:"))
# suma = numero1 + numero2
# resta = numero1 - numero2
# division = numero1 / numero2
# multiplicacion = numero1 * numero2
# print("el resultado de la suma es:", suma, "\n"
#       "el resultado de la resta es:", resta, "\n"
#       "el resultado de la division es:", division, "\n"
#       "el resultado de la multiplicacion es:", multiplicacion)

'''Ejercicio: entrada_salida_08
Enunciado:
Se deberan pedir dos numeros por input y realizar una operacion que devuelva el resto
de una division entre los numeros ingresados.
Ej: "El resto de dividir 7 por 2 es: 1" '''

# numero1 = int(input("Ingrese un numero:"))
# numero2 = int(input("Ingrese un numero:"))
# resto = numero1 % numero2
# print("El resto de la divion es: ", resto)

'''Ejercicio: entrada_salida_09
Enunciado:
Se deberan tomar dos datos con input. El primero correspondera al sueldo 
y el segundo al incremento del sueldo(porcentaje). 
Mostrar por consola el sueldo con aumento.'''

# sueldo = int(input("Ingrese su sueldo:"))
# incremento_sueldo = int(input("Ingrese el incremento:"))
# porcentaje_incremento = sueldo * incremento_sueldo / 100
# sueldo_total = sueldo + porcentaje_incremento
# print(f"El sueldo con incremento es {sueldo_total}")

'''Ejercicio: entrada_salida_10
Enunciado:
Se deberan tomar dos datos con input. El primero correspondera al precio de un producto 
y el segundo al descuento realizado en el mismo(porcentaje).
Mostrar por consola el precio con descuento.'''

# producto = int(input("ingrese el precio del producto:"))
# descuento = int(input("ingrese el descuento:"))
# porcentaje_descuento = producto * descuento / 100
# precio = producto - porcentaje_descuento
# print(f"El precio con descuento es {precio}")

'''Enunciado:
2.	Para el departamento de Pinturas:
	A.	Al ingresar una temperatura en Fahrenheit debemos mostrar la temperatura en Centígrados con un mensaje concatenado 
        (0 °F − 32) × 5/9 = -17,78 °C

    B.	Al ingresar una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        (0 °C × 9/5) + 32 = 32 °F    '''

# A
# temperatura_fahrenheit = float(input("Ingrese la temperatura en fahrenheit:"))
# tempreatura_centigrados = (temperatura_fahrenheit - 32) * 5/9
# print(f"la temperatura en centigrados es {tempreatura_centigrados}")
# B
# tempreatura_c = float(input("Ingrese la temperatura en centigrados:"))
# tempreatura_f = (tempreatura_c * 9 / 5) + 32
# print(f"la temperatura en fahrenheit es: {tempreatura_f}")

'''Enunciado:Integrador E/S
Para el departamento de logística de una importante empresa de construcción, 
necesitamos saber:
La cantidad de camiones que harían falta para transportar los materiales 
que se utilizarán para la construcción de un edificio. Para ello, 
se ingresa la cantidad de toneladas necesarias de materiales a transportar. 
El programa deberá informar la cantidad de camiones, sabiendo que cada uno 
de ellos puede transportar por viaje 3500kg.
A partir del ingreso de la cantidad de kilómetros que tiene que recorrer 
estos camiones para llegar al destino de la obra, necesitamos que el programa 
informe cual es el tiempo (en horas) que tardará cada uno de los camiones, 
si sabemos que cada camión puede ir a una velocidad máxima y constante de 90 km/h '''

materiales = int(input("Ingrese la cantidad de materiales necesarias a transportar:"))
cantidad_de_camiones = materiales / 3500
print(f"la cantidad de camiones necesarios son: {math.ceil(cantidad_de_camiones)}")
kilometros = int(input("Ingrese la cantidad de km a recorrer:"))
tiempo = kilometros / 90 * 60
print(f"El tiempo que tardara cada uno de los camiones es: {int(tiempo)}","minutos")
