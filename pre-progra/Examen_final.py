"""
Nombre:Agustin
Apellido:Camporeale
Division:203
DNI:46350154

Consigna:
Es la gala final de Gran Hermano y la producción nos pide un programa para contar los votos de los
televidentes y saber así quién será el ganador del programa.
Los participantes finalistas son: Emma, Furia y Bautista.
Para poder participar de la votación, el televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo (Validar entre las 3 opciones)
● Realizó el pago con mercado pago (si o no)
Se necesita saber::
Tema A:
1. El promedio de edad de las votantes de género femenino que realizaron el pago con
mercado pago..
2. El nombre del participante que ganó el reality (El que tiene más votos).
3. Nombre del votante más joven qué votó a Bautista.
4. Nombre de cada participante y porcentaje de los votos que recibió.
5. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Furia o a
Emma.
"""

votantes_femeninos = 0
edad_femeninos = 0
votos_emma = 0
votos_furia = 0
votos_bautista = 0
contador = 0
votante_mas_joven = ""
edad_mas_joven = 0
bandera_min = False
cant_personas_m = 0
while True:
    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad(debe ser mayor a 13): "))
    while edad < 13:
        edad = int(input("Edad ingresada no valida. Vuelva a ingresar su edad: "))
    genero = input("Ingrese su genero(masculino, femenino, otro): ")
    voto = input("Ingrese el nombre del participante a quien le dará el voto positivo: ").lower()
    while voto != "emma" and voto != "furia" and voto != "bautista":
        voto = input("ERROR. Vuelva a ingresar el nombre del participante a quien le dará su voto positivo: ").lower()
    if voto == "emma":
        votos_emma += 1
        if edad >= 25 and edad <= 40 and genero == "masculino":
            cant_personas_m += 1
    elif voto == "furia":
        votos_furia += 1
        if edad >= 25 and edad <= 40 and genero == "masculino":
            cant_personas_m += 1
    elif voto == "bautista":
        votos_bautista += 1
        if bandera_min == False or edad_mas_joven > edad:
            votante_mas_joven = nombre
            bandera_min = True
    mercado_pago = input("¿Realizar el pago con mercado pago?(si/no): ").lower()
    if genero == "femenino" and mercado_pago == "si":
        votantes_femeninos += 1
        edad_femeninos += edad
    contador += 1
    seguir = input("¿Desea continuar?(si/no): ").lower()
    if seguir == "no":
        break

if votantes_femeninos > 0:
    promedio_edad = edad_femeninos / votantes_femeninos
    print(f"\nEl promedio de edad de las votantes de género femenino que realizaron el pago con mercado pago es {promedio_edad:.2f}")
else:
    print("\nNo se registraron personas votantes del género femenino")

if votos_emma > votos_furia and votos_emma > votos_bautista:
    ganador = "Emma"
elif votos_furia > votos_emma:
    ganador = "Furia"
else:
    ganador = "Bautista"

porcentaje_emma = votos_emma / contador
porcentaje_furia = votos_furia / contador
porcentaje_bautista = votos_bautista / contador

print(f"\nEl ganador de Gran Hermano es {ganador}"
      f"\nEl nombre del votante más joven que voto a Bautista es {votante_mas_joven}"
      f"\nEl porcentaje de votos de Emma es %{porcentaje_emma:.2f}" 
      f"\nEl porcentaje de votos de Furia es %{porcentaje_furia:.2f}"
      f"\nEl porcentaje de votos de Bautista es %{porcentaje_bautista:.2f}"
      f"\nLa cantidad de personas de género masculino entre 25 y 40 años que votaron a Furia o a Emma son:{cant_personas_m}")