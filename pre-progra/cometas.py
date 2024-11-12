bc = float(input("Ingrese la medida BC en cm: "))
cd = float(input("Ingrese la medida CD en cm: "))
da = float(input("Ingrese la medida DA en cm: "))
#Convertir a metros
bc_m = bc / 100.0
cd_m = cd / 100.0
da_m = da / 100.0
    
# Calcular AB y DC
ab = (bc_m**2 + da_m**2)**0.5
dc = cd_m
    
# Calcular los lados menores
bd = (ab**2 - dc**2)**0.5
ac = (da_m**2 + bd**2)**0.5
    
# Calcular perímetro de varillas de plástico
perimetro_varillas = ab + 2 * bc_m + 2 * cd_m
    
# Calcular área de papel necesario
area_cuerpo = (ab * dc) / 2
area_colas = area_cuerpo * 0.1  # 10% adicional
    
# Calcular área total de papel para 10 cometas
area_total_papel = 10 * (area_cuerpo + area_colas)
    
# Convertir perímetro de varillas de plástico a metros
perimetro_varillas_m = perimetro_varillas / 100.0
    
# Resultados
print("Materiales necesarios para la construcción de 10 cometas:")
print(f"Metros de varillas de plástico: {perimetro_varillas_m:.2f} m")
print(f"Metros cuadrados de papel: {area_total_papel:.2f} m²")
