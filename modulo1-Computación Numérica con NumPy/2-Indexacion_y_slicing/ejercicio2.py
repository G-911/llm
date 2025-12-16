"""Selecciona las primeras dos filas y las últimas dos columnas de tu matriz 5x5."""

import numpy as np

np.random.seed(0) 
matriz_numpy = np.random.randint(0, 10, size=(5, 5))

print(f"La matriz = \n {matriz_numpy}")

print(f"Primeras dos filas = \n {matriz_numpy[:2, :]}")
print(f"Ultimas dos columnas = \n {matriz_numpy[: , -2:]}")

print(f"Primeras dos filas con ultimas dos columnas = \n {matriz_numpy[:2, -2:]}")

print(f"matriz > 5 = {matriz_numpy[matriz_numpy > 5]}")