"""
Programa para saber si la persona es mayor de edad

"""

# Declaramos una constante
ADULT_AGE = 18

# pedimos al usuario que introduzca su edad

age_perso = int(input("Ingresa tu edad: "))

# evaluamos si la edad de la persona es mayor o igual a 18.
if age_perso >= ADULT_AGE:
    print(f"Tu edad {age_perso}. Eres un aduto.")
else:
    print(f"Tu edad {age_perso}. Eres menor de edad") 