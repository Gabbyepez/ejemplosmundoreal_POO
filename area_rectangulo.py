"""
Programa: Cálculo del área de un rectángulo
Asignatura: Programación
Tema: Tipos de datos e identificadores en Python
Descripción:
Este programa calcula el área de un rectángulo usando medidas ya definidas
en metros y muestra el resultado en metros cuadrados (m²).
Se utilizan tipos de datos string, float y boolean,
con identificadores en snake_case.
Autor: Gabriela Yepez
"""

# Función que calcula el área de un rectángulo
def calcular_area_rectangulo(largo_metros, ancho_metros):
    return largo_metros * ancho_metros


# Datos ya definidos (medidas)
nombre_usuario = "Gabriela"     # Tipo de dato: string
largo_metros = 5.0              # Tipo de dato: float (metros)
ancho_metros = 3.0              # Tipo de dato: float (metros)

# Cálculo del área
area_metros_cuadrados = calcular_area_rectangulo(largo_metros, ancho_metros)

# Validación del área
area_valida = area_metros_cuadrados > 0  # Tipo de dato: boolean

# Salida de resultados
print("--- RESULTADOS ---")
print(f"Usuario: {nombre_usuario}")
print(f"Largo del rectángulo: {largo_metros} m")
print(f"Ancho del rectángulo: {ancho_metros} m")
print(f"Área del rectángulo: {area_metros_cuadrados} m²")

if area_valida:
    print("El área calculada es válida.")
else:
    print("El área no es válida.")

