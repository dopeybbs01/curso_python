"""
Programa para saber si el valor está dentro del rango.
"""

# declaramos las constantes

MINIMUM_VALUE = 0
MAXIMUM_VALUE = 5

# Pedimos al usuario que introduzca un valor
value = int(input("Ingresa un valor: "))

# Evaluamos el valor introducido por el usuario con las cantidades minima y maxima y la guardamos en range.
 
range = value >= MINIMUM_VALUE and value <= MAXIMUM_VALUE

# finalmente hacemos la pregunta y dependiendo de lo tenga range almacenado nos arrojará el mensase

if range:
    print(f"El valor {value} está dentro del rango.")
else:
    print(f"El valor {value} está fuera del rango.")