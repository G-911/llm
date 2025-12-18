# """Realiza una operación de "broadcasting": crea una 
# matriz de 3x3 y un vector de 3 elementos. 
# Suma el vector a cada fila de la matriz."""

# import numpy as np 

# np.random.seed(0)
# matriz = np.random.randint(0, 10, size=(3, 3))

# vector_elementos = np.random.randint(0, 10, size=(3))
# vector = np.array(vector_elementos) # <--- ESTA LÍNEA ES REDUNDANTE

# print(f"la matriz es: \n {matriz}")
# print(f"El vector es: \n {vector}")
# print(f"la suma del vector con la matriz es: \n {matriz + vector}")

# print(f"la suma del vector con el lado izquierdo de la matriz es: \n {matriz[:3, :1] + vector}")
# print(f"La suma del vector con el lado derecho de la matriz es: \n {matriz[:3, -1:] + vector}")

"""Solucion de la IA"""
"""Realiza una operación de "broadcasting"."""

import numpy as np 

np.random.seed(0)

# 1. Crear matriz (3x3)
matriz = np.random.randint(0, 10, size=(3, 3))

# 2. Crear vector (3 elementos)
# Corrección: Lo asignamos directo a la variable 'vector'
vector = np.random.randint(0, 10, size=(3))

print(f"Matriz:\n{matriz}\n")
print(f"Vector:\n{vector}\n")

# 3. Broadcasting estándar (Suma a cada fila)
print("-" * 20)
print(f"Suma (Matriz + Vector):\n{matriz + vector}")

# 4. Broadcasting avanzado (Columna + Fila = Nueva Matriz)
print("-" * 20)
print("Suma de la primera columna (vertical) + el vector (horizontal):")
# Esto crea una nueva matriz 3x3 donde cada fila es el vector desplazado por el valor de la columna
print(matriz[:3, :1] + vector)