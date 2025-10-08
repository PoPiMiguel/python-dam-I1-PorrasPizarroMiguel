# Programa conversor de temperaturas

def celsius_a_kelvin(c):
    return c + 273.15

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def kelvin_a_celsius(k):
    return k - 273.15

def kelvin_a_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_a_kelvin(f):
    return (f - 32) * 5/9 + 273.15

print("=== Conversor de Temperaturas ===")
print("Tipos disponibles: Celsius (C), Kelvin (K), Fahrenheit (F)")

# Solicita la unidad de entrada
origen = input("¿Qué tipo de temperatura vas a introducir? (C/K/F): ").strip().upper()

# Solicita la unidad de salida
destino = input("¿A qué unidad quieres convertir? (C/K/F): ").strip().upper()

# Solicita el valor numérico
valor = float(input(f"Introduce el valor en {origen}: "))

# Realiza la conversión según las opciones elegidas
resultado = None

if origen == "C":
    if destino == "K":
        resultado = celsius_a_kelvin(valor)
    elif destino == "F":
        resultado = celsius_a_fahrenheit(valor)
elif origen == "K":
    if destino == "C":
        resultado = kelvin_a_celsius(valor)
    elif destino == "F":
        resultado = kelvin_a_fahrenheit(valor)
elif origen == "F":
    if destino == "C":
        resultado = fahrenheit_a_celsius(valor)
    elif destino == "K":
        resultado = fahrenheit_a_kelvin(valor)

# Muestra el resultado o mensaje de error
if resultado is not None:
    print(f"{valor}°{origen} equivalen a {resultado:.2f}°{destino}")
else:
    print("Conversión no válida. Asegúrate de usar C, K o F correctamente.")
