# list_1 = [10]
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1 = 20

# print(list_1)
# print(list_2)

nombres = ["Ana", "Sol", "Pedro", "Juan"]
notas = [7,8,6,9]
min = notas[0]
pos = 0
for i in range(len(notas)):
     if (notas[i] < min):
          pos = i

print("Menor:", nombres[pos])
