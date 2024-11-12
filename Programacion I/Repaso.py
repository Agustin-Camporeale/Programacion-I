"""Enunciado/s:
Tabla de Posiciones de Torneo de Ping-Pong
Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
Los datos que se cargarán son:
Nombre del jugador
Edad (validar)
Cantidad de puntos (validar-número entero positivo, hasta 60).
Número de partidos ganados (validar-número entero positivo, hasta 35).
Tipo de saque ("plano", "liftado", "cortado")
Categoría ("elite", "experto", "avanzado")
Se necesita saber
Tema A:
1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
inclusive.
2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
3-Porcentaje de jugadores de categoría "experto".
4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea elite"""

opcion = "s"
jugadores_saque_plano = 0
jugador_menor_edad = 0
bandera_menor = False
cant_jugadores_experto = 0
cant_jugadores_avanzado = 0
contador = 0
cant_saque_plano = 0
cant_saque_cortado = 0
cant_saque_liftado = 0
saque_elite_mas_usado = ""

while opcion == "s":
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    edad = int(input("Ingrese la edad del jugador(debe ser mayor a 18): "))
    while edad < 18 or edad > 99:
        edad = int(input("Erorr. vuelva a ingresar la edad del jugador(debe ser mayor a 18): "))
    cantidad_puntos = int(input("Ingrese la cantidad de puntos del jugador(hasta 60): "))
    while cantidad_puntos < 0 and cantidad_puntos > 60:
        cantidad_puntos = int(input("Error. Vuelva a ingresar la cantidad de puntos del jugador: "))
    partidos_ganados = int(input("Ingrese cuantos partidos ganados tiene el jugador(hasta 35): "))
    while partidos_ganados < 0 and partidos_ganados > 35:
        partidos_ganados = int(input("Error. vuelva a ingresar los partidos ganados del jugador(hasta 35): "))
    tipo_saque = input("Ingrese el tipo de saque del jugador(plano, liftado, cortado): ").lower()
    while tipo_saque != "plano" and tipo_saque != "liftado" and tipo_saque != "cortado":
        tipo_saque = input("Error. Vuelva a ingresar el tipo de saque del jugador: ").lower()
    if tipo_saque == "plano":
        cant_saque_plano += 1
    elif tipo_saque == "cortado":
        cant_saque_cortado += 1
    else:
        cant_saque_liftado += 1
    categoria = input("Ingrese la categoria del jugador(elite, experto, avanzado): ").lower()
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("ERROR. vuelva a ingresar la categoria del jugador(elite, experto, avanzado): ").lower()
    if (edad >= 19 and edad <= 25) and categoria == "elite" and tipo_saque == "plano":
        jugadores_saque_plano += 1

    if (bandera_menor == False or edad < jugador_menor_edad) and cantidad_puntos > 50:
        nombre_menor = nombre_jugador
        categoria_menor = categoria
        bandera_menor = True

    if categoria == "experto":
        cant_jugadores_experto += 1
    elif categoria == "avanzado":
        cant_jugadores_avanzado += 1
    
    if categoria == "elite":
        if cant_saque_plano > cant_saque_cortado and cant_saque_plano > cant_saque_liftado:
            saque_elite_mas_usado = "plano"
        elif cant_saque_cortado > cant_saque_plano:
            saque_elite_mas_usado = "cortado"
        else:
            saque_elite_mas_usado = "liftado"

    contador += 1
    opcion = input("¿Desea agregar mas jugadores?(s/n):").lower()
    while opcion != "s" and opcion != "n":
        opcion = input("ERROR. vuelva a ingresar:¿Desea agregar mas jugadores?(s/n): ").lower()

porcentaje_jugadores_expertos = cant_jugadores_experto * 100 / contador

print("la cantidad de jugadores de la categoría elite con tipo de saque plano, cuya edad esté entre 19 y 25 años son:", jugadores_saque_plano)
print("El nombre del jugador de menor edad con mas de 50 puntos es:", nombre_menor, "y su categoria es", categoria_menor)
print("El porcentaje de jugadores de la categoria experto es:", porcentaje_jugadores_expertos,"%")
print("El saque mas usado por los jugadores de la categoria elite es:", saque_elite_mas_usado)



