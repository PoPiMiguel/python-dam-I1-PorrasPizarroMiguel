# Pedir al usuario una lista de números separados por comas
entrada = input("Introduce una lista de números separados por comas: ")

# Convertir la entrada en una lista de floats
numeros = [float(x.strip()) for x in entrada.split(",")]

# Calcular suma, media y máximo
suma = sum(numeros)
media = suma / len(numeros)
maximo = max(numeros)

# Detectar duplicados
duplicados = set([x for x in numeros if numeros.count(x) > 1])

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Media: {media}")
print(f"Máximo: {maximo}")

if duplicados:
    print(f"Números duplicados: {duplicados}")
else:
    print("No hay números duplicados.")
