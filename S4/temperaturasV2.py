# Conversor de Temperaturas con Menú

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


def conversor():
    print("\n=== Conversor de Temperaturas ===")
    print("Tipos disponibles: Celsius (C), Kelvin (K), Fahrenheit (F)")

    origen = input("¿Qué tipo de temperatura vas a introducir? (C/K/F): ").strip().upper()
    destino = input("¿A qué unidad quieres convertir? (C/K/F): ").strip().upper()

    # Validar entrada
    if origen not in ["C", "K", "F"] or destino not in ["C", "K", "F"]:
        print("Opción no válida. Usa C, K o F.")
        return

    if origen == destino:
        print("No tiene sentido convertir a la misma unidad.")
        return

    try:
        valor = float(input(f"Introduce el valor en {origen}: "))
    except ValueError:
        print("Valor numérico inválido.")
        return

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

    print(f"{valor}°{origen} equivalen a {resultado:.2f}°{destino}")


def menu():
    while True:
        print("\n==============================")
        print("      CONVERSOR DE TEMPERATURAS")
        print("==============================")
        print("1. Realizar una conversión")
        print("2. Salir")

        opcion = input("Selecciona una opción (1/2): ")

        if opcion == "1":
            conversor()
        elif opcion == "2":
            print("Gracias por usar el conversor. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


# Programa principal
if __name__ == "__main__":
    menu()
