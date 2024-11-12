class Calculadora: 
     def __init__(self, num_1:int, num_2:int):
          self.numero_1 = num_1
          self.numero_2 = num_2

    ############## Bucle calculadora ###############

     def ejecutar_calculadora(self):
          while True:
               opciones  = self.__mostrarmenu()
          match (opciones):
               case 1: 
                    self.suma()
               case 2:
                    self.resta()
               case 3:
                    self.multiplicacion()
               case 4:
                    self.division()
               case 5:
                    self.reemplazo_nums()

          if (opciones > 5 or opciones < 0):
               break

     def __mostrarmenu(self):
          return int(input("""
                    1 sumar
                    2 restar
                    3 multiplicar
                    4 dividir
                    5 cambiar numeros
                    """))

    ################ 4 operaciones básicas ###############
     def suma(self):
          suma = self.numero_1 + self.numero_2 
          print(f"El resultado de la suma es: {suma}")
    
     def resta(self):
          resta = self.numero_1 - self.numero_2 
          print(f"El resultado de la resta es: {resta}")

     def multiplicacion(self):
          multiplicacion = self.numero_1 * self.numero_2 
          print(f"El resultado de la multiplicacion es: {multiplicacion}")

     def division(self):
          division = self.numero_1 / self.numero_2 
          print(f"El resultado de la division es: {division}")

################ Reemplazo de atributos ###############
     def reemplazo_nums(self):
          self.numero_1 = int(input("Ingrese un numero : "))
          self.numero_2 = int(input("Ingrese otro numero : "))



numero_ing_1 = int(input("Ingrese un numero : "))
numero_ing_2 = int(input("Ingrese otro numero : "))

###### INSTANCIA ###########
numeros = Calculadora(numero_ing_1,numero_ing_2)
numeros.suma()
numeros.reemplazo_nums()