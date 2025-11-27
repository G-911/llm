"""Extrae todos los elementos mayores a 0.5 de tu matriz aleatoria."""

import numpy as np

np.random.seed(0)
matriz_numpy = np.random.randint(0, 10, size=(5, 5))

print(f"matriz = {matriz_numpy}")
print(f"valores mayores a 5 = {matriz_numpy[matriz_numpy > 5]}")