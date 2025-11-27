"""**Ejercicios Prácticos:**

    1. **Creación y Atributos de Arreglos:**
        - [ ]  Crea un vector (arreglo de 1D) de 10 ceros.
        - [ ]  Crea una matriz (arreglo de 2D) de 5x5 con valores aleatorios entre 0 y 1.
        - [ ]  Crea un arreglo con valores espaciados uniformemente del 10 al 50.
        - [ ]  Inspecciona los atributos de tus arreglos: shape, ndim y dtype.
"""

import numpy as np
# Corrección: Quita "modulo1." de las importaciones
from ejercicio1 import vector_numpy
from ejercicio2 import matriz_numpy
from ejercicio3 import arreglo_numpy

print("--- Vector de Ceros ---")
print(f"Dimensiones: {vector_numpy.ndim}")
print(f"Forma: {vector_numpy.shape}")
print(f"Tipo de Dato: {vector_numpy.dtype}")
print("-" * 25) # Un separador para que sea más legible

print("--- Matriz Aleatoria ---")
print(f"Dimensiones: {matriz_numpy.ndim}")
print(f"Forma: {matriz_numpy.shape}")
print(f"Tipo de Dato: {matriz_numpy.dtype}")
print("-" * 25)

print("--- Arreglo Espaciado ---")
print(f"Dimensiones: {arreglo_numpy.ndim}")
print(f"Forma: {arreglo_numpy.shape}")
print(f"Tipo de Dato: {arreglo_numpy.dtype}")
print("-" * 25)

# lote = np.array([
#     [3, 4, 6, 9],
#     [4, 5, 6, 5],
#     [4, 1, 3, 4]
#     ])

# print(f"numero de dimensiones = {lote.ndim}")
# print(f"forma de los datos = {lote.shape}")
# print(f"tipo de dato = {lote.dtype}")

# lote2 = np.array([3, 4, 7, 9, 5.5])
# # print(f"el tipo de dato del lote dos es = {lote2.dtype}")