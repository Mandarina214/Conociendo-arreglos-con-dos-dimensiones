# Programa para declarar y poblar una matriz 3x3 con números enteros

# Inicialización de la matriz 3x3
matriz = [[0 for _ in range(3)] for _ in range(3)]

# Función para poblar la matriz
def poblar_matriz(matriz):
    print("Por favor, ingresa 9 números enteros para poblar la matriz:")
    for i in range(3):
        for j in range(3):
            while True:
                try:
                    valor = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
                    matriz[i][j] = valor
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número entero.")

# Función para calcular la sumatoria de los elementos de la matriz
def calcular_sumatoria(matriz):
    suma = 0
    for fila in matriz:
        suma += sum(fila)
    return suma

# Llamar a la función para poblar la matriz
poblar_matriz(matriz)

# Calcular y mostrar la sumatoria
sumatoria = calcular_sumatoria(matriz)
print("\nLa matriz es:")
for fila in matriz:
    print(fila)

print(f"\nLa sumatoria de los elementos de la matriz es: {sumatoria}")

# Verificar si la sumatoria es igual a 21
if sumatoria == 21:
    print("¡La sumatoria es correcta y es igual a 21!")
else:
    print("La sumatoria no es igual a 21. Por favor, verifica los valores ingresados.")