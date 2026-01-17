"""
Programa: Ejemplo de Programación Orientada a Objetos en Python
Asignatura: Programación
Tema: POO (Clases, Objetos, Herencia, Encapsulación y Polimorfismo)
Autor: Gabriela Yepez
"""

# -------------------------
# CLASE BASE
# -------------------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre          # Atributo público
        self.__edad = edad            # Atributo privado (Encapsulación)

    # Método para obtener la edad (getter)
    def get_edad(self):
        return self.__edad

    # Método para modificar la edad (setter)
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser mayor a cero")

    # Método que será sobrescrito (Polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.__edad} años."


# -------------------------
# CLASE DERIVADA (HERENCIA)
# -------------------------
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Polimorfismo: sobrescribimos el método presentarse
    def presentarse(self):
        return f"Hola, soy {self.nombre}, estudio {self.carrera} y tengo {self.get_edad()} años."


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

# Creación de objetos (instancias)
persona1 = Persona("Carlos", 30)
estudiante1 = Estudiante("Gabriela", 21, "Ingeniería en Sistemas")

# Uso de métodos
print(persona1.presentarse())
print(estudiante1.presentarse())

# Demostración de encapsulación
estudiante1.set_edad(22)
print("Edad actualizada:", estudiante1.get_edad())
