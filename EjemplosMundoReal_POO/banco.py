# Ejemplo del mundo real: Sistema de Cuenta Bancaria

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return "Retiro realizado"
        else:
            return "Fondos insuficientes"

    def mostrar_saldo(self):
        return f"Saldo actual: ${self.saldo}"


# Programa principal
cuenta1 = CuentaBancaria("María Gabriela", 200)

cuenta1.depositar(50)
print(cuenta1.mostrar_saldo())

print(cuenta1.retirar(100))
print(cuenta1.mostrar_saldo())
