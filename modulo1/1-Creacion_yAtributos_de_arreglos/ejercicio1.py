"""**Ejercicios Prácticos:**

    1. **Creación y Atributos de Arreglos:**
        - [ ]  Crea un vector (arreglo de 1D) de 10 ceros.
        - [ ]  Crea una matriz (arreglo de 2D) de 5x5 con valores aleatorios entre 0 y 1.
        - [ ]  Crea un arreglo con valores espaciados uniformemente del 10 al 50.
        - [ ]  Inspecciona los atributos de tus arreglos: shape, ndim y dtype.
"""

"""Ejercicio 1"""
vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Mi solucion

"""Solucion correcta"""
import numpy as np

vector_numpy = np.zeros(10)

print(vector_numpy)
print(type(vector_numpy))