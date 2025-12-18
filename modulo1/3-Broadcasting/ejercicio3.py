import numpy as np

# 1. Creamos una matriz de ejemplo
# Usamos seed para que siempre salgan los mismos números al probar
np.random.seed(42) 
matriz = np.random.randint(0, 20, size=(4, 5))

print(f"Matriz:\n{matriz}\n")

# --- RESOLUCIÓN DEL EJERCICIO ---

# 2. Calcular la suma total
suma_total = np.sum(matriz)
# También funcionaría: matriz.sum()

# 3. Calcular la media (promedio)
media = np.mean(matriz)
# También funcionaría: matriz.mean()

# 4. Calcular la desviación estándar
desviacion = np.std(matriz)
# También funcionaría: matriz.std()

# --- RESULTADOS ---
print(f"Suma total de elementos: {suma_total}")
print(f"Media (Promedio): {media:.2f}") # .2f es para mostrar solo 2 decimales
print(f"Desviación Estándar: {desviacion:.2f}")