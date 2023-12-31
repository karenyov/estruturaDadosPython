# -*- coding: utf-8 -*-
"""Notação Big-O.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B4kcOEG5iDkT8N07NjPnOOXXWcp6VfZo

# Notação Big-O

- Como comparar dois algoritmos?
- Comparação objetiva entre algoritmos
- Considera diferenças entre poder de processamento, sistema operacional, linguagem de programação
- O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas

## Função 1 - O(n)
"""

# 11 passos
def soma1(n):
  soma = 0
  for i in range(n + 1):
    soma += i

  return soma

soma1(10)

# Commented out IPython magic to ensure Python compatibility.
# %timeit soma1(10)

"""## Função 2"""

(10 * 11) / 2

# 3 passos
# O(3)
def soma2(n):
  return (n * (n + 1)) / 2

soma2(10)

# Commented out IPython magic to ensure Python compatibility.
# %timeit soma2(10)

"""## Função 3

- https://wiki.python.org/moin/TimeComplexity
- https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
"""

# O(1000) -> O(n)
def lista1():
  lista = []
  for i in range(1000):
    lista += [i]
  return lista

print(lista1())

len(lista1())

# Commented out IPython magic to ensure Python compatibility.
# %timeit lista1()

"""## Função 4"""

def lista2():
  return range(1000)

l = lista2()

for i in l:
  print(i)

# Commented out IPython magic to ensure Python compatibility.
# %timeit lista2()

"""## Funções Big-O

- 1	Constant
- log(n)	Logarithmic
- n	Linear
- nlog(n)	Log Linear
- n^2	Quadratic
- n^3	Cubic
- 2^n	Exponential

"""

from math import log
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)

len(n)

n

n.shape

np.ones(n.shape)

n

np.log(n)

n

n * np.log(n)

n

n**2

n

n**3

n

2**n

labels = ['Constant', 'Logarithmic', 'Linear', 'Log linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(10,8))
plt.ylim(0, 100)
for i in range(len(big_o)):
  plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')

"""## Exemplos Big-O

- https://www.bigocheatsheet.com/

### Constant - O(1)
"""

lista = [1, 2, 3, 4, 5]

def constant(n):
  print(n[0])
  print(n[1])

constant(lista)

"""### Linear - O(n)"""

def linear(n):
  for i in n:
    print(i)

linear(lista)

"""### Quadratic - O(n^2) - polynomial"""

def quadratic(n):
  for i in n:
    for j in n:
      print(i, j)
    print('---')

quadratic(lista)

"""### Combination"""

# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) -> O(n)

def combination(n):
  # O(1)
  print(n[0])

  # O(5)
  for i in range(5):
    print('test ', i)

  # O(n)
  for i in n:
    print(i)

  # O(n)
  for i in n:
    print(i)

  # O(3)
  print('Python')
  print('Python')
  print('Python')

combination(lista)