# -*- coding: utf-8 -*-
"""Matrizes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zAIrO3jkpxFp5mtYmHu3VN75hv12Rihx

# Matrizes
"""

import numpy as np

matriz = np.array([[2, 3, 1],
                   [4, 5, 7]])

matriz

matriz.shape

matriz[0]

matriz[1]

matriz[0][2]

matriz[1][2]

matriz.shape

for i in range(matriz.shape[0]):
  print(matriz[i])
  for j in range(matriz.shape[1]):
    print(matriz[i][j])