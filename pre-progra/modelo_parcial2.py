'''
Nombre:Agustin
Apellido:Camporeale
DNI:46350154

Se desea desarrollar un programa que permita al usuario ingresar el valor en dólares 
de una criptomoneda en diferentes momentos, solicitando nombre del activo digital
(BTC, ETH, DODGE COIN), valor(No puede ser negativo), periodo de  
ingreso (antes del 2008, entre el 2008 y el 2016 o despues del 2016).
Realizar las siguientes operaciones:

1- Calcular el promedio de los valores ingresados.
2- Calcular el mayor valor ingresado antes del 2008.
3- Encontrar el valor máximo, con la fecha en la que sucedió.
4- Encontrar el valor minimo, con la fecha en la que sucedió.
5- Calcular el menor valor ingresado despues del 2016.
7- Cual fue la cripto mas ingresada al sistema.
'''

valor_mayor = 0
valor_menor = 0
valor_total = 0
valor_maximo = 0
valor_minimo = 0
bandera_max = False
bandera_min = False
bandera_menor = False
contador = 0
cripto_btc = 0
cripto_eth = 0
cripto_dodge_coin = 0
seguir = "si"
while seguir == "si":
    cripto = input("Ingrese el nombre de la criptomoneda(BTC, ETH, DODGE COIN): ").lower()
    while cripto != "btc" and cripto != "eth" and cripto != "dodge coin":
        cripto = input("Error. vuelva a ingresar el nombre de la criptomoneda(BTC, ETH, DODGE COIN): ").lower()
    if cripto == "btc":
        cripto_btc += 1
    elif cripto == "eth":
        cripto_eth +=1
    elif cripto == "dodge coin":
        cripto_dodge_coin += 1
    valor = int(input("Ingrese el valor de la criptomeneda(no puede ser negativo): "))
    while valor < 0:
        valor = int(input("Valor invalido, vuelva a ingresar el valor(no puede ser negativo): "))
    valor_total += valor
    periodo_ingreso = int(input("Ingrese el perdiodo de ingreso: "))
    if periodo_ingreso < 2008 and valor > valor_mayor:
        valor_mayor = valor

    if bandera_menor == False or valor_menor > valor and periodo_ingreso > 2016:
        valor_menor = valor
        bandera_menor = True
    
    if bandera_max == False or valor > valor_maximo:
        valor_maximo = valor
        fecha_max = periodo_ingreso
        bandera_max = True
    if bandera_min == False or valor < valor_minimo:
        valor_minimo = valor
        fecha_min = periodo_ingreso
        bandera_min = True
    contador += 1
    seguir = input("¿Desea continuar?(si/no):").lower()

promedio = valor_total / contador
print(f"El promedio de los valores ingresados es:{promedio:.2f}")
print(f"El mayor valor ingresado antes del año 2008 fue:USD{valor_mayor}")
print(f"El valor maximo fue:USD{valor_maximo} en el año {fecha_max}")
print(f"El valor minimo fue:USD{valor_minimo} en el año {fecha_min}")
print(f"El menor valor ingresado despues del año 2016 fue:USD{valor_menor}")
if cripto_btc > cripto_eth and cripto_btc > cripto_dodge_coin:
    print(f"La cripto mas ingresada fue BTC")
elif cripto_eth > cripto_dodge_coin:
    print(f"La cripto mas ingresada fue ETH")
else:
    print(f"La cripto mas ingresada fue DODGE COIN")