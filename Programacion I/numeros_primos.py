def es_primo(num,divisores=2):
     primo = num % divisores
     if divisores == num:
          return True
     elif primo == 0:
          return False
     else:
          return es_primo(num,divisores+1)

numero = int(input("Ingrese un numero(mayor a 1): "))
if es_primo(numero):
     print("Es primo")
else:
     print("No es primo")