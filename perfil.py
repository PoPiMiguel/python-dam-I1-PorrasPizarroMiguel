#Pedir nombre + año de nacimiento
#Calcular edad
#Clasificar por tramos de edad (<18, 18-65, >65)
#Manejo de error si no mete numero
#Comentarios en el codigo


# Pedir nombre y año de nacimiento al usuario
nombre = input("Introduce tu nombre: ")

while True:
    try:
        ano_nacimiento = int(input("Introduce tu año de nacimiento: "))
        break
    except ValueError:
        print("Por favor, introduce un año válido.")

# Calcular edad
from datetime import datetime
ano_actual = datetime.now().year
edad = ano_actual - ano_nacimiento

# Clasificar por tramos de edad
if edad < 18:
	clasificacion = "Menor de edad (<18)"
elif edad <= 65:
	clasificacion = "Adulto (18-65)"
else:
	clasificacion = "Mayor de 65 (>65)"

# Mostrar resultado por pantalla
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Clasificación: {clasificacion}")





#Prompts usados para este ejercicio:
#Primer propt
#Pide el nombre y la edad al usuario, clasificarlo por edades (<18, 18-65, >65) y mostrarlo por pantalla
#Segundo prompt (El primero no calculaba la edad, fallo mio por no concretarlo)
#Pide el año de nacimiento y calcula la edad