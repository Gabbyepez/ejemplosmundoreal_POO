"""
Universidad Estatal Amazónica
Asignatura: Programación Orientada a Objetos
Tema: Implementación de Constructores y Destructores en Python

Descripción:
Este programa demuestra el uso de constructores (__init__) y destructores (__del__)
en Python. El constructor inicializa los atributos del objeto y el destructor
libera los recursos utilizados, como el cierre de un archivo.
"""

# Definición de la clase
class Archivo:
    def __init__(self, nombre_archivo):
        """
        CONSTRUCTOR (__init__):
        Se ejecuta automáticamente cuando se crea el objeto.
        Inicializa el nombre del archivo y abre el archivo para escritura.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, "w", encoding="utf-8")
        print("✔ Constructor ejecutado: archivo abierto correctamente.")

    def escribir(self, texto):
        """
        Método que permite escribir texto en el archivo.
        """
        self.archivo.write(texto + "\n")
        print("✍ Texto escrito en el archivo.")

    def __del__(self):
        """
        DESTRUCTOR (__del__):
        Se ejecuta cuando el objeto se elimina de la memoria.
        Cierra el archivo y libera los recursos utilizados.
        """
        self.archivo.close()
        print("🧹 Destructor ejecutado: archivo cerrado y recursos liberados.")


# Programa principal
if __name__ == "__main__":
    # Creación del objeto (aquí se activa el constructor)
    archivo1 = Archivo("constructores_destructores.txt")

    # Uso del objeto
    archivo1.escribir("Universidad Estatal Amazónica")
    archivo1.escribir("Asignatura: Programación Orientada a Objetos")
    archivo1.escribir("Tema: Constructores y Destructores")
    archivo1.escribir("Ejemplo práctico en Python")

    # Eliminación del objeto (aquí se activa el destructor)
    del archivo1

