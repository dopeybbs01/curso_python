""""
Programa para saber si un número es par e Impar.

"""

# pedimos al usuario que introduzca un número

number = int(input("Dame un número: "))

# numero % 2 calcula el residuo de la división de número entre 2
module= number % 2

# si el residuo es cero es par y si es 1 es impar.
if module == 0:
    print(f"{number} es par")
else:
    print(f"{number} es impar")
