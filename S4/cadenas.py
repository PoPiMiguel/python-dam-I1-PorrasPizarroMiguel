def analizar_cadena(cadena):
    # Inicializamos los contadores
    vocales = 0
    consonantes = 0
    mayusculas = 0
    total_caracteres = len(cadena)

    # Definimos las vocales
    lista_vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

    for caracter in cadena:
        if caracter.isalpha():  # Si es una letra
            if caracter in lista_vocales:
                vocales += 1
            else:
                consonantes += 1
            if caracter.isupper():
                mayusculas += 1

    # Mostramos los resultados
    print(f"Vocales: {vocales}")
    print(f"Consonantes: {consonantes}")
    print(f"Mayúsculas: {mayusculas}")
    print(f"Número total de caracteres: {total_caracteres}")


# Programa principal
texto = input("Introduce una cadena: ")
analizar_cadena(texto)
