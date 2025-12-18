"""Multiplica dos matrices elemento a elemento (Hadamard)."""

import numpy as np 

np.random.seed(0)

matriz_1 = np.random.randint(0, 10, size = (3, 5))
matriz_2 = np.random.randint(0, 10, size = (3, 5))

print(f"Matriz 1 = \n {matriz_1} \n")
print(f"Matriz 2 = \n {matriz_2} \n")

print(f"La multiplicacion elemento a elemento es = \n {matriz_1 * matriz_2}")