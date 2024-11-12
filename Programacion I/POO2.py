class Persona:
     def __init__(self, nombre, edad):
     # Inicializar los atributos nombre y edad
          self.nombre = nombre
          self.edad = edad

     def saludar(self):
     # Mostrar un mensaje de saludo con el nombre y la edad
          print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Programa principal
# persona1 = Persona("Lautaro", 26)
# persona1.saludar()

class Libro:
     def __init__(self, titulo, autor, año):
     # Inicializar los atributos titulo, autor y año
          self.titulo = titulo
          self.autor = autor
          self.año = año

     def mostrar(self):
     # Mostrar los datos del libro
          print(f"El titulo del libro es {self.titulo}, su autor es {self.autor} y el año es que se publico es {self.año}")

# libro = Libro("Harry Potter", "J. K. Rowling", 2017)
# libro.mostrar()

class Rectangulo:
     def __init__(self, base, altura):
          self.base = base
          self.altura = altura

     def area(self):
          self.area = self.base * self.altura
          print(f"La base del rectangulo es {self.area}")
     
     def perimetro(self):
          self.perimetro = (self.base + self.altura)*2
          print(f"El perimetro del rectangulo es {self.perimetro}")

# rectangulo = Rectangulo(5,3)
# rectangulo.area()
# rectangulo.perimetro()

class Animal:
     def __init__(self, nombre):
          self.nombre = nombre

class Perro(Animal):
     def mostrar(self):
          print(f"El sonido del perro es 'guau guau'")

class Gato(Animal):
          print(f"El sonido del gato es 'miau'")


class CuentaBancaria:
     def __init__(self, titular, saldo):
          self.titular = titular
          self.saldo = saldo

     def obtener_saldo(self):
          return self.saldo

     def depositar(self, cantidad):
          if cantidad > 0:
               self.saldo += cantidad
               print(f"Depósito de {cantidad} exitoso. Nuevo saldo: {self.saldo}")
     
     def retirar(self, cantidad):
          if 0 < cantidad <= self.saldo:
               self.saldo -= cantidad
               print(f"Retiro de {cantidad} exitoso. Nuevo saldo: {self.saldo}")

# cuenta = CuentaBancaria("Mario", 2000)
# cuenta.depositar(500)
# cuenta.retirar(250)