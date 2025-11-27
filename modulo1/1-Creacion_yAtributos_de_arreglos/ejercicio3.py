"""**Ejercicios Prácticos:**

    1. **Creación y Atributos de Arreglos:**
        - [ ]  Crea un vector (arreglo de 1D) de 10 ceros.
        - [ ]  Crea una matriz (arreglo de 2D) de 5x5 con valores aleatorios entre 0 y 1.
        - [ ]  Crea un arreglo con valores espaciados uniformemente del 10 al 50.
        - [ ]  Inspecciona los atributos de tus arreglos: shape, ndim y dtype.
"""

"""Ejercicio 3"""
# import numpy as np

# arreglo_numpy = []
# n = 10

# while(n <= 50):
#     if(n <= 50):
#         arreglo_numpy.append(n)
#     n += 1
    
# print(arreglo_numpy)

"""SOLUCION"""
import numpy as np

arreglo_numpy = np.arange(10, 51)
print(arreglo_numpy)