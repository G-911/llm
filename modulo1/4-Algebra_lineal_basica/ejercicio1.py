"""Calcula el producto punto de dos vectores."""

import numpy as np 

vector = np.random.randint(0, 10, size=(3))
vector2 = np.random.randint(0,10, size=(3))

print(f"El vector1 es: \n {vector}")
print(f"El vector2 es: \n {vector2}")

vector_aux = vector * vector2

producto_punto = 0

# for i in vector_aux:  <-- No volver a utilizar un for en numpy
#     producto_punto += i

producto_punto = vector_aux.sum() # <-- Recomendacion de la ia

print(f"el producto punto es: {producto_punto}")

# """Solucion de la ia"""

# import numpy as np

# # Creamos dos vectores (ejemplo: embeddings simplificados de dos palabras)
# vector_a = np.array([1, 2, 3])
# vector_b = np.array([4, 5, 6])

# # Forma clásica de NumPy
# producto_punto = np.dot(vector_a, vector_b)

# # Forma moderna (recomendada en Python 3.5+) usando el operador @
# producto_punto_moderno = vector_a @ vector_b

# print(f"Producto punto: {producto_punto}")
# # Matemáticamente hizo: (1*4) + (2*5) + (3*6) = 4 + 10 + 18 = 32