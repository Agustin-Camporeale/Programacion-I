import random
import pygame

lista = [
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]}
]

def generar_numeros(lista:list):
    for i in range(1,8):
        i = random.randint(1,3)
        i_2 = random.randint(1,3)
        i_3 = random.randint(1,3)
        i_4 = random.randint(1,3)
        lista[0]["piezas"].append(i)
        lista[1]["piezas"].append(i_2)
        lista[2]["piezas"].append(i_3)
        lista[3]["piezas"].append(i_4)

generar_numeros(lista)
for i in range(len(lista)):
    print(lista[i])