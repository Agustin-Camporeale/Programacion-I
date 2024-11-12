# Ejercicio 1:Realizar una función recursiva que calcule la suma de los primeros números naturales

def sumar_naturales(numero: int)->int:
     if numero == 10:
          return 0
     else:
          return numero + sumar_naturales(numero + 1)

print(sumar_naturales(1))

# Ejercicio 2:Realizar una función recursiva que calcule la potencia de un número

def calcular_potencia(base: int,exponente: int)->int:
     if exponente == 0:
          return 1
     else:
          return base * calcular_potencia(base, exponente - 1)

base = int(input("Ingrese la base de la potencia: "))
exponente = int(input("Ingrese el exponente de la potencia: "))
print(f"La potencia de {base} elevado a {exponente} es", calcular_potencia(base, exponente))

# Ejercicio 3:Realizar una función recursiva que permita realizar la suma de los dígitos de un número

def sumar_digitos(numero: int)->int:
     if numero < 10:
          return numero
     else:
          return numero % 10 + sumar_digitos(numero // 10)

numero = int(input("Ingrese un numero(Que tenga mas de un digito):"))
print(f"La suma de los digitos de {numero} es {sumar_digitos(numero)}")

# Ejercicio 4:Realizar una función para calcular el número de Fibonacci de un número ingresado por consola

def calcular_fibonacci(numero: int)->int:
     if numero == 0:
          return 0
     elif numero == 1:
          return 1
     else:
          return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

numero = int(input("ingrese un numero(mayor a 0): "))
print(f"El numero de Fibonacci de {numero} es:", calcular_fibonacci(numero))
