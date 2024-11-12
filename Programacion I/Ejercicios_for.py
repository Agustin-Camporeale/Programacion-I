# # Ejercicio 1: Mostrar los números ascendentes desde el 1 al 10

# for i in range(1,11):
#    print(i)

# # Ejercicio 2: Mostrar los números descendentes desde el 10 al 1

# for i in range(10,0,-1):
#     print(i)

# # Ejercicio 3: Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

# numero = int(input("Ingrese un numero: "))
# for i in range(0,numero+1):
#     print(i)

# # Ejercicio 4: Ingresar un número y mostrar la tabla de multiplicar de ese número

# numero = int(input("Ingrese un numero: "))
# for i in range(0,11):
#     multiplicacion = numero * i
#     print(numero, "x", i, "=", multiplicacion)

# # Ejercicio 5: Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

# suma = 0
# contador = 0
# for i in range(1,11):
#     numero = int(input("Ingrese un numero(con 0 termina)"))
#     if numero == 0:
#         break
#     suma += numero
#     contador += 1
    
# promedio = suma / contador
# print("La suma de los numeros ingresados es", suma)
# print(f"El promedio de los numeros ingresados es {promedio:.2f} %")

# Ejercicio 6: Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

# for i in range(0,11,3):
#     if i == 0:
#         print(1)
#     else:
#         print(i)

# Ejercicio 7: Mostrar los números pares que hay desde la unidad hasta el número 50 (*)

# for i in range(1,51):
#     numero_par = i
#     if numero_par % 2 == 0:
#         print(numero_par)

# Ejercicio 8: Realizar un programa que permita mostrar una pirámide de números.

# numero = int(input("ingrese un numero: "))
# acumulador = ""
# for i in range(1,numero+1):
#     acumulador += str(i)
#     print(acumulador,end="\n")

# Ejercicio 9: Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

# numero = int(input("Ingrese un numero: "))
# cant_divisores = 0
# for i in range(1,numero+1):
#     divisores = i
#     if numero % i == 0:
#         print(divisores,end=" ")
#         cant_divisores += 1
# print("\nLa cantidad de divisores encontrados es:", cant_divisores)

# Ejercicio 10: Ingresar un número. Determinar si el número es primo o no.

# numero = int(input("Ingrese un número para determinar si es primo: "))
# conta = 0
# for i in range(1,numero):
#     if numero % i == 0:
#         conta += 1

# if conta == 1:
#     print(f"El numero {numero}, es primo")
# else:
#     print(f"El numero {numero}, No es primo")

# Ejericicio 11: Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

numero = int(input("Ingrese un numero: "))
primo = False
cantidad_primos = 0
while numero <= 1:
    numero = int(input("Eror,Vuelva a ingresar un numero(mayor a 1): "))
for dividido in range(2,numero + 1):
    primo = True

    for divisor in range(2,dividido):
        if dividido % divisor == 0:
            primo = False
        
    if primo == True:
        print(f"{dividido} es primo")
        cantidad_primos += 1
print(f"La cantidad de primos encotrados es {cantidad_primos}")