# Lista para almacenar los estudiantes
estudiantes = []

# Ciclo para ingresar estudiantes y sus notas
while True:
    nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    
    try:
        nota = float(input(f"Ingrese la nota de {nombre}: "))
        estudiantes.append({"nombre": nombre, "nota": nota})
    except ValueError:
        print("Error: La nota debe ser un número.")

# erificar q se ingresaron estudiantes
if len(estudiantes) == 0:
    print("No se ingresaron estudiantes.")
else:
    # Número de estudiantes
    num_estudiantes = len(estudiantes)

    # Calcular el promedio de notas
    suma_notas = sum(estudiante["nota"] for estudiante in estudiantes)
    promedio = suma_notas / num_estudiantes

    # buscar al estudiante con la not a mas alta 
    mejor = max(estudiantes, key=lambda x: x["nota"])
    mejor_nombre = mejor["nombre"]
    mejor_nota = mejor["nota"]

    # busacar al estudiante con la nota mas baja 
    peor = min(estudiantes, key=lambda x: x["nota"])
    peor_nombre = peor["nombre"]
    peor_nota = peor["nota"]

    # reporte final
    print(f"\nNúmero de estudiantes: {num_estudiantes}")
    print(f"Promedio de notas: {promedio:.2f}")
    print(f"Mejor estudiante: {mejor_nombre} con nota {mejor_nota:.2f}")
    print(f"Peor estudiante: {peor_nombre} con nota {peor_nota:.2f}")

    # ordenar los estudiantes de menor a mayor nota
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x["nota"])
    print("\nEstudiantes ordenados de menor a mayor nota:")
    for estudiante in estudiantes_ordenados:
        print(f"{estudiante['nombre']}: {estudiante['nota']:.2f}")
