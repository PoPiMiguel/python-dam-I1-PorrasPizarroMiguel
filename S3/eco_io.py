# Pedir al usuario 3 números, calcular suma, media y mayor
#Crea una lista para almacenar los números
numeros = []
#Con un bucle for pide 3 números al usuario, asegurándose de que son válidos
for i in range(1, 4):
	while True:
		try:
			num = float(input(f"Introduce el número {i}: "))
			#.append añade el número a la lista
			numeros.append(num)
			break
		except ValueError:
			print("Por favor, introduce un número válido.")

suma = sum(numeros)
media = suma / 3
mayor = max(numeros)

print(f"Suma: {suma}")
print(f"Media: {media}")
print(f"Mayor: {mayor}")

#Aquí añadire la adaptacion libre. En este caso ordenare los numeros de menor a mayor y los mostrare
numeros_ordenados = sorted(numeros)