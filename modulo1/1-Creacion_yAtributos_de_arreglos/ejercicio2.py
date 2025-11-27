"""**Ejercicios Prácticos:**

    1. **Creación y Atributos de Arreglos:**
        - [ ]  Crea un vector (arreglo de 1D) de 10 ceros.
        - [ ]  Crea una matriz (arreglo de 2D) de 5x5 con valores aleatorios entre 0 y 1.
        - [ ]  Crea un arreglo con valores espaciados uniformemente del 10 al 50.
        - [ ]  Inspecciona los atributos de tus arreglos: shape, ndim y dtype.
"""

"""Ejercicio 2"""
# import numpy as np

# matriz_numpy = np.array((5, 5))

# print(matriz_numpy)
# print(type(matriz_numpy))

"""Solucion correcta"""

import numpy as np
matriz_numpy = np.random.rand(5, 5)

print(matriz_numpy)
print(type(matriz_numpy))