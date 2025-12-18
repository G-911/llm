"""Suma un escalar (un solo número) a todo un arreglo."""

# import numpy as np
# valor = input("Ingrese un valor de un escalar: ")
# escalar = np.array(int(valor))
# arr = [1, 2, 3, 4, 5]

# print(f"el escalar {escalar.dtype}")
# arreglo_np = np.array(arr)
# print(f"el arreglo {arreglo_np.dtype}")

# print(f"la suma del arreglo con el escalar es: {escalar + arreglo_np}")

"""Respuesta de la IA"""
import numpy as np

# 1. Recibimos el valor y lo convertimos a entero (int) inmediatamente
valor = int(input("Ingrese un valor de un escalar: ")) 

# 2. Creamos el escalar (ahora sí será numérico)
escalar = np.array(valor)

# 3. Definimos el arreglo
arr = [1, 2, 3, 4, 5]
arreglo_np = np.array(arr)

# Verificamos los tipos (ahora ambos serán int32 o int64)
print(f"El tipo de dato del escalar es: {escalar.dtype}")
print(f"El tipo de dato del arreglo es: {arreglo_np.dtype}")

# 4. Realizamos la suma
# NumPy usa "Broadcasting": toma el escalar y se lo suma a CADA elemento del arreglo
print(f"La suma del arreglo con el escalar es: {escalar + arreglo_np}")