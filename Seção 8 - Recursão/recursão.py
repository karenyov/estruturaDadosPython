# -*- coding: utf-8 -*-
"""Recursão.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vez3YC5pu5GRnKx7oEpDrgk3Ddd6YvOE

# Recursão

## Mostrar mensagens
"""

for _ in range(5):
  print('Recursão')

def recursao(i):
  print('Recursão')
  i += 1
  if i == 5:
    return
  else:
    recursao(i)

recursao(0)

"""## Somar valores"""

def soma1(n):
  soma = 0
  for i in range(n + 1):
    soma += i
  return soma

soma1(5)

def soma2(n):
  if n == 0:
    return 0

  return n + soma2(n - 1)

soma2(5)

# Commented out IPython magic to ensure Python compatibility.
# %timeit soma1(100)

# Commented out IPython magic to ensure Python compatibility.
# %timeit soma2(100)