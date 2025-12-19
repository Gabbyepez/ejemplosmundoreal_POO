# Ejemplo del mundo real: Sistema de Reservas de un Hotel

class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_datos(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"


class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        self.disponible = False


class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def calcular_total(self):
        return self.dias * self.habitacion.precio

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.reservar()
            return "Reserva confirmada"
        else:
            return "Habitación no disponible"


# Programa principal
cliente1 = Cliente("María Gabriela", "0102030405")
habitacion1 = Habitacion(101, "Matrimonial", 40)
reserva1 = Reserva(cliente1, habitacion1, 3)

print(cliente1.mostrar_datos())
print(f"Habitación: {habitacion1.numero} - {habitacion1.tipo}")
print(reserva1.confirmar_reserva())
print(f"Total a pagar: ${reserva1.calcular_total()}")
