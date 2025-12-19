"""Encuentra la inversa y el determinante de una matriz cuadrada."""

import numpy as np 

np.random.seed(0)
matriz = np.random.randint(0, 10, size=(3, 3))

# determinante = np.linalg.det(matriz)
# inversa = np.linalg.inv(matriz)

print(f"la matriz es: \n {matriz}")
print(f"La inversa es: \n {np.linalg.inv(matriz)}")
print(f"El determinante es: \n {np.linalg.det(matriz)}")
print(f"La matriz identidad: \n {np.round(matriz @ np.linalg.inv(matriz))}")

"""Solucion de la IA"""

# import numpy as np 

# np.random.seed(0)
# matriz = np.random.randint(0, 10, size=(3, 3))

# print(f"La matriz original es:\n{matriz}")

# # Calculamos el determinante primero
# det = np.linalg.det(matriz)
# print(f"El determinante es: {det:.2f}") # .2f para mostrar solo 2 decimales

# # Verificamos si es seguro calcular la inversa (evitar división por cero)
# # Usamos np.isclose porque comparar floats con == 0 es peligroso
# if np.isclose(det, 0):
#     print("¡Cuidado! La matriz es singular (determinante 0). No tiene inversa.")
# else:
#     inversa = np.linalg.inv(matriz)
#     print(f"La inversa es:\n{inversa}")
    
#     # --- PASO EXTRA: VERIFICACIÓN ---
#     # Multiplicamos la original por la inversa. Debería dar la Identidad.
#     check = matriz @ inversa
    
#     # Usamos np.round para limpiar el "ruido" numérico (ej: 0.99999 -> 1.0)
#     print(f"\nVerificación (Matriz @ Inversa = Identidad):\n{np.round(check)}")