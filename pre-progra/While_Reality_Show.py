participantes = 0
while participantes == 0 and participantes < 3:
    participante_1 = input("ingrese su nombre: ")
    edad_par1 = int(input("ingrese su edad(mayor a 25): "))
    while edad_par1 < 25:
        edad_par1 = int(input("ingrese su edad(mayor a 25): "))
    cantidad_votos1 = int(input("ingrese la cantidad de votos: "))
    while cantidad_votos1 < 0:
        cantidad_votos1 = int(input("Dato incorecto... vuelva a intertarlo: "))  
    participantes += 1
    participante_2 = input("ingrese su nombre: ")
    edad_par2 = int(input("ingrese su edad(mayor a 25): "))
    while edad_par2 < 25:
        edad_par2 = int(input("ingrese su edad(mayor a 25): "))
    cantidad_votos2 = int(input("ingrese la cantidad de votos: "))
    while cantidad_votos2 < 0:
        cantidad_votos2 = int(input("Dato incorecto... vuelva a intertarlo: "))  
    participantes += 1
    participante_3 = input("ingrese su nombre: ")
    edad_par3 = int(input("ingrese su edad(mayor a 25): "))
    while edad_par3 < 25:
        edad_par3 = int(input("ingrese su edad(mayor a 25): "))
    cantidad_votos3 = int(input("ingrese la cantidad de votos: "))
    while cantidad_votos3 < 0:
        cantidad_votos3 = int(input("Dato incorecto... vuelva a intertarlo: "))  
    participantes += 1
    
if cantidad_votos1 > cantidad_votos2 and cantidad_votos1 > cantidad_votos3:
    print("El participante con mas votos fue:", participante_1)
elif cantidad_votos2 > cantidad_votos1 and cantidad_votos2 > cantidad_votos3:
    print("El participante con mas votos fue:", participante_2)
elif cantidad_votos3 > cantidad_votos2 and cantidad_votos3 > cantidad_votos1:
    print("El participante con mas votos fue:", participante_3)

if cantidad_votos1 < cantidad_votos2 and cantidad_votos1 < cantidad_votos3:
    print("El partcipante con menos votos fue:", participante_1, edad_par1,"años")
elif cantidad_votos2 < cantidad_votos1 and cantidad_votos2 < cantidad_votos3:
    print("El participante con menos votos fue:", participante_2, edad_par2,"años")
elif cantidad_votos3 < cantidad_votos1 and cantidad_votos3 < cantidad_votos2:
    print("El participante con menos votos fue:", participante_3, edad_par3,"años")
total_edad = edad_par1 + edad_par2 + edad_par3
print("El promedio de edad es:", total_edad / 3)
total_votos = cantidad_votos1 + cantidad_votos2 + cantidad_votos3
print("El total de los votos fue:", total_votos)
    
