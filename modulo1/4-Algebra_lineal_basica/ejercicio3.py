"""Resuelve un sistema de ecuaciones lineales simple."""

# import numpy as np

# np.random.seed(0)

# a = np.random.randint(0, 10, size=(2, 2))
# b = np.random.randint(0, 10, size=(2, 2))

# respuesta = np.linalg.solve(a, b)

# print(f"a: \n {a}")
# print(f"b: \n {b}")
# print(f"la solucion es: \n {respuesta}")

"""Solucion de la IA"""
"""Resuelve un sistema de ecuaciones lineales simple."""
import numpy as np

np.random.seed(0)

# Matriz de coeficientes (2x2) -> Correcto
a = np.random.randint(0, 10, size=(2, 2))

# Vector de resultados (Vector de tamaño 2) -> CORREGIDO
# Cambiamos size=(2, 2) por size=(2)
b = np.random.randint(0, 10, size=(2))

# Resolvemos
respuesta = np.linalg.solve(a, b)

print(f"Matriz A (Coeficientes): \n {a}")
print(f"Vector b (Resultados): \n {b}")
print("-" * 20)
print(f"La solución (x, y) es: {respuesta}")

# --- VERIFICACIÓN (La prueba de fuego) ---
# Si multiplicamos A por la solución, debemos obtener b
comprobacion = a @ respuesta
print(f"Comprobación (A @ solución): {comprobacion}")
print(f"¿Es igual a b? {np.allclose(comprobacion, b)}")