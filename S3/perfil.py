#Pedir nombre + año de nacimiento
#Calcular edad
#Clasificar por tramos de edad (<18, 18-65, >65)
#Manejo de error si no mete numero
#Comentarios en el codigo


# Pedir nombre y año de nacimiento al usuario
nombre = input("Introduce tu nombre: ")

#Mientras que no se introduzca un año válido, el programa seguirá pidiendo el año
while True:
    try:
        ano_nacimiento = int(input("Introduce tu año de nacimiento: "))
        break
    except ValueError:
        print("Por favor, introduce un año válido.")

# Calcular edad
#Creo que esto es una librería de python para manejar fechas
from datetime import datetime
#Aqui se obtiene el año actual y se calcula la edad restando el año de nacimiento
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
