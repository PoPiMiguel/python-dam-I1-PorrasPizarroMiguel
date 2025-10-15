# Pedir notas al usuario
print("Introduce las calificaciones entre 0 y 10 separadas por comas (ejemplo: 6.5, 8, 5, 4, 9, 10, 7, 3)")
entrada = input("> ")

try:
    # Convertir la entrada en lista de números y validar rango
    notas = []
    for nota in entrada.split(','):
        valor = float(nota.strip())
        if valor < 0 or valor > 10:
            raise ValueError("Las notas deben estar entre 0 y 10")
        notas.append(valor)
    
    # Cálculos básicos
    total_notas = len(notas)
    media = sum(notas) / total_notas
    nota_minima = min(notas)
    nota_maxima = max(notas)
    
    # Calcular porcentajes
    aprobados = len([n for n in notas if n >= 5])
    sobresalientes = len([n for n in notas if n >= 9])
    porcentaje_aprobados = (aprobados / total_notas) * 100
    porcentaje_sobresalientes = (sobresalientes / total_notas) * 100
    
    # Encontrar la moda (nota más repetida)
    frecuencia = {}
    for nota in notas:
        frecuencia[nota] = frecuencia.get(nota, 0) + 1
    moda = [nota for nota, freq in frecuencia.items() if freq == max(frecuencia.values())]
    
    # Mostrar resultados
    print("\nResumen Estadístico:")
    print(f"▪ Total de notas: {total_notas}")
    print(f"▪ Media: {media:.2f}")
    print(f"▪ Nota mínima: {nota_minima}")
    print(f"▪ Nota máxima: {nota_maxima}")
    print(f"▪ Porcentaje de aprobados: {porcentaje_aprobados:.1f}%")
    print(f"▪ Porcentaje de sobresalientes: {porcentaje_sobresalientes:.1f}%")
    print(f"▪ Nota(s) más repetida(s): {', '.join(map(str, moda))}")
    
    # Mensaje final
    if media >= 8:
        print("\nNivel excelente")
    elif media >= 5:
        print("\nNivel medio")
    else:
        print("\nNecesita refuerzo")
        
except ValueError as e:
    if str(e) == "Las notas deben estar entre 0 y 10":
        print("Error: Las notas deben estar entre 0 y 10")
    else:
        print("Error: Por favor, introduce números válidos separados por comas.")