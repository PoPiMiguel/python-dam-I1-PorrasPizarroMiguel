def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# Programa principal
try:
    num = int(input("Introduce un número: "))
    if es_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
except ValueError:
    print("Por favor, introduce un número entero válido.")
