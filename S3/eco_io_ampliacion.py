
while True:
	comando = input("Escribe 'salir' para terminar o pulsa Enter para continuar: ").strip().lower()
	if comando == "salir":
		print("Programa finalizado.")
		break
	numeros = []
	# Con un bucle for pide 3 números al usuario, asegurándose de que son válidos
	for i in range(1, 4):
		while True:
			try:
				num = float(input(f"Introduce el número {i}: "))
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

